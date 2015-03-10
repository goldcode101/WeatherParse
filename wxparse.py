#Author: Chris Lenz
#Date: 3/8/2015
#To use: pass in the full absolute path to the file containing weather info to be parsed.
import sys

def LoadData(fileLines, headers):
    print 'Loading data...'
    print 'There are ' + str(len(fileLines)) + ' lines to be read.'

    for ln in fileLines:
        if(ln != fileLines[0]):
            splitList = ln.split(',', len(headers))
            for split in splitList:
                day = []
                day.append(split)
    print len(day)
    print 'Done!'


def main(filename):
    file = open(filename, 'r')
    fileLines = file.read().split('\n')
    lstHeader = fileLines[0].split(',')
    print 'There are ' + str(len(lstHeader)) + ' headers.'

    LoadData(fileLines, lstHeader)


if __name__ == '__main__':
    main(sys.argv[1])

