def __init__(self):
    self.board = [
            ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
            ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"],
            ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"]]
    self.moveFunctions = {'p': self.getPawnMoves, 'R': self.getRookMoves, 'N': self.getKnightMoves,
                            'B': self.getBishopMoves, 'Q': self.getQueenMoves, 'K': self.getKingMoves}
    self.whiteToMove = True,
    self.moveLog = []
    self.whiteKingLocation = (7, 4)
    self.blackKingLocation = (0, 4)
    self.checkMate = False
    self.staleMate = False

def makeMove(self, move):
    self.board[move.startRow][move.startCol] = "--"
    self.board[move.endRow][move.endCol] = move.pieceMoved
    self.moveLog.append(move)
    self.whiteToMove = not self.whiteToMove
    if move.pieceMoved == "wK":
            self.whiteKingLocation = (move.endRow, move.endCol)
    elif move.pieceMoved == "bK":
            self.blackKingLocation = (move.endRow, move.endCol)

    if move.isPawnPromotion:
            self.board[move.endRow][move.endCol] = move.pieceMoved[0] + "Q"


def undoMove(self):
    if len(self.moveLog) != 0:
            move = self.moveLog.pop()
            self.board[move.startRow][move.startCol] = move.pieceMoved
            self.board[move.endRow][move.endCol] = move.pieceCaptured
            self.whiteToMove = not self.whiteToMove
            if move.pieceMoved == "wK":
                    self.whiteKingLocation = (move.startRow, move.startCol)
            if move.pieceMoved == "bK":
                    self.blackKingLocation = (move.startRow, move.startCol)