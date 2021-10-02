from Piece import Piece
from Board import Board

board = Board()
for i in range(81):
    board.addPiece()
    print(board)



# Keyboard module in Python
# pip install keyboard
#import keyboard
##while board.countNonZero() < board.m*board.n+1:
##    other = board.clone()
##    other.rightMove()
##    if ((board.countNonZero() == board.m*board.n) and 
##        (board.isEqual(board.rightMove())) and 
##        (board.isEqual(board.upMove())) and 
##        (board.isEqual(board.leftMove())) and 
##        (board.isEqual(board.downMove()))
##    ):
##        break
##    else:
##        keyboard.add_hotkey('right', lambda: board.rightMove())
##        keyboard.add_hotkey('up', lambda: board.upMove())
##        keyboard.add_hotkey('left', lambda: board.leftMove())
##        keyboard.add_hotkey('down', lambda: board.downMove())
##        print('Push the arrows to play')
##        keyboard.wait()
