"""ai.py

Functions related to Chess AI.
"""

def execute_ai_move(engine, board):
    """execute_ai_move

    Determine best AI move and perform move.
    Returns UCI representation of string.

    :return str
    """

    engine.position(board)
    ai_move = engine.go(movetime=2000).bestmove.uci()
    board.push_uci(ai_move)

    return ai_move
