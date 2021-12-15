import argparse
from get_puzzle import DataProcess
from datetime import datetime
import random

parser = argparse.ArgumentParser(description='Description of your program')
parser.add_argument('--local_path', help='Provide the path of where the raw FEN data is saved locally. Default is to process data from web.')
parser.add_argument('--web_link', help='Provide the web link of where the raw FEN data is stored. Default is "https://wtharvey.com/m8n2.txt"')
parser.add_argument('--number_of_moves', help='Provide how many moves of the puzzles to get. You can input any of 2, 3, 4, or combination of the 3 numbers. Default is 2')
parser.add_argument('--data_storage_path', help='Provide the local path to save the data files. Default is to create a puzzle folder under the same directory')
parser.add_argument('--max_number_of_puzzles', help='Specify the max number of puzzles to be processed and saved. Default is unlimited')
parser.add_argument('--whether_randomize_puzzles', help='Specify whether to randomize the puzzles. You can input True or False. Default is False')

args = vars(parser.parse_args())

dp = DataProcess()

def get_max_puzzles_and_randomize(agg_fen_block, max_number_of_puzzles, whether_randomize_puzzles):
    '''
    This function allows users to specify max number of puzzless to be processed and whether to randomize the puzzles
    :param:max_number_of_puzzles is the max number of puzzles designated by the user
    :param:whether_randomize_puzzles is whether to randomly select puzzles
    :return: max_and_randomize_block, an aggregate block that are processed based on the inputs
    '''
    if max_number_of_puzzles:
        max_number_of_puzzles = min(max_number_of_puzzles, len(agg_fen_block))
    else:
        max_number_of_puzzles = len(agg_fen_block)

    if whether_randomize_puzzles:
        selected_id = random.sample(range(0, len(agg_fen_block)), max_number_of_puzzles)
    else:
        selected_id = list(range(0, max_number_of_puzzles))
    
    max_and_randomize_block = []
    for fen_block in agg_fen_block:
        if fen_block['id'] in selected_id:
            max_and_randomize_block.append(fen_block)

    return max_and_randomize_block

def process_and_save(agg_fen_block, path = None):
    '''
    This function process and save FEN blocks to local files. 
    :param: agg_fen_block is input FEN blocks to be processed and saved locally
    :param: path: where to save the processed files
    '''
    agg_transform_block = dp.get_aggregate_transform_block(agg_fen_block)
    dp.save_json_files(agg_transform_block, path)
    now = datetime.now()
    print('Great! Data has been processed at', now, '. Check out puzzle_folder or designated path for more details!')


def run_from_command_line():
    '''
    This function supports running the script from command line
    '''

    data_storage_path = args['data_storage_path']
    max_number_of_puzzles = int(args['max_number_of_puzzles'])
    whether_randomize_puzzles = args['whether_randomize_puzzles']

    if args['local_path']:
        agg_fen_block = dp.get_fen_block_from_local(args['local_path'])
            
    elif args['web_link']:
        agg_fen_block = dp.get_fen_block_from_web(args['web_link'])

    elif args['number_of_moves']:
        moves = str(args['number_of_moves'])
        if moves in ['2', '3', '4', '2,3', '3,4', '2,3,4']:
            agg_fen_block = []
            for move in moves.split(','):
                web_link = "https://wtharvey.com/m8n" + move + ".txt"
                current_agg_fen_block = dp.get_fen_block_from_web(web_link)
                for block in current_agg_fen_block:
                    agg_fen_block.append(block)
            print('Getting ', moves, 'moves of data!')

    else:
        agg_fen_block = dp.get_fen_block_from_web()

    max_and_randomize_block = get_max_puzzles_and_randomize(agg_fen_block, max_number_of_puzzles, whether_randomize_puzzles)
    
    process_and_save(max_and_randomize_block, data_storage_path)


if __name__ == "__main__":
    run_from_command_line()