# counter = 0
# woah = ""
# while True:
#     things = {"a":False,"b":False,"c":False,"d":False,"e":False,"f":False,"g":False,"h":False,"i":False,"j":False,"k":False,"l":False,"m":False,"n":False,"o":False,"p":False,"q":False,"r":False,"s":False,"t":False,"u":False,"v":False,"w":False,"x":False,"y":False,"z":False}
    
#     thing = input()
#     if thing=="-1":
#         break
    
#     woah+=thing
    
#     if thing =="":
#         for i in woah:
#             things[i]=True
        
#         for key in things.values():
#             if key:
#                 counter+=1
#         woah=""

# print(counter)


firstTime = True
counter = 0

comm_set = set([])

while True:
    thing = input()
    if firstTime:
        for i in thing:
            comm_set.add(i)
        firstTime=False
    
    if thing=="-1":
        break
    
    if thing != "":
        curr_arr = []
        for j in thing:
            curr_arr.append(j)
        comm_set = comm_set.intersection(curr_arr)


    if thing=="":
        counter+=len(comm_set)
        comm_set=set([])
        firstTime=True

print(counter)