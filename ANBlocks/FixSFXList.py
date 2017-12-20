with open("SFXList_ToFix.txt", "r") as file:
	content = file.readlines()

content = [x.strip() for x in content]
theGoodStuff = []
for i in content:
	theGoodPart = i.split(" ")[0]
	theGoodStuff.append(theGoodPart)

with open("SFXList.txt", "w") as file:
	for i in theGoodStuff:
		file.write(i + "\n")
