import getopt
import sys
import os


class Interface:
    def __init__(self):
        pass

    def run(self):
        while True:
            args = input("> ").split()
            optlist, args = getopt.getopt(args, "")

            print(optlist, args)
