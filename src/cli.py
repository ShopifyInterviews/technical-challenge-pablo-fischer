import functools

import cmd2
from tabulate import tabulate
from cmd2 import COMMAND_NAME

class RobotCLI(cmd2.Cmd):
    
    def __init__(self) -> None:
        self.panel = []
        self.direction = "right"
        self.current_position_x = 0
        self.current_position_y = 0
        super().__init__()
        

    start_parser = cmd2.Cmd2ArgumentParser(
        description='Start or initialize our panel',
    )
    start_parser.add_argument('columns', type=int, help='Number of columns the panel should have')
    start_parser.add_argument('rows', type=int, help='Number of rows the panel should have')
    
    @cmd2.with_argparser(start_parser)
    def do_start(self, opts) -> None:
        """Start command."""
        
        for column in range(0, opts.columns):
            self.panel.append([0] * opts.rows)
        self.poutput('Panel initialized, please use right, left, up or down')    

    def do_right(self, _) -> None:
        """Right command."""
        if self.panel is None:
            self.poutput('Panel not initialized. Use "start" command first.')
            return
        self.direction = "right"
        self.poutput('Right')

    def do_left(self, _) -> None:
        """Left command."""
        if self.panel is None:
            self.poutput('Panel not initialized. Use "start" command first.')
            return        
        self.direction = "left"
        self.poutput('Left')
        
    def do_up(self, _) -> None:
        """Up command."""
        if self.panel is None:
            self.poutput('Panel not initialized. Use "start" command first.')
            return        
        self.direction = "up"
        self.poutput('Up')

    def do_down(self, _) -> None:
        """Down command."""
        if self.panel is None:
            self.poutput('Panel not initialized. Use "start" command first.')
            return
        self.direction = "down"
        self.poutput('Down')
        
    move_pos_parser = cmd2.Cmd2ArgumentParser(
        description='Move the robot in the specified direction in number of N moves',
    )
    move_pos_parser.add_argument('steps', type=int, help='Number of steps to move the robot')
    @cmd2.with_argparser(move_pos_parser)
    def do_move(self, opts) -> None:
        """Down command."""
        if self.panel is None:
            self.poutput('Panel not initialized. Use "start" command first.')
            return
        
        for i in range(opts.steps):
            if self.direction == "right":
                if self.current_position_x == len(self.panel) - 1:
                    self.poutput('Cannot move right, already at the rightmost position.')
                    break
                self.current_position_x += 1
            elif self.direction == "left":
                if self.current_position_x == 0:
                    self.poutput('Cannot move left, already at the leftmost position.') 
                    break
                self.current_position_x -= 1
            elif self.direction == "up":
                if self.current_position_y == 0:
                    self.poutput('Cannot move up, already at the topmost position.')
                    break
                self.current_position_y -= 1
            elif self.direction == "down":
                if self.current_position_y == len(self.panel[0]) - 1:
                    self.poutput('Cannot move down, already at the bottommost position.')
                    break
                self.current_position_y += 1
        
        self.print_grid()
        # Print current position
        self.poutput(f'Moved to position {self.current_position_x}, {self.current_position_y}')
        
    def print_grid(self):
        grid = self.panel
        for x in range(0, len(grid)):
            for y in range(0, len(grid[x])):
                if x == self.current_position_x and y == self.current_position_y:
                    grid[x][y] = 'X'
                else:
                    grid[x][y] = 'O'
        self.poutput(tabulate(grid, tablefmt='grid'))
                
        

if __name__ == '__main__':
    import sys

    c = RobotCLI()
    sys.exit(c.cmdloop())
