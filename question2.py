possibilities = {
    "A Y":8,
    "A X":4,
    "A Z":3,
    "B Y":5,
    "B X":1,
    "B Z":9,
    "C Y":2,
    "C X":7,
    "C Z":6
    }


points = 0


with open("q2.txt","r") as file:
    lines = file.readlines()

for line in lines:
    points+=possibilities[line.strip()]
    
print(points)
    
    
    
    