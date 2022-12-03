vals = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"


matchingval = ""
count = 0


with open("q3.txt", "r") as file:
    lines = file.readlines()

for line in lines:
    lineclean = line.strip()

    comp1 = lineclean[0:(len(lineclean)//2)]
    comp2 = lineclean[(len(lineclean)//2):]
    for letter in comp1:
        if letter in comp2:
            matchingval = letter
            count+=vals.index(matchingval)
            break

print(count)
    
