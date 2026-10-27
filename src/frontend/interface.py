from src.config.config import COMMANDS
from src.config.colours import Colours

from src.backend.interpreter import Interpreter

import getopt

class Interface:
    def run(self):
        while True:
            user_input = input("> ").split()
            
            try:
                optlist, args = getopt.getopt(args=user_input, shortopts="t:f:p:", longopts=list(COMMANDS))
                
                output = Interpreter(optlist, args)
                
                print(output)
            except getopt.GetoptError as err:
                print(str(err))