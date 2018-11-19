import chess.uci
import chess
from flask import Flask
from config import STOCKFISH_PATH

# Initialize board and engine state
app = Flask(__name__)
board = chess.Board()
engine = chess.uci.popen_engine(STOCKFISH_PATH)

import serverapp.api.routes
