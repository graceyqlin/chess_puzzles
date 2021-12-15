## About
This repo contains a chess puzzle scraper that can scrape chess puzzles from user defined web or local files. 

It also transforms chess puzzle data in FEN format to a format that can be easily consumed by downstream task.

Testing functions are saved in get _ puzzle _ test.py.

Users can either run the scrips directly or run it from command line. 

## Main Functionality:

1. get data

	a. from web,  example link: https://wtharvey.com/m8n2.txt
	
	b. from local, example path: data/m8n2.txt
	
2. transform FEN format 

	FROM: 
	
		{'id': 1, 'board': ['1rb4r', 'pkPp3p', '1b1P3n', '1Q6', 'N3Pp2', '8', 'P1P3PP', '7K'], 'moves': ['Qd', 'Ka', 'cxbN#']}
	
	TO:
	
		{'id': 1, 'board': [[{None}, {'type': 'rook', 'side': 'white'}, {'type': 'bishop', 'side': 'white'}, {None}, {None}, {None}, {None}, {'type': 'rook', 'side': 'white'}], [{'type': 'pawn', 'side': 'white'}, {'type': 'king', 'side': 'white'}, {'type': 'pawn', 'side': 'black'}, {'type': 'pawn', 'side': 'white'}, {None}, {None}, {None}, {'type': 'pawn', 'side': 'white'}], [{None}, {'type': 'bishop', 'side': 'white'}, {None}, {'type': 'pawn', 'side': 'black'}, {None}, {None}, {None}, {'type': 'knight', 'side': 'white'}], [{None}, {'type': 'queen', 'side': 'black'}, {None}, {None}, {None}, {None}, {None}, {None}], [{'type': 'knight', 'side': 'black'}, {None}, {None}, {None}, {'type': 'pawn', 'side': 'black'}, {'type': 'pawn', 'side': 'white'}, {None}, {None}], [{None}, {None}, {None}, {None}, {None}, {None}, {None}, {None}], [{'type': 'pawn', 'side': 'black'}, {None}, {'type': 'pawn', 'side': 'black'}, {None}, {None}, {None}, {'type': 'pawn', 'side': 'black'}, {'type': 'pawn', 'side': 'black'}], [{None}, {None}, {None}, {None}, {None}, {None}, {None}, {'type': 'king', 'side': 'black'}]], 'moves': ['Qd', 'Ka', 'cxbN#']}
		
## Testing:


	$pytest -v
	
You can see
	
	get_puzzle_test.py::test_get_fen_block_from_web PASSED                                                [ 33%]
	get_puzzle_test.py::test_get_single_transform_board PASSED                                            [ 66%]
	get_puzzle_test.py::test_get_aggregate_transform_block PASSED                                         [100%]
		
		============================================= 3 passed in 0.62s =============================================
		

	
## Running From Command Line:

1. Provide the path of where the raw FEN data is saved locally. Default is to process data from web.

		$python command.py --local_path='data/m8n2.txt'
		
2. Provide the web link of where the raw FEN data is stored. Default is "https://wtharvey.com/m8n2.txt"
                       
        $python command.py --web_link="https://wtharvey.com/m8n2.txt"
        
3. Provide how many moves of the puzzles to get. You can input any of 2, 3, 4, or combination of the 3 numbers. Default is 2.

        $python command.py --number_of_moves=2,3,4
  			
4. Provide the local path to save the data files. Default is to create a puzzle_folder under the same directory
	
		$python command.py --data_storage_path='/Users/lin/Desktop/test'

5. Specify the max number of puzzles to be processed and saved. Default is unlimited
				                        
		$python command.py --max_number_of_puzzles=10

6. Specify whether to randomize the puzzles. You can input True or False. Default is False.
		
		$python command.py --whether_randomize_puzzles=True
                        