from get_puzzle import DataProcess
import os
import json
import pytest
from unittest.mock import patch

dp = DataProcess()

def test_get_fen_block_from_web():
    """
    a test function for get_fen_block_from_web
    """
    aggregate_block = dp.get_fen_block_from_web(url = "https://wtharvey.com/m8n2.txt")
    block1 = aggregate_block[1]
    block10 = aggregate_block[10]
    assert block1 == {'id': 1, 'board': ['1rb4r', 'pkPp3p', '1b1P3n', '1Q6', 'N3Pp2', '8', 'P1P3PP', '7K'], 'moves': ['Qd', 'Ka', 'cxbN#']}
    assert block10 == {'id': 10, 'board': ['r2q1b1r', '1pN1n1pp', 'p1n3k1', '4Pb2', '2BP4', '8', 'PPP3PP', 'R1BQ1RK1'], 'moves': ['Qg', 'Bxg', 'Bf']}

def test_get_single_transform_board():
    """
    a test function for get_single_transform_board
    """

    single_fen_board1 = ['1rb4r', 'pkPp3p', '1b1P3n', '1Q6', 'N3Pp2', '8', 'P1P3PP', '7K']
    single_transform_board1 = dp.get_single_transform_board(single_fen_board1)
    assert single_transform_board1 == [[{None}, {'type': 'rook', 'side': 'white'}, {'type': 'bishop', 'side': 'white'}, {None}, {None}, {None}, {None}, {'type': 'rook', 'side': 'white'}], [{'type': 'pawn', 'side': 'white'}, {'type': 'king', 'side': 'white'}, {'type': 'pawn', 'side': 'black'}, {'type': 'pawn', 'side': 'white'}, {None}, {None}, {None}, {'type': 'pawn', 'side': 'white'}], [{None}, {'type': 'bishop', 'side': 'white'}, {None}, {'type': 'pawn', 'side': 'black'}, {None}, {None}, {None}, {'type': 'knight', 'side': 'white'}], [{None}, {'type': 'queen', 'side': 'black'}, {None}, {None}, {None}, {None}, {None}, {None}], [{'type': 'knight', 'side': 'black'}, {None}, {None}, {None}, {'type': 'pawn', 'side': 'black'}, {'type': 'pawn', 'side': 'white'}, {None}, {None}], [{None}, {None}, {None}, {None}, {None}, {None}, {None}, {None}], [{'type': 'pawn', 'side': 'black'}, {None}, {'type': 'pawn', 'side': 'black'}, {None}, {None}, {None}, {'type': 'pawn', 'side': 'black'}, {'type': 'pawn', 'side': 'black'}], [{None}, {None}, {None}, {None}, {None}, {None}, {None}, {'type': 'king', 'side': 'black'}]]
    
    single_fen_board10 = ['r2q1b1r', '1pN1n1pp', 'p1n3k1', '4Pb2', '2BP4', '8', 'PPP3PP', 'R1BQ1RK1']
    single_transform_board10 = dp.get_single_transform_board(single_fen_board10)   
    assert single_transform_board10 == [[{'type': 'rook', 'side': 'white'}, {None}, {None}, {'type': 'queen', 'side': 'white'}, {None}, {'type': 'bishop', 'side': 'white'}, {None}, {'type': 'rook', 'side': 'white'}], [{None}, {'type': 'pawn', 'side': 'white'}, {'type': 'knight', 'side': 'black'}, {None}, {'type': 'knight', 'side': 'white'}, {None}, {'type': 'pawn', 'side': 'white'}, {'type': 'pawn', 'side': 'white'}], [{'type': 'pawn', 'side': 'white'}, {None}, {'type': 'knight', 'side': 'white'}, {None}, {None}, {None}, {'type': 'king', 'side': 'white'}, {None}], [{None}, {None}, {None}, {None}, {'type': 'pawn', 'side': 'black'}, {'type': 'bishop', 'side': 'white'}, {None}, {None}], [{None}, {None}, {'type': 'bishop', 'side': 'black'}, {'type': 'pawn', 'side': 'black'}, {None}, {None}, {None}, {None}], [{None}, {None}, {None}, {None}, {None}, {None}, {None}, {None}], [{'type': 'pawn', 'side': 'black'}, {'type': 'pawn', 'side': 'black'}, {'type': 'pawn', 'side': 'black'}, {None}, {None}, {None}, {'type': 'pawn', 'side': 'black'}, {'type': 'pawn', 'side': 'black'}], [{'type': 'rook', 'side': 'black'}, {None}, {'type': 'bishop', 'side': 'black'}, {'type': 'queen', 'side': 'black'}, {None}, {'type': 'rook', 'side': 'black'}, {'type': 'king', 'side': 'black'}, {None}]]


def test_get_aggregate_transform_block():
    """
    a test function for get_aggregate_transform_block
    """
    aggregate_block = []
    aggregate_block.append({'id': 1, 'board': ['1rb4r', 'pkPp3p', '1b1P3n', '1Q6', 'N3Pp2', '8', 'P1P3PP', '7K'], 'moves': ['Qd', 'Ka', 'cxbN#']})

    with patch("get_puzzle.DataProcess.get_single_transform_board") as function_mock:
        function_mock.return_value = [[{None}, {'type': 'rook', 'side': 'white'}, {'type': 'bishop', 'side': 'white'}, {None}, {None}, {None}, {None}, {'type': 'rook', 'side': 'white'}], [{'type': 'pawn', 'side': 'white'}, {'type': 'king', 'side': 'white'}, {'type': 'pawn', 'side': 'black'}, {'type': 'pawn', 'side': 'white'}, {None}, {None}, {None}, {'type': 'pawn', 'side': 'white'}], [{None}, {'type': 'bishop', 'side': 'white'}, {None}, {'type': 'pawn', 'side': 'black'}, {None}, {None}, {None}, {'type': 'knight', 'side': 'white'}], [{None}, {'type': 'queen', 'side': 'black'}, {None}, {None}, {None}, {None}, {None}, {None}], [{'type': 'knight', 'side': 'black'}, {None}, {None}, {None}, {'type': 'pawn', 'side': 'black'}, {'type': 'pawn', 'side': 'white'}, {None}, {None}], [{None}, {None}, {None}, {None}, {None}, {None}, {None}, {None}], [{'type': 'pawn', 'side': 'black'}, {None}, {'type': 'pawn', 'side': 'black'}, {None}, {None}, {None}, {'type': 'pawn', 'side': 'black'}, {'type': 'pawn', 'side': 'black'}], [{None}, {None}, {None}, {None}, {None}, {None}, {None}, {'type': 'king', 'side': 'black'}]]
        aggregate_transform_block = dp.get_aggregate_transform_block(aggregate_block)
        assert aggregate_transform_block[0] == {'id': 1, 'board': [[{None}, {'type': 'rook', 'side': 'white'}, {'type': 'bishop', 'side': 'white'}, {None}, {None}, {None}, {None}, {'type': 'rook', 'side': 'white'}], [{'type': 'pawn', 'side': 'white'}, {'type': 'king', 'side': 'white'}, {'type': 'pawn', 'side': 'black'}, {'type': 'pawn', 'side': 'white'}, {None}, {None}, {None}, {'type': 'pawn', 'side': 'white'}], [{None}, {'type': 'bishop', 'side': 'white'}, {None}, {'type': 'pawn', 'side': 'black'}, {None}, {None}, {None}, {'type': 'knight', 'side': 'white'}], [{None}, {'type': 'queen', 'side': 'black'}, {None}, {None}, {None}, {None}, {None}, {None}], [{'type': 'knight', 'side': 'black'}, {None}, {None}, {None}, {'type': 'pawn', 'side': 'black'}, {'type': 'pawn', 'side': 'white'}, {None}, {None}], [{None}, {None}, {None}, {None}, {None}, {None}, {None}, {None}], [{'type': 'pawn', 'side': 'black'}, {None}, {'type': 'pawn', 'side': 'black'}, {None}, {None}, {None}, {'type': 'pawn', 'side': 'black'}, {'type': 'pawn', 'side': 'black'}], [{None}, {None}, {None}, {None}, {None}, {None}, {None}, {'type': 'king', 'side': 'black'}]], 'moves': ['Qd', 'Ka', 'cxbN#']}
        assert len(aggregate_block) == len(aggregate_transform_block)


def run_all_tests():
    test_get_fen_block_from_web()
    test_get_single_transform_board()
    test_get_aggregate_transform_block()
    print('All tests are passed!')


if __name__ == "__main__":
    run_all_tests()