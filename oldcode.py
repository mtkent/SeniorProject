


children = [None] * 100

newchildren = [None] * 100


def shapeCross(p1, p2):
	likely = 50
	newChildren = []
	for i in range(len(p1.children)):
		rand = random.uniform(0, 100)
		if (rand > likely):
			newChildren.append(p1.children[i])	# do I want chance of getting all modifiers?
		else:
			newChildren.append(p2.children[i])
			# print(p2.children[i])
	
	ran = random.uniform(0, 100)
	if ran > likely:
		# print("CHILDREN", newChildren)
		child = (type(p1))(*newChildren)
	else:
		# print("CHILDREN", newChildren)

		child = (type(p2))(*newChildren)

	# print ("here children", child.children[0][0], child.children[0][1])
	# print ("child ", child)
	return child

# print ("testing", shapeCross(parent1, parent2).children[0][0].values[0])


def shapeDefCross(p1, p2):     # need to find suitable cross 
	likely = 50
	newChildren = []
	for i in range(len(p1.children)):
		rand = random.uniform(0, 100)
		if (rand > likely):
			newChildren.append(p1.children[i])	# do I want chance of getting all modifiers?
		else:
			newChildren.append(p2.children[i])
			# print(p2.children[i])
	
	ran = random.uniform(0, 100)
	if ran > likely:
		# print("CHILDREN", newChildren)
		child = ShapeDef(p1.name, newChildren)
	else:
		# print("CHILDREN", newChildren)

		child = ShapeDef(p2.name, newChildren)

	# print ("here children", child.children[0][0], child.children[0][1])
	# print ("child ", child)
	return child

# print ("testing", shapeCross(parent1, parent2).children[0][0].values[0])

def paramCross(p1, p2, child):
	likely = 50
	for i in range (len(child.children[0])):
		for j in range (len(child.children[0][i].values)):
			rand = rand = random.uniform(0, 100)
			# print ("VAL" , p1.children[i].values[j])
			# if (rand > likely):
			# 	child.children[0][i].values[j] = p1.children[i].values[j]
			# else:
			# 	child.children[0][i].values[j] = p2.children[i].values[j]

	return child

# print ("HERE ERALSKEJRD" , paramCross(parent1, parent2, shapeCross(parent1, parent2)))



# print("NEW", shapeCross(parent1, parent2))
# print (childabc)

# split the declarations into lists of strings
list1 = str(parent1).split()
list2 = str(parent2).split()

# for shapes 
# if have two of same size, will do crossover
# will make an empty program 
def swap(l1, l2):  # want to crossover with objects instead 
	l3 = list(l1) # should start empty instead 
	for index,item in enumerate(l2):
		ran = random.uniform(0, 100)
		if (ran > 50):
			l3[index] = l2[index]
		else:
			l3[index] = l1[index]
	return l3


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False
        
def mutate(list):
	for index, item in enumerate(list):
		if (is_number(item)):
			ran = random.uniform(0, 100)
			if (ran > 85):
				rand = random.uniform(0, 100)
				if (rand > 50):
					temp = float(item) * 1.05
					list[index] = str(temp)
				else:
					temp = float(item) * .95
					list[index] = str(temp)
	# still doesn't edit last one

	return list



# def newbreed ():
# 	for _ in range(100):
# 		ran = int(random.uniform(0,99))
# 		rand = int(random.uniform(0,99))
# 		if (ran == rand):
# 			if (rand < 99):
# 				rand = rand + 1
# 			else:
# 				rand = rand - 1
# 		p1 = newchildren[ran]
# 		p2 = newchildren[rand]
# 		newreproduce(newchildren, p1, p2)

# # will choose two from previous generation, will repopulate chilren list with next generation - will do this a set number of times
# def breed():
# 	for _ in range(100):
# 		# picks new parent1
# 		ran = random.uniform(0,99)
# 		list3 = str(children[int(ran)]).split()
# 		# picks new parent2, making sure is not same one
# 		rand = random.uniform(0,99)
# 		if (ran == rand):
# 			if (rand < 99):
# 				rand = rand + 1
# 		list4 = str(children[int(rand)]).split()
# 		reproduce(children, list3, list4)


# def newreproduce(arr, p1, p2):
# 	for i in range(100):
# 		child = shapeCross(p1, p2)
# 		arr[i] = child

# newreproduce(newchildren, parent1, parent2)

# # will create a number of children 
# def reproduce(arr, par1, par2):
# 	for i in range(100):
# 		temp = swap(par1, par2)
# 		mutate(temp)
# 		child = ' '.join(word for word in temp)
# 		arr[i] = child;

# reproduce(children, list1, list2)


# breed();
# newbreed();
# print(str(templateBuild(newchildren[0])))


newShape = shapeDefCross(parent4, parent3)
program2 = Program(newShape.name, [newShape])


# PROBLEM: how to make more complicated?
# needs to traverse tree, recursively, when comes to shape node, needs to add text?
def templateBuild(object):
	return """
	startshape start
	CF::Background = [hue 120 sat 1 b -0.5]
	CF::MinimumSize = 0.1
	shape start {{
	{}
	}}
	""".format(str(object))

	
# createImage(templateBuild(children[0]))
# print(str(templateBuild(children[0])))






# was in what is now newprogram
	# splits = [3, 4, 5, 8, 34]

	# numparts = splits[random.randint(0, (len(splits) -1 ))]
	
	# p1arr = slicechildren(p1.shapes[0].children, numparts)
	# p2arr = slicechildren(p2.shapes[0].children, numparts)

	# attributes = []
	# for i in range (0, numparts):
	# 	ran = random.uniform(0,99)
		
	# 	if (ran < 50):
	# 		# if (not p1arr[i] is None) and (not p2arr[i] is None):
	# 		# if (len(p1arr[i]) > 0) and (len(p2arr[i]) > 0) and (len(p2arr) >= len(p1arr)):
	# 		# 	for j in range (0, len(p1arr)):
	# 		# swapmodifers(p1arr[i], p2arr[i])
	# 		# swapmodifers(p1arr[i], p2arr[i])
	# 		# 	print ("I SWAPPED")
	# 		attributes.extend(p1arr[i])
	# 	else:
	# 		# swapmodifers(p2arr[i], p1arr[i])
	# 		attributes.extend(p2arr[i])
	# desired = crossSequences(p1.shapes, p2.shapes) # = nonterminals - highest level





	# SWAPPING:

	# each is an array of size 0-something; are shapes
# def swapmodifers(parent, swap):
# 	swaparr = []
# 	if len(swap) > 0:
# 		for i in range (0, len(swap)):
# 				if not (not swap[i][j]):
# 					swaparr.append(swap[i][j])

# 	print ("LIST OF SWAPPABLE", swaparr)

# 	if len(parent) > 0 and len(swaparr) > 1:
# 		for i in range (0, len(parent)):
# 			ranswaparr = swaparr[random.randint(0, (len(swaparr) - 1))]
# 			if not (not parent[i]):
# 				print("parent i ", parent[i], "ran", ranswaparr)

# 				parent[i] = ranswaparr
# 				print ("new parent i ", parent[i])
# 	return parent


# p1arr = slicechildren([[1, 2, 3, 4]], 3)
# p2arr = slicechildren([[1, 123], [6, 7, 8]], 3)

# print("SWAP", swapmodifers(p1arr, p2arr))



# for mutation 
# size tricky since can't be over certain number w/o crashing, so currently not including
mod1 = [Alpha, Brightness, Saturation, Hue, Y, Z, Rotate, Flip, X, Transform]
mod2 = [X, Transform, Skew]
# will look at len(values), if 1, small chance of swapping with random element of mod1, same for 2