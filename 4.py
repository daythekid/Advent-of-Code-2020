# counter = 0
# woah = ""
# while True:
#     things = {"byr":False,"iyr":False,"eyr":False,"hgt":False,"hcl":False,"ecl":False,"pid":False}
    
#     thing = input()
#     if thing=="-1":
#         break
#     woah+=thing
#     if thing =="":
#         for i in range(len(woah)):
#             if woah[i]==":":
#                 things[woah[i-3:i]] = True
#         if all(value==True for value in things.values()):
#             counter +=1
#         woah=""

# print(counter)

#ANSWER 200



counter = 0
woah = ""
while True:
    things = {"byr":"1231","iyr":"1233","eyr":"1232","hcl":"a","ecl":"as","pid":"2","hgt":"123434234"}
    
    thing = input()
    if thing=="-1":
        break
    woah+=" "+thing
    if thing =="":
        newList = woah.split()
        for i in newList:
            things[i.split(":")[0]] = i.split(":")[1]
        test1=False
        test2=False

        if 1920<=int(things["byr"])<=2002:
            if 2010<=int(things["iyr"])<=2020:
                if 2020<=int(things["eyr"])<=2030:
                    if things["hcl"][0]=="#" and len(things["hcl"])==7:
                        test1=True
                        for i in things["hcl"][1:7]:
                            if i not in ["0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f"]:
                                test1=False
                    if things["ecl"] in ["amb","blu","brn","gry","grn","hzl","oth"]:
                        if len(things["pid"])==9 and int(things["pid"])>-100:
                            if things["hgt"][-2:]=="cm":
                                if 150<=int(things["hgt"][0:len(things["hgt"])-2])<=193:
                                    test2 = True
                            elif things["hgt"][-2:]=="in":
                                if 59<=int(things["hgt"][0:len(things["hgt"])-2])<=76:
                                    test2 = True


        if test2 and test1:
            counter+=1

        woah=""

print(counter)
