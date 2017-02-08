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

class Blah2(Shape):
	name = "blah2"


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

parent1 = Triangle(Skew(20, 30), Brightness(.5) ) #, Hue(41312), Y(100)) 
# parent1 = Square() Blah2(Skew(20, 30), Rotate(93.18 .10), X(14), Saturation(0.9992))
print (str(parent1))

parent2 = Square(Transform(45, 100), Flip(5)) #, Alpha(3), Saturation(44))
# TRIANGLE() blah2 [Transform(45, 100), X(3.18 101), Y(31), Brightness(0.5) ] 
print (str(parent2))


list1 = str(parent1).split()
list2 = str(parent2).split()

# if have two of same size, will do crossover
def swap(l1, l2):
	l3 = list(l1)
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

# will create a number of children 
def reproduce(arr, par1, par2):
	for i in range(100):
		temp = swap(par1, par2)
		mutate(temp)
		child = ' '.join(word for word in temp)
		arr[i] = child;

reproduce(children, list1, list2)

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
def templateBuild(object):
	return """
	startshape start
	CF::Background = [hue 120 sat 1 b -0.5]
	CF::MinimumSize = 0.1
	shape start {{
	{}
	}}
	""".format(str(object))

	# return """
	# startshape blah
	# CF::Background = [hue 199 sat 1 b -0.435 ]
	# CF::MinimumSize =  0.186
	# shape blah {
	# blah2 [alpha -1]
	# blah2 [ flip 65 alpha -1 x 5 b 1]
	# blah2 [alpha - 2 y -5 b 1]
	# blah2 [flip 90 alpha -1 x 5 y -5]
	# }
	# shape blah2 {{
	# {}
	# }}

	# """.format(str(object))


def createImage(code):
	if (not os.path.exists("output")):
		os.mkdir("output")

	with open("output/code.cfdg", "w") as fout:
		fout.write(code)

	subprocess.run(["ContextFree/ContextFreeCLI.exe", "output/code.cfdg", "output/result.png"])



breed();
createImage(templateBuild(children[0]))

print(str(templateBuild(children[0])))

# def createImage2(code):
# 	if (not os.path.exists("output")):
# 		os.mkdir("output")

# 	with open("output/code.cfdg", "w") as fout:
# 		fout.write(code)

# 	subprocess.run(["ContextFree/ContextFreeCLI.exe", "output/code.cfdg", "output/result2.png"])

# createImage2(templateBuild(test2))

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
