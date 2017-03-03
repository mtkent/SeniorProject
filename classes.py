# imports
import math
import random
import subprocess 
import os
import copy
import string

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

class NonTerminal:
	def __str__(self):
		return ("\n".join(str(k) for k in self.children))
	def __init__ (self, *children, program = None):
		self.children = children
		for c in self.children:
			c.parent = self
		self.program = program
	def setProgram (self, p):              # should I have self here? yes
		self.program = p
		# for c in self.children:
		# 	c.setProgram(c, p)
	def addShapeDef (self, shapedef):
		self.children.append(shapedef)
		shapedef.parent = self
	def __copy__ (self):
		self.copyHelper({})
	def copyHelper (self, dictionary):
		if self in dictionary:
			return dictionary[self]
		else:
			result =NonTerminal(*[c.copyHelper(dictionary) for c in self.children], program = None)
			dictionary[self] = result
			return result

class ShapeDef:
	def __str__(self): #to code method
		return "rule " + self.parent.name + " " + str(self.weight) + "{\n" + "\n".join(str(x) for x in self.children) +  " \n } \n"
	def __init__ (self, parent, children, weight = 1):
		self.parent = parent
		self.children = children
		self.weight = weight
	# def setProgram (self, p):                                  # do I want this?
	# 	self.program = p
	# 	for c in self.children:
	# 		c.setProgram(p)
	def __copy__ (self):
		self.copyHelper({})
	def copyHelper (self, dictionary):
		if self in dictionary:
			return dictionary[self]
		else:
			result = ShapeDef(None, [c.copyHelper(dictionary) for c in self.children], self.weight)
			dictionary[self] = result
			return result

class Node:
	def __str__(self):
		return "unimplemented"
	def __init__(self, *children):
		self.children = children
	def __copy__ (self):
		self.copyHelper({})
	def copyHelper (self, dictionary):
		if self in dictionary:
			return dictionary[self]
		else:
			result = type(self)([c.copyHelper(dictionary) for c in self.children])
			dictionary[self] = result
			return result
			
# added copy
class Shape(Node):
	def __str__(self):
		return "{} [{}]".format(self.name, self.argsStr() )
	def __init__(self, name, *args):
		super().__init__(*args)
		self.name = name
	def argsStr(self):
		return " ".join(str(c)for c in self.children)

# need to copy?
class SimpleShape (Shape):
	def __init__ (self, *args):
		super().__init__(None, *args)
		del self.name

class RuleCall (Shape):
	def __init__(self, rule, *args):
		super().__init__(rule.name, *args)
		self.rule = rule
	def __str__(self):
		self.name = self.rule.name
		return super().__str__(self)
	def __copy__ (self):
		self.copyHelper({})
	def copyHelper (self, dictionary):
		if self in dictionary:
			return dictionary[self]
		else:
			result = type(self)(self.rule.copyHelper(dictionary), [c.copyHelper(dictionary) for c in self.children])
			dictionary[self] = result
			return result

# shapes
class Square(SimpleShape):
	name = "SQUARE"

class Circle(SimpleShape):
	name = "CIRCLE"

class Triangle(SimpleShape):
	name = "TRIANGLE"

class Modifier:
	def __str__(self):
		return "{} {}".format(self.name, " ".join(str(v) for v in self.values))
	def __init__(self, *values):
		self.values = values

# modifers and value
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
parent2 = Square(Transform(45, 100), Flip(5)) #, Alpha(3), Saturation(44))

# 4 squares 
parent3 = ShapeDef(None, [
	Square(Transform(-3, -3)), 
	Square(Transform(3, 3)), 
	Square(Transform(3, -3)), 
	Square(Transform(-3, 3)) ])

parent4 = ShapeDef(None, [
	Triangle(Y (10)), 
	Triangle(Y (5)), 
	Triangle(Y (0)) ])

parent5 = ShapeDef(None, [
	Circle (X (2), Skew (12, 45), Hue (45), Rotate (33) ), 
	Square(Transform(3, 3)), 
	Triangle(Saturation (300), Alpha (43), Transform(4)),
	Shape("newshaape", Transform(1, 2)),
	])

nt4 = NonTerminal(parent4)
nt3 = NonTerminal(parent3) 
nt5 = NonTerminal(parent5, parent3)

program1 = Program("testshape", [nt3])
program2 = Program("newshape",[nt4])
program3 = Program("newshape",[nt5, nt4])

print("p1 here: ", type(program1))
nt3.setProgram(program1)
nt4.setProgram(program2)
nt5.setProgram(program3)

# will pull needed code to make sure it calls everything it should
def flattenProgram (nt):
	result = []

	for rule in nt:
		for child in rule.children:
			if isinstance(child, RuleCall):
				result.append(child.rule) 

	return result

def pickPartner (rule, p1, p2):     # finding a suitable match - for shapedefs  add weights 
	partner = None
	parent = rule.parent.program  #how do we know?
	otherParent = (p1, p2) [parent == p1]  # clever tuple work 

	ran = random.choice(otherParent.children)

	return random.choice(ran.children)

# make a program into something of size 1, with each line taking a certain amount of space
# program has a name and a list of shapes - startshape and shapes
# working fairly well, will sometimes drop ones, especially at end?
def slicechildren (children, numparts):
	toReturn = [None] * numparts 
	size = math.ceil(len(children) / numparts)

	for i in range (0, numparts):
		ran = random.uniform(0,99)
		# the lower the number the fewer shapes will go into final program
		# have higher chance of overlap - good for small programs, but LOTS of repetition, since breeding takes away varience
		if (ran < 75):
			size1 = size + 1
		else: 
			size1 = size - 1

		start = i * size
		toReturn[i] = children[start: (start + size1)]
	
	return toReturn

# knows how to cross shapes - a single one at a time
def crossSequences (s1, s2):
	splits = [3, 4, 5, 8, 34]
	numparts = splits[random.randint(0, (len(splits) -1 ))]
	
	p1arr = slicechildren(s1, numparts)
	p2arr = slicechildren(s2, numparts)

	attributes = []
	for i in range (0, numparts):
		ran = random.uniform(0,99)
		
		if (ran < 50):
			attributes.extend(p1arr[i])
		else:
			attributes.extend(p2arr[i])

	return attributes

# crossing the shapedefs - will cross its children: (simple)shapes
# why do we need to know the parents?
def crossShapeDef(rule, partner, p1, p2):   
	result = []
	rprog = rule.parent.program
	pprog = partner.parent.program
	children = rule.children
	crosschildren = crossSequences(rule.chilren, partner.children)

	# call cross attributes 
	weight = random.choice([rule.weight, partner.weight])

	return ShapeDef(None, crosschildren, weight)

# crosses nonterminals, which calls the crossing of its children: shapedefs
def crossNT (nt1, nt2, p1, p2):
	rules = crossSequences(nt1.children, nt2.children)
	result = []
	
	for rule in rules:
		partner = pickPartner (rule, p1, p2) # a shapedef 
		result.append[crossShapeDef(rule, partner, p1, p2)]

	return flattenProgram(NonTerminal(*result))

def scramblenames (nts):
# add unique prefixes to names of program - programs don't have names...
	i = 0
	for nt in nts:
		nt.name += str(i) # + nt.name(:20)
		i += 1

# crossover for programs - doesn't take care of shape parameters
# will need to iterate if more than one shape
def newprogram (p1, p2):	
	result = crossNT(p1.startshape, p2.startshape, p1, p2)
	scramblenames(result)                                           #does this mean we won't call any shapes correctly?
	return (Program(result[0].name, result))

# breeding and more generations

programarr = [None] * 100

def programreproduce(arr, prog1, prog2):
	for i in range(100):
		child = newprogram(prog1, prog2)
		arr[i] = child


def programbreed ():
	# firsthalf = programarr[0:49]
	# secondhalf = programarr[50:99]
	for _ in range(100):
		newarr = []
		
		ran = int(random.uniform(0,99))
		rand = int(random.uniform(0,99))
		if (ran == rand):
			if (rand < 99):
				rand = rand + 1
			else:
				rand = rand - 1
		p1 = programarr[ran]
		p2 = programarr[rand]
		# p3 = firsthalf[math.ceil(ran/2)]
		# p4 = secondhalf[math.ceil(rand/2)]

		# programreproduce(firsthalf, p1, p2)
		# programreproduce(secondhalf, p3, p4)

		programreproduce(programarr, p1, p2)
		# newarr.extend(secondhalf)
		# newarr.extend(secondhalf)
		# programarr = newarr

def createImage(code):
	if (not os.path.exists("output")):
		os.mkdir("output")

	with open("output/code.cfdg", "w") as fout:
		fout.write(code)

	subprocess.run(["ContextFree/ContextFreeCLI.exe", "output/code.cfdg", "output/result.png"])

# aProgram = newprogram(program1, program2)
# createImage(str(aProgram))
# print(str(aProgram))

# programreproduce(programarr, program1, program3)
# programbreed()
# createImage(str(programarr[0]))
# print(str(programarr[0]))

# print("program 2: ", str(programarr[1]))

# print("new program: ", str(newprogram(program1, program2)))
print(str(program3))

createImage(str(program3))