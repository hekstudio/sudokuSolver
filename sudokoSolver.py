import ast

def initSudokuList(dataList,value):
    for i in range(81):
            dataList.append(value)

def printSudokuList(list):
    print ('')
    for i in range(81):
        for j in range(4-len(str(list[i]))):
            print (' ',end='')
        if (list[i]!=46):
            print (str(list[i]).strip(),end='')
        else:
            print (' ',end='')
        if ((i+1)%3 == 0):
            print(' ',end='')
        if ((i+1)%9 == 0):
            print ('')
        if ((i+1)%27 == 0):
            print ('')

def solveSudokuList(dataList, fixList):
    for i in range(81):
        if(dataList[i] < 10):
            eliminate(dataList,i)

def eliminate(dataList, index):
    listToDelete = list()
    for i in range(81):
        listToDelete.append(0)
    start = int(i%9/3)*3
    for j in range(start,start+3):
        # Determine which block to delete
        listToDelete[j] = 1
        listToDelete[j+9] = 1
        listToDelete[j+18] = 1
    start = int(index/9)*9
    for j in range(start,start+9):
        # Determine which row to delete
        listToDelete[j] = 1
    start = index%9
    for j in range(0,9):
        # Determine which column to delete
        listToDelete[start+j*9] = 1
    for i in range(0,81):
        if( listToDelete[i] == 1 and dataList[i] > 9):
            dataList[i] = dataList[i] - dataList[index]

def check(dataList, fixList):
    return
            

def loadChallenge(file,list,fixList):
    f = open(file,'r')
    for line in f:
        x,y,value = line.split(',')
        x = int(x)
        y = int(y)
        value = int(value)
        list[y*9+x] = value
        fixList[y*9+x] = 1
    f.close()

# ----------------------------------------------
#   Main Program Starts
# ----------------------------------------------
# Load Prime Table
f = open("primeList.txt","r")
primeTable = ast.literal_eval(f.read())
print (primeTable[1])
f.close()

sList = list()
fixList = list()

initSudokuList(sList,45)
initSudokuList(fixList,0)

loadChallenge("problem1.txt",sList,fixList)
printSudokuList(sList)

#print (matrix)
solveSudokuList(sList, primeTable)
printSudokuList(sList)
solveSudokuList(sList, primeTable)
printSudokuList(sList)
solveSudokuList(sList, primeTable)
printSudokuList(sList)
#eliminate(sList,8)

printSudokuList(sList)



