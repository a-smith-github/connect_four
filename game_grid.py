import numpy as np

class GameGrid:
    """Class representing a Connect Four game grid.
    
        The grid is stored in a numpy array using the values
            0 for empty
            1 for player
            2 for computer

    """
    
    def __init__(self):
        self.rows = 6
        self.columns = 7
        #Stored column-major for convenience
        self.grid = np.zeros( (self.columns, self.rows) ).astype(int)

    def display(self):        
        """Display the current state of the Connect Four grid."""
        
        #Transpose Grid and print to screen 
        print("GAME STATE")
        print(np.flip( np.transpose(self.grid),axis=0) )

    def convert_human_to_stored_column_number(self, play):
        
        column = int(play)-1
        return column
    
    def add_counter(self, player, column):
        row = np.argmin(self.grid[column])
        if row < self.rows:
            self.grid[column,row] = player

    def validate_input(self, play):
        try:
            integer = self.convert_human_to_stored_column_number(play)
        except:
            print("Not an integer")
            return False    

        return 0 <= integer < self.columns and np.count_nonzero(self.grid[integer]) < self.rows

    def human_play(self):

        valid_input = False
        while not valid_input:
            play = input(f"Pick a column (from 1 to {self.columns}):\n")
            valid_input = self.validate_input(play)
            
            if not valid_input:
                print(f"Not a valid integer. Please pick an integer between 1 and {self.columns}")

        self.add_counter(1, self.convert_human_to_stored_column_number(play))

    
    def computer_play(self):
        valid_input = False
        while not valid_input:
            play = np.random.randint(1, self.columns)
            valid_input = self.validate_input(play)

        self.add_counter(2, self.convert_human_to_stored_column_number(play))

    def check_stalemate(self):
        column = np.linspace(1,self.columns,self.columns).astype(int)-1
        full_columns = np.count_nonzero((self.grid[column,:]), axis=1) == 6

        if np.sum(full_columns) == self.columns:
            return True
        else:
            return False



game_board = GameGrid()
game_board.display()

session = True 
while session:

    game_board.human_play()
    game_board.computer_play()
    print(game_board.display())

    if game_board.check_stalemate():
        print("Game is a draw")
        session = False



