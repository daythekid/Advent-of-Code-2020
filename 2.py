# trues = 0

# while True:
#     stringToParse = input()
#     if (stringToParse=="-1"):
#         break
    
#     arr = stringToParse.split()
#     splitted = arr[0].split("-")
#     minimum = int(splitted[0])
#     maximum = int(splitted[1])
#     charWanted = arr[1][0]
#     num = arr[2].count(charWanted)

#     if minimum <= num <= maximum:
#         trues+=1

# print(trues)


trues = 0

while True:
    stringToParse = input()
    if (stringToParse=="-1"):
        break
    
    arr = stringToParse.split()
    splitted = arr[0].split("-")
    minimum = int(splitted[0])
    maximum = int(splitted[1])
    charWanted = arr[1][0]
    first = False
    second = False

    if arr[2][minimum-1] == charWanted:
        first = True
    if arr[2][maximum-1] == charWanted:
        second = True

    if (not first) == second:
        trues+=1

print(trues)