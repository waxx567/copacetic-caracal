import pygame
import random
import sys

# Constants
TILE_SIZE = 100  # Size of each tile
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
MAX_ROWS_COLS = 9  # Maximum rows and columns allowed
MAX_TRIALS = 40  # Maximum number of trials allowed

class MemoryGame:
    def __init__(self, grid_size, num_pairs):
        # Initialize game attributes
        self.grid_size = grid_size  # Store grid size as (rows, columns)
        self.window_size = (TILE_SIZE * grid_size[1], TILE_SIZE * grid_size[0])  # Calculate window size
        self.tiles_revealed = [[False] * grid_size[1] for _ in range(grid_size[0])]  # Track revealed tiles
        self.tile_colors = [[WHITE] * grid_size[1] for _ in range(grid_size[0])]  # Tile colors
        self.first_selection = None  # Store first tile selection
        self.second_selection = None  # Store second tile selection
        self.trials = 0  # Count of trials taken
        self.matched_pairs = 0  # Count of matched pairs
        
        pygame.init()  # Initialize Pygame
        self.window = pygame.display.set_mode(self.window_size)  # Create game window
        pygame.display.set_caption("Memory Matching Game")  # Set window title
        self.numbers = self.create_numbers(num_pairs)  # Generate number pairs
        
        self.clock = pygame.time.Clock()  # Control game frame rate
        self.font = pygame.font.Font(None, 48)  # Set font for displaying text
        self.run_game()  # Start the main game loop

    def create_numbers(self, num_pairs):
        # Create a shuffled list of numbers for the tiles
        numbers = list(range(1, num_pairs + 1)) * 2  # Create pairs
        random.shuffle(numbers)  # Shuffle the list
        return numbers  # Return shuffled numbers

    def draw_board(self):
        # Draw the game board
        self.window.fill(BLACK)  # Fill background with black
        for row in range(self.grid_size[0]):
            for col in range(self.grid_size[1]):
                rect = pygame.Rect(col * TILE_SIZE, row * TILE_SIZE, TILE_SIZE, TILE_SIZE)  # Define tile rectangle
                pygame.draw.rect(self.window, self.tile_colors[row][col], rect)  # Draw tile
                pygame.draw.rect(self.window, BLACK, rect, 2)  # Draw tile border

                # Display the number if the tile is revealed
                if self.tiles_revealed[row][col]:
                    text = self.font.render(str(self.numbers[row * self.grid_size[1] + col]), True, BLACK)
                    self.window.blit(text, text.get_rect(center=rect.center))  # Center the text in the tile

    def check_match(self):
        # Check if the two selected tiles match
        if self.first_selection and self.second_selection:
            first_row, first_col = self.first_selection
            second_row, second_col = self.second_selection

            # If numbers match
            if (self.numbers[first_row * self.grid_size[1] + first_col] ==
                self.numbers[second_row * self.grid_size[1] + second_col]):
                self.matched_pairs += 1  # Increment matched pairs count
                self.tile_colors[first_row][first_col] = GREEN  # Change color to green for matched tiles
                self.tile_colors[second_row][second_col] = GREEN
            else:
                # Change color to red for mismatched tiles
                self.tile_colors[first_row][first_col] = RED
                self.tile_colors[second_row][second_col] = RED
                self.draw_board()  # Update board to show red
                pygame.display.flip()  # Refresh the display
                pygame.time.wait(1000)  # Wait for a second to show the red color

                # Reset revealed state for mismatched tiles
                self.tiles_revealed[first_row][first_col] = False
                self.tiles_revealed[second_row][second_col] = False
                self.tile_colors[first_row][first_col] = WHITE  # Reset color to white
                self.tile_colors[second_row][second_col] = WHITE
            
            # Reset selections for the next turn
            self.first_selection = None
            self.second_selection = None

    def run_game(self):
        # Main game loop
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # Check for quit event
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    # Get mouse position and calculate selected tile
                    pos = pygame.mouse.get_pos()
                    col = pos[0] // TILE_SIZE
                    row = pos[1] // TILE_SIZE
                    
                    # Ensure the selected tile is valid
                    if 0 <= row < self.grid_size[0] and 0 <= col < self.grid_size[1]:
                        if not self.tiles_revealed[row][col]:  # If tile not revealed
                            self.tiles_revealed[row][col] = True  # Mark tile as revealed
                            self.tile_colors[row][col] = BLUE  # Change color for selected tile
                            
                            if self.first_selection is None:  # First selection
                                self.first_selection = (row, col)
                            elif self.second_selection is None:  # Second selection
                                self.second_selection = (row, col)
                                self.trials += 1  # Increment trial count
                                self.check_match()  # Check for match

            self.draw_board()  # Draw the current state of the board
            pygame.display.flip()  # Refresh the display

            # Check for win condition
            if self.matched_pairs == self.grid_size[0] * self.grid_size[1] // 2:
                self.show_winner()

            # Check for maximum trials
            if self.trials >= MAX_TRIALS:
                self.show_game_over()  # Show game over if maximum trials reached

            self.clock.tick(30)  # Limit frame rate to 30 FPS

    def show_winner(self):
        # Display win message
        self.window.fill(WHITE)  # Fill background with white
        text = self.font.render("You've matched all pairs!", True, BLACK)  # Create win message text
        self.window.blit(text, text.get_rect(center=(self.window_size[0] // 2, self.window_size[1] // 2)))  # Center the text
        pygame.display.flip()  # Refresh the display
        pygame.time.wait(3000)  # Wait for 3 seconds before resetting
        self.reset_game()  # Reset game state

    def show_game_over(self):
        # Display game over message
        self.window.fill(WHITE)  # Fill background with white
        text = self.font.render("Game Over! Too many trials!", True, BLACK)  # Create game over message
        self.window.blit(text, text.get_rect(center=(self.window_size[0] // 2, self.window_size[1] // 2)))  # Center the text
        pygame.display.flip()  # Refresh the display
        pygame.time.wait(3000)  # Wait for 3 seconds before resetting
        self.reset_game()  # Reset game state

    def reset_game(self):
        # Reset game state for a new game
        self.first_selection = None
        self.second_selection = None
        self.trials = 0
        self.matched_pairs = 0
        self.tiles_revealed = [[False] * self.grid_size[1] for _ in range(self.grid_size[0])]  # Reset revealed state
        self.tile_colors = [[WHITE] * self.grid_size[1] for _ in range(self.grid_size[0])]  # Reset tile colors

def get_grid_size_and_pairs():
    # Get grid size and number of pairs from the user
    while True:
        try:
            rows = int(input("Enter number of rows (at least 2, max 9): "))  # Get number of rows
            cols = int(input("Enter number of columns (at least 2, max 9): "))  # Get number of columns
            # Validate input
            if (rows < 2 or cols < 2 or rows > MAX_ROWS_COLS or cols > MAX_ROWS_COLS):
                print("Both rows and columns should be between 2 and 9.")
                continue
            if (rows % 2 != 0 and cols % 2 != 0):
                print("At least one of the numbers must be even.")
                continue
            num_pairs = (rows * cols) // 2  # Calculate number of pairs
            return (rows, cols), num_pairs  # Return grid size and number of pairs
        except ValueError:
            print("Please enter valid integers.")  # Handle invalid input

if __name__ == "__main__":
    grid_size, num_pairs = get_grid_size_and_pairs()  # Get user input for grid size and pairs
    MemoryGame(grid_size, num_pairs)  # Start the game
