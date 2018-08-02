import ast

def initSudokuList(dataList,value):
    for i in range(81):
            dataList.append(value)

def printSudokuList(list):
    print ('')
    for i in range(81):
        for j in range(3-len(str(list[i]).strip())):
            print (' ',end='')
        if (list[i] != 46):
            print (str(list[i]).strip()+' ',end='')
        else:
            print ('-',end='')
        if ((i+1)%3 == 0):
            print(' ',end='')
        if ((i+1)%9 == 0):
            print ('')
        if ((i+1)%27 == 0):
            print ('')
    print ('----------------------------------------')

<<<<<<< HEAD
def solveSudokuList(dataList, fixList, primeList):
    for i in range(81):
        if(dataList[i] < 10):
            eliminate(dataList,i, primeList)

def eliminate(dataList, index, primeList):
=======
def printList(list):
    for i in range(81):
        print (str(i)+"  "+str(list[i]))

def solveSudokuList(dataList, fixList):
    for i in range(1):
        if(fixList[i] == 1):
            eliminate(dataList,i,fixList)

def eliminate(dataList, index, fixList):
>>>>>>> f1d94a4780b514205f80b73866b86761fa00e91a
    listToDelete = list()
    for i in range(81):
        listToDelete.append(0)
    start = int(index%9/3)*3+int(index/27)*27
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
<<<<<<< HEAD
    for i in range(0,81):
        if( listToDelete[i] == 1 and dataList[i] > 9):
            if(dataList[i] % primeList[dataList[index]] == 0):
                dataList[i] = dataList[i] / primeList[dataList[index]]

def check(dataList, fixList):
    for i in range(0,8,3):
        for j in range(0,72,27):
            # Looping through 1st element of each block
            tempList = list()
            for i1 in range(i,i+3):
                for j1 in range(j,j+27,9):
                    # Looping through every elements in one block
                    # Add indexes in a list
                    tempList.append(i1+j1)
            # Check validity of each block
            #for p in range(10):

=======
    printSudokuList(listToDelete)
    test1 = 0
    #dataList[1].pop(8-1)
    for i in range(81):
        if ( listToDelete[i] == 1 and fixList[i] != 1):
            print(str(i)+" "+str(dataList[index])+str(dataList[i]))
            if (dataList[index] in dataList[i]):
                test1 = test1 + 1
                number = dataList[index]
                dataList[i].remove(number)
    print("TEST1 "+str(test1))

def check(dataList, fixList):
    tempList = list()
    tempFix = list()
    # Go through all rows
    for i in range(0,73,9):
        tempList.clear()
        tempFix.clear()
        # Go through each row
        for j in range(i,i+9):
            if (fixList(j) == 1):
                tempFix.append(j)
            else:
                tempList.append(j)
    return
            
>>>>>>> f1d94a4780b514205f80b73866b86761fa00e91a

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

<<<<<<< HEAD
initSudokuList(sList,223092870)
=======
initSudokuList(sList,[1,2,3,4,5,6,7,8,9])
>>>>>>> f1d94a4780b514205f80b73866b86761fa00e91a
initSudokuList(fixList,0)


printList(sList)
loadChallenge("problem1.txt",sList,fixList)
printSudokuList(fixList)
printList(sList)

#print (matrix)
<<<<<<< HEAD
solveSudokuList(sList, fixList, primeTable)
printSudokuList(sList)
check(sList,fixList)
=======
solveSudokuList(sList,fixList)
printList(sList)
#printSudokuList(sList)
>>>>>>> f1d94a4780b514205f80b73866b86761fa00e91a
#solveSudokuList(sList, primeTable)
#printSudokuList(sList)
#solveSudokuList(sList, primeTable)
#printSudokuList(sList)
#eliminate(sList,8)

<<<<<<< HEAD

=======
#printSudokuList(sList)
>>>>>>> f1d94a4780b514205f80b73866b86761fa00e91a



