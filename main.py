from board import Board
from pathlib import Path 

file_name= str(Path(__file__).parent / "assets" / "config_file.json")


board = Board(file_name)
