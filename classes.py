import math
import random
import subprocess 
import os

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

class Alpha(Modifier):
	name = "a"

class Brightness(Modifier):
	name = "b"

class Saturation(Modifier):
	name = "sat"

class Hue(Modifier):
	name = "h"

class Y(Modifier):
	name ="y"

class Z(Modifier):
	name ="z"

class Rotate(Modifier):
	name = "r"

class Flip(Modifier):
	name = "f"

class X(Modifier):
	name = "x"

class Size(Modifier):
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

class Operator:
	def __str__(self):
		return str(self.lhs) + self.opsStr + str(self.rhs)
	def __init__(self, lhs, rhs):
		self.rhs = rhs
		self.lhs = lhs

class Plus(Operator):
	opsStr = "+"

class Minus(Operator):
	opsStr = "-"

class Multiply(Operator):
	opsStr = "*"

class Divide(Operator):
	opsStr = "/"

parent1 = Triangle(Skew(20, 30), Brightness(.5)) 
print (str(parent1))

parent2 = Square(Transform(45, 100), Flip(5))
print (str(parent2))

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

r = random.uniform(0, 50)


list1 = str(parent1).split()
list2 = str(parent2).split()
# list5 = list1

# for index, item in enumerate(list2):
# 	print(index, item)
# 	print(list5[index])
# 	list5[index] = list2[index]

# child2 = ' '.join(word for word in list5)

# print("here", child2)

# if have two of same size, will do crossover
def swap(l1, l2):
	l3 = l1

	for index,item in enumerate(l2):
		ran = random.uniform(0, 5)
		if (ran >= 4):
			l3[index] = l2[index]

	return l3

temp = swap(list1, list2)
child = ' '.join(word for word in temp)

createImage(templateBuild(child))

# def createImage2(code):
# 	if (not os.path.exists("output")):
# 		os.mkdir("output")

# 	with open("output/code.cfdg", "w") as fout:
# 		fout.write(code)

# 	subprocess.run(["ContextFree/ContextFreeCLI.exe", "output/code.cfdg", "output/result2.png"])

# createImage2(templateBuild(test2))

print(str(templateBuild(child)))



# will randomly pick left or right first, set left to current
# def crossover(left, right):
# 50 percent return copy of left (new node that is equivilant, except with crossover function applied to each child)
# if type(left) (use is instance?) = node - check if node, not a number 
# if random less than percent
# 	crossover: return  crossover (find_crossover(right, left))
# else
# 	don't crossover: result type (left)()
# 		for c in left.children : result.append (Crossover (c, right))

	# preferentially crossover with similar size - need a function that finds the best crossovers
	# takes in a node, node type, node size 
	# first check probability of crossover. Need to get a height function in node - do children have children? recurse. 



# class Number, variable - name that is a string, want without quotes 
# repr of a string adds quotes
# class parameter also 




# Made new modifiers, of different types - good idea? - something off about the number of args?
# Want to be able to use in program - how?

# crossover: if modifiers have same type, can interchange. Shapes can also switch. 
# can use mutation for numbers. 
# will want to be able to crossover body of shape 


# shape definition will be tricky with the types 