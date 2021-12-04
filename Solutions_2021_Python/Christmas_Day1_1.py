def ReadFile(FilePath):
    with open(FilePath) as f:
        lines = f.read().splitlines()
    return lines

CurrentDepth = 0

#Returns true if NewDepth is higher than CurrentDepth
def CompareDepth(NewDepth):
    global CurrentDepth
    if NewDepth > CurrentDepth:
        CurrentDepth = NewDepth
        return True
    else:
        CurrentDepth = NewDepth
        return False

def Main():
    AllLines = ReadFile('D:\Tools\input.txt')
    DeepCount = -1
    for Line in AllLines:
        if CompareDepth(int(Line)):
            DeepCount+=1
    print (DeepCount)

Main()