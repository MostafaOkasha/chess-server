"""play_ai.py

A basic Python script for demo purposes of Flask
server and integration with chess engine AI.
"""

import requests
import json

# Solution to import configuration variables from config.py
import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0,parent_dir)
import config

ENDPOINTS = {
    "start": "/start/",
    "print": "/print/",
    "move": "/move/"
}


def create_request(uri, endpoint, **kwargs):
    """create_request

    """

    query_parameters = "&".join([f"{key}={val}" for key, val in kwargs.items()])
    # Prepend ? to query parameters if query parameters exist
    if query_parameters:
        query_parameters = "?" + query_parameters

    return f"{uri}{endpoint}{query_parameters}"


def start_game(uri):
    """start_game

    """

    url = create_request(uri, ENDPOINTS["start"])
    requests.get(url)


def prettify_board(board):
    """prettify_board


    """

    top = f"  a b c d e f g h \n  {'-'*15}\n"
    bottom = f"\n  {'-' * 15}\n  a b c d e f g h"

    numbered_board = [f"{row_num}|{row}|{row_num}" for row, row_num
                      in zip(board.split("\n"), range(8, 0, -1))]

    return top + "\n".join(numbered_board) + bottom


def request_player_move(uri):
    """request_player_move

    """

    # Request player move from server
    player_move = input("\nWhat move would you like to "
                        "make in UCI notation (ex. e2e4)?: ")

    move_url = create_request(uri, ENDPOINTS["move"], move=player_move)
    move_resp = requests.get(move_url)

    return move_resp.text


def play_game(uri):
    """play_game

    """

    while True:
        # Request board state
        print_url = create_request(uri, ENDPOINTS["print"])
        raw_resp = requests.get(print_url)
        raw_board_state = json.loads(raw_resp.text)["string"]

        # Pretty print board
        pretty_board = prettify_board(raw_board_state)
        print(pretty_board)

        # Request player move from server
        moves = json.loads(request_player_move(uri))

        # Request move until move is valid
        while not moves["success"]:
            print("Sorry! Invalid move.", end="")
            moves = json.loads(request_player_move(uri))

        print(f"Your move was {moves['player_move']}. "
              f"The AI move was {moves['ai_move']}\n")


if __name__ == "__main__":
    HOST = config.HOST or "127.0.0.1"
    PORT = config.PORT or 5000

    uri = f"http://{HOST}:{PORT}"
    start_game(uri)
    play_game(uri)
