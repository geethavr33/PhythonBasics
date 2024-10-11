var="{([])}" #string input
dict1={"{":"}","(":")","[":"]","<":">"} #dictionary declare
length=len(var) #find the length of var
if length%2==0: #check if length is even
    while True: #loop continues until its true
        var1=var # set var to var1
        for i,j in dict1.items(): #loop through each opening and closing
            var=var.replace(i+j,"") #if matches replace with empty string
        if var==var1: #if no changes made then break
            break
if var=="": #if resulting var is empty
    print("Ok") #print ok
else:
    print("not Ok") #else print not ok