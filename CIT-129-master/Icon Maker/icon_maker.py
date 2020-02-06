#setting up variable 

newLine=0

#opening file and assigning it to a variable

f = open("icon_files/icon_data.txt").readlines()


#making list for file to go into
iconList=[]


for i in f:
    #stripping the quotes( ' ' ) from the strings within list
    iconList.append(i.strip())
 
#switching strings to integers within the list
iconList = [int(i) for i in iconList] 


#turning the 0's and 1's into true and false, making a new list

bool_list = [bool(i) for i in iconList]


#for loop to assign a string value to false and true then printing it
for i in bool_list:
    if i == False:
        print(" ", end=' ')
        newLine = newLine + 1
    else:
        print("@", end=' ')
        newLine = newLine + 1
        
    if newLine == 10:
        print("\n")
        newLine=0
