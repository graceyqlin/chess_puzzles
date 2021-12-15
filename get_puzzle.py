import json
import urllib.request
import os
import re
from datetime import datetime

class DataProcess():

    def get_fen_block_from_local(self, local_file_path = 'm8n2.txt'):
        """
        This function gets initial board position in FEN format and solution moves from a saved local file.
        
        Raw data for one of the game:
            Henry Buckle vs NN, London, 1840
            r2qkb1r/pp2nppp/3p4/2pNN1B1/2BnP3/3P4/PPP2PPP/R2bK2R w KQkq - 1 0
            1. Nf6+ gxf6 2. Bxf7# 
        
        param: local_file_path is the location where the file is saved
        
        return: an aggregate data with id, initial board position in FEN format, and moves 
        (for example {id:1, board: 'r2qkb1r/pp2nppp/3p4/2pNN1B1/2BnP3/3P4/PPP2PPP/R2bK2R', moves: Nf6+, gxf6 , Bxf7#})
        """
    
    
        file1 = open(local_file_path, 'r')
        Lines = file1.readlines()
        block_id = 0     
        agg_fen_block = []
        
        for row, line in enumerate(Lines):

            # getting lines with the initial positions
            if "/" in line:

                # getting lines start with the white
                if line.split()[1] == 'w':
                    
                    # empty block as a placeholder to add values
                    current_fen_block = {}
                    
                    # adding id to the block, starting with 0
                    current_fen_block['id'] = block_id         
                    block_id += 1
                    
                    # adding raw board position to the board
                    raw_board_position = line.split()[0].split('/')       
                    current_fen_block['board'] = raw_board_position
                    
                    # adding moves to the block
                    next_line = Lines[row + 1]
                    move = next_line.replace('\n', '')
                    move = re.sub('[0-9].', '', move)
                    move = move.split()
                    current_fen_block['moves'] = move
                    
                    # appending the current board to aggregate board
                    agg_fen_block.append(current_fen_block)
        
        return agg_fen_block

    
    def get_fen_block_from_web(self, url = "https://wtharvey.com/m8n2.txt"):
        """
        This function gets initial board position in FEN format and solution moves from web.
        
        Example for raw data for one of the game:
            Henry Buckle vs NN, London, 1840
            r2qkb1r/pp2nppp/3p4/2pNN1B1/2BnP3/3P4/PPP2PPP/R2bK2R w KQkq - 1 0
            1. Nf6+ gxf6 2. Bxf7# 
        
        param: url is the link to where the data is saved on the internet
        
        return: agg_fen_block, an aggregate data with id, initial board position in FEN format, and moves 
        (for example {id:1, board: 'r2qkb1r/pp2nppp/3p4/2pNN1B1/2BnP3/3P4/PPP2PPP/R2bK2R', moves: Nf6+, gxf6 , Bxf7#})
        """

        file = urllib. request. urlopen(url)   
        Lines = []
        
        for line in file:
            decoded_line = line. decode("utf-8")
            Lines.append(decoded_line)

        block_id = 0     
        agg_fen_block = []
        
        for row, line in enumerate(Lines):

            # getting lines with the initial positions
            if "/" in line:

                # getting lines start with the white
                if line.split()[1] == 'w':
                    
                    # empty block as a placeholder to add values
                    current_fen_block = {}
                    
                    # adding id to the block, starting with 0
                    current_fen_block['id'] = block_id         
                    block_id += 1
                    
                    # adding raw board position to the board
                    raw_board_position = line.split()[0].split('/')       
                    current_fen_block['board'] = raw_board_position
                    
                    # adding moves to the block
                    next_line = Lines[row + 1]
                    move = next_line.replace('\n', '')
                    move = re.sub('[0-9].', '', move)
                    move = move.split()
                    current_fen_block['moves'] = move
                    
                    # appending the current board to aggregate board
                    agg_fen_block.append(current_fen_block)
        
        return agg_fen_block

    def get_single_transform_board(self, single_fen_board):
        """
        this function transform a single board in FEN format to a format that can be processed by our application chessy.
        For example, ['1rb4r'] would be transformed to 
        [{None},{'type': 'rook', 'side': 'white'},{'type': 'bishop', 'side': 'white'},
        {None}, {None}, {None}, {None}, {'type': 'rook', 'side': 'white'}]
        
        :param: single_fen_board is the raw board in fen format
        :return: single_transform_board is the transformed board in chessy format
        """
        # create a mapping 
        mapping = {'r': {'type':'rook', 'side': 'white'},
            'b': {'type':'bishop', 'side': 'white'},
            'n': {'type': 'knight', 'side': 'white'},
            'k': {'type': 'king', 'side': 'white'},
            'q': {'type': 'queen', 'side': 'white'},
            'p': {'type': 'pawn', 'side': 'white'},
            'R': {'type':'rook', 'side': 'black'},
            'B': {'type':'bishop', 'side': 'black'},
            'N': {'type': 'knight', 'side': 'black'},
            'K': {'type': 'king', 'side': 'black'},
            'Q': {'type': 'queen', 'side': 'black'},
            'P': {'type': 'pawn', 'side': 'black'},
            '0': {None}}
        
        
        single_transform_board = []
        
        for row in single_fen_board:
            # transform the FEN data format to chessy initial board format 
            #(for example, 'r2qkb1r' --> ['r', '0', '0', 'q', 'k', 'b', '0', 'r'])
            transform_row = []
            for item in row:
                if item.isalpha():
                    transform_row.append(item)
                else:
                    for element in int(item) * ['0']:
                        transform_row.append(element)
                        
            # map alphas to chessy's data input type (for example, from 'r' to {'type':'rook', 'side': 'white'})
            transform_row = [mapping[item] for item in transform_row]
            single_transform_board.append(transform_row)
        
        return single_transform_board
        
    
    def get_aggregate_transform_block(self, agg_fen_block):
        """
        this function replace the fen board format with transform format in an aggregate board. 

        :param: agg_fen_block is an aggregate block with the board in fen format
        :return: agg_transform_board is the transform board that has the board in transformed format 
        """
    
        for index, current_block in enumerate(agg_fen_block):
            current_fen_board = current_block['board']
            single_transform_board = self.get_single_transform_board(current_fen_board)
            current_block['board'] = single_transform_board
        
        agg_transform_block = agg_fen_block
        
        return agg_transform_block


    def set_default(self, obj):
        if isinstance(obj, set):
            return list(obj)
        raise TypeError


    def save_json_files(self, aggregate_transform_board, path = None):

        if not path:
            path = os. getcwd() + '/puzzle_folder'

            if not os.path.exists(path):
                os.makedirs(path)
        
        for index, board in enumerate(aggregate_transform_board):
            
            json_board = json.dumps(board, default=self.set_default)
            
            board_name = path + '/' + str(board['id']) + '_board.json'
            
            jsonFile = open(board_name, "w")
            jsonFile.write(json_board)
            jsonFile.close()

    def run(self):
        agg_fen_block = self.get_fen_block_from_web()
        agg_transform_block = self.get_aggregate_transform_block(agg_fen_block)
        self.save_json_files(agg_transform_block)
        now = datetime.now()
        print('Great! Data has been processed at', now, '. Check out puzzle_folder or designated folder for more details!')

        
    
if __name__ == "__main__":
    DataProcess().run()
    