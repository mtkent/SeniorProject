import math
import random
import subprocess 
import os
import copy

# unit tests random.seed?
class Program: # has startshape, which shapeDef, and a dictionary of nodes
	def __str__(self):
		return """
		startshape {startshape}
		CF::Background = [hue 120 sat 1 b -0.5]
		CF::MinimumSize = 0.1
		{shapes}
		""".format(startshape = self.startshape, shapes = "\n".join(str(k) for k in self.shapes))
	def __init__(self, startshape, shapes): # shapes should be dictionary 
		self.startshape = startshape
		self.shapes = shapes # add if statment for dictionary
	def addShape (self, shape):
		self.shapes[shape.name] = shape


class ShapeDef:
	def __str__(self): #to code method
		return "shape " + self.name + "{\n" + "\n".join(str(x) for x in self.children) +  " \n } \n"
	def __init__ (self, name, children):
		self.name = name
		self.children = children

class Node:
	def __str__(self):
		return "unimplemented"
	def __init__(self, *children):
		self.children = children

class Shape(Node):
	def __str__(self):
		return "{} [{}]".format(self.name, self.argsStr() )
	def __init__(self, *args):
		super().__init__(*args)
	def argsStr(self):
		return " ".join(str(c)for c in self.children)

class Square(Shape):
	name = "SQUARE"

class Circle(Shape):
	name = "CIRCLE"

class Triangle(Shape):
	name = "TRIANGLE"



class Modifier:
	def __str__(self):
		return "{} {}".format(self.name, " ".join(str(v) for v in self.values))
	def __init__(self, *values):
		self.values = values

# 1
class Alpha(Modifier):
	name = "a"
# 1
class Brightness(Modifier):
	name = "b"
# 1
class Saturation(Modifier):
	name = "sat"
# 1
class Hue(Modifier):
	name = "h"
# 1
class Y(Modifier):
	name ="y"
# 1
class Z(Modifier):
	name ="z"
# 1
class Rotate(Modifier):
	name = "r"
# 1
class Flip(Modifier):
	name = "f"
# 1, 2, 3
class X(Modifier): 
	name = "x"
# 1, 2, 3
class Size(Modifier):    # if this larger than certain number, does not work well
	name = "s"

# takes 1, 2, 4, 6
class Transform(Modifier):
	name = "trans"

# takes 2
class Skew(Modifier):
	name = "skew"	

class Value:
	def __str__(self):
		return repr(self.val)
	def __init__(self, val):
		self.val = val


parent1 = Triangle(Skew(20, 30), Brightness(.5) ) #, Hue(41312), Y(100)) 
# parent1 = Square() Blah2(Skew(20, 30), Rotate(93.18 .10), X(14), Saturation(0.9992))
print (str(parent1))

parent2 = Square(Transform(45, 100), Flip(5)) #, Alpha(3), Saturation(44))
# TRIANGLE() blah2 [Transform(45, 100), X(3.18 101), Y(31), Brightness(0.5) ] 
print (str(parent2))

# 4 squares 
parent3 = ShapeDef("testshape", [
	Square(Transform(-10, -10)), 
	Square(Transform(10, 10)), 
	Square(Transform(10, -10)), 
	Square(Transform(-10, 10)) ])

parent4 = ShapeDef("testshape", [
	Triangle(Y (20)), 
	Triangle(Y (10)), 
	Triangle(Y (0)) ])


program1 = Program("testshape", [parent4])

# prints (45, 100) f5 2
# print (parent2.children[0].values, parent2.children[1], len(parent2.children))

# # prints SQUARE
# print (parent2.name)
# will print Triangle
# print(type(s2).__name__)
# will print true
# print(s1.__class__ == (Triangle or Square or Circle))

# size tricky since can't be over certain number w/o crashing, so currently not including
mod1 = [Alpha, Brightness, Saturation, Hue, Y, Z, Rotate, Flip, X, Transform]
mod2 = [X, Transform, Skew]
# will look at len(values), if 1, small chance of swapping with random element of mod1, same for 2

# type(p1)(newChildren) = ~p3

def shapeCross(p1, p2):
	likely = 50
	newChildren = []
	for i in range(len(p1.children)):
		rand = random.uniform(0, 100)
		if (rand > likely):
			newChildren.append(p1.children[i])	# do I want chance of getting all modifiers?
		else:
			newChildren.append(p2.children[i])
			print(p2.children[i])
	
	ran = random.uniform(0, 100)
	if ran > likely:
		print("CHILDREN", newChildren)
		child = (type(p1))(*newChildren)
	else:
		print("CHILDREN", newChildren)

		child = (type(p2))(*newChildren)

	# print ("here children", child.children[0][0], child.children[0][1])
	print ("child ", child)
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
			print(p2.children[i])
	
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


children = [None] * 100

newchildren = [None] * 100

def newreproduce(arr, p1, p2):
	for i in range(100):
		child = shapeCross(p1, p2)
		arr[i] = child

newreproduce(newchildren, parent1, parent2)

# will create a number of children 
def reproduce(arr, par1, par2):
	for i in range(100):
		temp = swap(par1, par2)
		mutate(temp)
		child = ' '.join(word for word in temp)
		arr[i] = child;

reproduce(children, list1, list2)

def newbreed ():
	for _ in range(100):
		ran = int(random.uniform(0,99))
		rand = int(random.uniform(0,99))
		if (ran == rand):
			if (rand < 99):
				rand = rand + 1
			else:
				rand = rand - 1
		p1 = newchildren[ran]
		p2 = newchildren[rand]
		newreproduce(newchildren, p1, p2)

# will choose two from previous generation, will repopulate chilren list with next generation - will do this a set number of times
def breed():
	for _ in range(100):
		# picks new parent1
		ran = random.uniform(0,99)
		list3 = str(children[int(ran)]).split()
		# picks new parent2, making sure is not same one
		rand = random.uniform(0,99)
		if (ran == rand):
			if (rand < 99):
				rand = rand + 1
		list4 = str(children[int(rand)]).split()
		reproduce(children, list3, list4)


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


def createImage(code):
	if (not os.path.exists("output")):
		os.mkdir("output")

	with open("output/code.cfdg", "w") as fout:
		fout.write(code)

	subprocess.run(["ContextFree/ContextFreeCLI.exe", "output/code.cfdg", "output/result.png"])

newShape = shapeDefCross(parent4, parent3)
program2 = Program(newShape.name, [newShape])

# breed();
# newbreed();
# print(str(templateBuild(newchildren[0])))
createImage(str(program2))

print(str(program2))

# createImage(templateBuild(children[0]))
# print(str(templateBuild(children[0])))

