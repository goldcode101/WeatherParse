#Author: Chris Lenz
#Date: 3/8/2015
#To use: pass in the full absolute path to the file containing weather info to be parsed.
import sys

def LoadData(fileLines, headers):
    print('Loading data...')
    print('There are ' + str(len(fileLines)) + ' lines to be read.')

    arrayOfDays = []
    for ln in fileLines:
        if(ln != fileLines[0]):
            splitList = ln.split(',', len(headers))
            day = []
            for split in splitList:
                day.append(split)
            arrayOfDays.append(day)
    print('Done!')

    return arrayOfDays

def main(filename):
    file = open(filename, 'r')
    fileLines = file.read().split('\n')
    lstHeader = fileLines[0].split(',')
    print('There are ' + str(len(lstHeader)) + ' headers.')

    wxData = LoadData(fileLines, lstHeader)
    invalidInput = True
    while invalidInput:
        queryType = input('Select type of query: (D)ay, (S)ingle,')
        if(queryType == 'd' or queryType == "D"):
            invalidInput = False
            #Do more day query stuff
        elif(queryType == 's' or queryType == 'S'):
            invalidInput = False
            #Do more single query stuff
        else:
            invalidInput = True



if __name__ == '__main__':
    main(sys.argv[1])

