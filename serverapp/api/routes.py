"""routes.py

A barebones module to play a game of chess with
an AI with move validation.
"""

from flask import request, jsonify, abort

from serverapp import app, board, engine
from serverapp.api.ai import execute_ai_move


@app.route("/start/")
def start():
    """start

    Start the game engine.
    Return a No Content HTTP response

    :return tuple
    """

    # Start UCI engine Stockfish
    engine.uci()

    # Return a No Content response
    return '', 204


@app.route("/move/")
def execute_player_move():
    """move_player_piece

    Move piece on board and performs ai move if
    human move is valid

    :param uci_move: string representation of player's move
    :return: json object
    """

    uci_move = request.args.get("move")
    if uci_move is None:
        abort(400, "No move data provided as argument")

    try:
        board.push_uci(uci_move)
        ai_move = execute_ai_move(engine, board)
        return jsonify(success=True, ai_move=ai_move, player_move=uci_move)
    except ValueError:
        return jsonify(success=False, ai_move=None)


@app.route("/print/")
def board_to_str():
    """board_to_str

    Return the string representation of the board.

    :return str
    """

    return jsonify(string=str(board))
