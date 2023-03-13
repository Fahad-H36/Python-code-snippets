from node import BSTNode



tree = BSTNode()


def customInsert(t):
	val = input("Enter value you want to insert: ")
	try:
		val = int(val)
		t.insert(val)
	except:
		print("=> Enter Integer Input")
		customInsert(t)

def customDelete(t):
	val = input("=> Enter value you want to Delete: ")
	try:
		val = int(val)
		assert t.exists(val) == True
		t.delete(val)
	except:
		print("=> Either you have inserted a non-integer value or this Integer does not exist in the tree")
		customDelete(t)



with open("code.txt", "r") as f:
	file = f.read()

lines = file.split("\n")

vals = []
for i in lines:
	for j in i.split():
		vals.append(int(j))


for i in vals:
	tree.insert(i)

print("=> All the data from file is added to the tree ", tree.inorder([]))


message = "=> Enter 'A' to add any element, 'D' to delete any element and any other key to exit: "

choice = input(message)
while(choice == "a" or choice == "A" or choice == "D" or choice == "d"):
	if choice == "a" or choice == "A":
		customInsert(tree)

	elif choice == "D" or choice == "d":
		customDelete(tree)

	choice = input(message)

print("=> The Final Data", tree.inorder([]))

fileName = 'code.txt'
file1 = open(fileName, 'w')
for i in tree.inorder([]):
	file1.write(str(i)+" ")
file1.close()
print("=> Data stored in file " + fileName)

