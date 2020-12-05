# maximum = 0
# while True:
#     strings = input()
#     if strings=="-1":
#         break

#     rangeStart = 0
#     rangeEnd = 127

#     for i in strings[0:7]:
#         diff = (rangeEnd-rangeStart+1)/2
#         if i =="F":
#             rangeEnd-=diff
#         if i=="B":
#             rangeStart+=diff

#     colStart = 0
#     colEnd = 7

#     for i in strings[7:10]:
#         diff = (colEnd-colStart+1)/2
#         if i =="R":
#             colStart+=diff
#         if i=="L":
#             colEnd-=diff

#     curr_num = int(rangeStart)*8+colStart
#     if curr_num>maximum:
#         maximum=curr_num

# print(int(maximum))
# ANSWER:880

seats=[]

for i in range(128):
    seats.append([True,True,True,True,True,True,True,True])

while True:
    strings = input()
    if strings=="-1":
        break

    rangeStart = 0
    rangeEnd = 127

    for i in strings[0:7]:
        diff = (rangeEnd-rangeStart+1)/2
        if i =="F":
            rangeEnd-=diff
        if i=="B":
            rangeStart+=diff

    colStart = 0
    colEnd = 7

    for i in strings[7:10]:
        diff = (colEnd-colStart+1)/2
        if i =="R":
            colStart+=diff
        if i=="L":
            colEnd-=diff

    seats[int(rangeStart)][int(colStart)] = False
    curr_num = int(rangeStart)*8+colStart



for i in range(128):
    for j in range(8):
        if seats[i][j] and 8*i+j!=1 and 8*i+j!=-1:
            print(i,j)
#ANSWER 91,3