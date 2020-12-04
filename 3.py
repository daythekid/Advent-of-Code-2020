arr = []

while True:
    string = input()
    if string == "-1":
        break
    arr.append(list(string))

#[down,across]

trees = 0
startX = 0
startY = 0
while True:
    try:
        if (startX>30):
            startX -=31
        if arr[startY][startX]=="#":
            trees+=1
        startX+=1
        startY+=2
    except:
        print(trees)
        break

#Part 2:
#66*200*76*81*46 = 3737923200



