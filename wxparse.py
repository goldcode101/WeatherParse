#Author: Chris Lenz
#Date: 3/8/2015
#To use: pass in the full absolute path to the file containing weather info to be parsed.
import sys

def main(filename):
    fileLines = open(filename, 'r').read().split('\n')
    lstHeader = fileLines[0].split(',')
    print 'There are ' + str(len(lstHeader)) + ' headers.'



if __name__ == '__main__':
    main(sys.argv[1])

