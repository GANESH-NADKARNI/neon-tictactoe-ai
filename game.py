import pygame
import sys
import random
from agent import MasterAgent

WIDTH, HEIGHT = 600, 600
BG_COLOR = (30, 10, 45)
GRID_COLOR = (80, 20, 100)
NEON_BLUE = (0, 255, 255)
NEON_RED = (255, 0, 100)
LINE_WIDTH = 10
CELL_SIZE = WIDTH // 3

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Neon Tic-Tac-Toe Unbeatable")
font = pygame.font.SysFont("arial", 40)

ai_agent = MasterAgent(ai_symbol='O', user_symbol='X')

class Game:
    def __init__(self):
        self.board = [' '] * 9
        self.running = True
        self.game_over = False
        self.winner = None
        
        self.user_symbol = random.choice(['X', 'O'])
        self.ai_symbol = 'O' if self.user_symbol == 'X' else 'X'
        self.turn = 'X' if random.choice([0, 1]) == 0 else 'O'
        
        print(f"You are: {self.user_symbol}")

    def draw_grid(self):
        for i in range(1, 3):
            pygame.draw.line(screen, GRID_COLOR, (0, i * CELL_SIZE), (WIDTH, i * CELL_SIZE), LINE_WIDTH)
            pygame.draw.line(screen, GRID_COLOR, (i * CELL_SIZE, 0), (i * CELL_SIZE, HEIGHT), LINE_WIDTH)

    def draw_neon_x(self, x, y):
        center_x, center_y = x * CELL_SIZE + CELL_SIZE // 2, y * CELL_SIZE + CELL_SIZE // 2
        offset = 60
        for width, alpha in [(20, 50), (12, 100), (4, 255)]:
            s = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
            color = (*NEON_BLUE, alpha)
            pygame.draw.line(s, color, (center_x - offset, center_y - offset), (center_x + offset, center_y + offset), width)
            pygame.draw.line(s, color, (center_x + offset, center_y - offset), (center_x - offset, center_y + offset), width)
            screen.blit(s, (0,0))

    def draw_neon_o(self, x, y):
        center_x, center_y = x * CELL_SIZE + CELL_SIZE // 2, y * CELL_SIZE + CELL_SIZE // 2
        radius = 70
        for width, alpha in [(20, 50), (12, 100), (4, 255)]:
            s = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
            color = (*NEON_RED, alpha)
            pygame.draw.circle(s, color, (center_x, center_y), radius, width)
            screen.blit(s, (0,0))

    def draw_board(self):
        screen.fill(BG_COLOR)
        self.draw_grid()
        for i in range(9):
            x, y = i % 3, i // 3
            if self.board[i] == 'X':
                self.draw_neon_x(x, y)
            elif self.board[i] == 'O':
                self.draw_neon_o(x, y)
        pygame.display.flip()

    def check_win(self):
        win_patterns = [
            [0,1,2], [3,4,5], [6,7,8], 
            [0,3,6], [1,4,7], [2,5,8], 
            [0,4,8], [2,4,6]
        ]
        for p in win_patterns:
            if self.board[p[0]] == self.board[p[1]] == self.board[p[2]] != ' ':
                self.winner = self.board[p[0]]
                self.game_over = True
                return
        if ' ' not in self.board:
            self.game_over = True

    def ai_move(self):
        if self.game_over: return
        
        ai_agent.ai = self.ai_symbol
        ai_agent.human = self.user_symbol
        
        move = ai_agent.choose_action(self.board)
        
        self.board[move] = self.ai_symbol
        self.turn = self.user_symbol
        self.check_win()

    def run(self):
        while self.running:
            self.draw_board()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                
                if event.type == pygame.MOUSEBUTTONDOWN and not self.game_over:
                    if self.turn == self.user_symbol:
                        x, y = event.pos
                        col, row = x // CELL_SIZE, y // CELL_SIZE
                        index = row * 3 + col
                        if self.board[index] == ' ':
                            self.board[index] = self.user_symbol
                            self.turn = self.ai_symbol
                            self.check_win()

            if self.turn == self.ai_symbol and not self.game_over:
                pygame.time.wait(1000)
                self.ai_move()

            if self.game_over:
                pygame.time.wait(1000)
                print(f"Game Over! Winner: {self.winner}")
                self.running = False

        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    Game().run()