from src.config.config import (COMMANDS, ARGUMENTS)

from src.backend.data import Data
from src.backend.hash import hash_sha256
from src.backend.scan import scan

import sys
import os

class Interpreter:
    def __new__(cls, optlist, args):
        if output := cls._exec_args(args):
            return output
        
        return super().__new__(cls)
    
    
    def __init__(self, optlist, args):
        self.filter = None
        self.type = None
        self.path = None

        self._exec_opts(optlist)
        
    def __str__(self):
        return f"{self.filter}, {self.type}, {self.path}"
    
    def _exec_opts(self, optlist):
        for opt, arg in optlist:
            setattr(self, opt.strip("--"), arg)
        
    @staticmethod
    def _exec_args(args):
        invalid_args = set(args) - set(ARGUMENTS)
        
        if invalid_args:
            arg = next(arg for arg in args if arg in invalid_args)
            return f'"{arg}": Not in specified arguments list.'
        
        if "clear" in args:
            os.system("cls" if os.name == "nt" else "clear")
        
        if "exit" in args or "quit" in args:
            sys.exit()
            quit()
            
        return None