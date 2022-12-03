count = 0
maxcals = 0
list_cals = []
with open("elfcals.txt","r") as file:
    lines = file.readlines()


for line in lines:
    if line.strip() == "":
        list_cals.append(count)
        count = 0
    elif line!="\n":
        count+=int(line.strip())
list_cals.append(count)

list_cals.sort()
print(list_cals)
        
