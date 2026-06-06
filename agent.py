import math

class MasterAgent:
    def __init__(self, ai_symbol='O', user_symbol='X'):
        self.ai = ai_symbol
        self.human = user_symbol

    def check_winner(self, board):
        win_patterns = [
            [0,1,2], [3,4,5], [6,7,8],
            [0,3,6], [1,4,7], [2,5,8],
            [0,4,8], [2,4,6]
        ]
        
        for p in win_patterns:
            if board[p[0]] == board[p[1]] == board[p[2]] and board[p[0]] != ' ':
                return board[p[0]]
        
        if ' ' not in board:
            return 'Draw'
        
        return None

    def minimax(self, board, depth, is_maximizing):
        result = self.check_winner(board)
        if result == self.ai: return 10 - depth
        if result == self.human: return -10 + depth
        if result == 'Draw': return 0

        if is_maximizing:
            best_score = -math.inf
            for i in range(9):
                if board[i] == ' ':
                    board[i] = self.ai
                    score = self.minimax(board, depth + 1, False)
                    board[i] = ' '
                    best_score = max(score, best_score)
            return best_score
        else:
            best_score = math.inf
            for i in range(9):
                if board[i] == ' ':
                    board[i] = self.human
                    score = self.minimax(board, depth + 1, True)
                    board[i] = ' '
                    best_score = min(score, best_score)
            return best_score

    def choose_action(self, board):
        if board.count(' ') == 9:
            return 4
            
        best_score = -math.inf
        best_move = -1
        
        for i in range(9):
            if board[i] == ' ':
                board[i] = self.ai
                score = self.minimax(board, 0, False)
                board[i] = ' '
                
                if score > best_score:
                    best_score = score
                    best_move = i
                    
        return best_move