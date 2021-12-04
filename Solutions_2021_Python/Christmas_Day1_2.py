def ReadFile(FilePath):
    with open(FilePath) as f:
        lines = f.read().splitlines()
    return lines

OldSum = 0
CurrentSum = 0
TempSum = 0


def AddSumAndCompare(CurrentDepth):
    global OldSum
    global CurrentSum
    global TempSum
    
    IsBigger = False
    CurrentSum+=CurrentDepth
    TempSum+=CurrentDepth

    if(CurrentSum > OldSum):
        IsBigger = True
    
    OldSum = CurrentSum
    CurrentSum = TempSum
    TempSum = CurrentDepth

    return IsBigger

def Main():
    AllLines = ReadFile('D:\Tools\input.txt')
    Count = -2
    for Line in AllLines:
        if AddSumAndCompare(int(Line)):
            Count+=1
    print(Count)

Main()