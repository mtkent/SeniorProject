# imports
import math
import random
import subprocess 
import os
import copy
import string
import classes
from classes import Triangle, Square, Circle, Skew, Alpha, Brightness, Saturation, Hue, Y, Z, Rotate, Flip, X, Transform, ShapeDef, NonTerminal, Shape, Program, RuleCall

# will pull needed code to make sure it calls everything it should
def flattenNT (nt, soFar = None):
	if soFar == None:
		soFar = {nt}
	result = [nt]

	# print("FLATTENING", nt, "program", nt.program, "nt.children", nt.children)
	# = FLATTENING shape program None nt3 nt.children ()
	for rule in nt.children:
		for child in rule.children:
			if isinstance(child, RuleCall) and child not in result:
				if child.rule not in soFar:
					soFar.add(child.rule)
					result.extend(flattenNT((child.rule), soFar))
	return result

def pickPartner (rule, p1, p2):     # finding a suitable match - for shapedefs 
# TODO:  add weights to try to find a match that is a similar weight 
	parent = rule.parent.program 
	otherParent = (p1, p2) [parent == p1]  # clever tuple work 
	print("parent", parent, "otherParent", otherParent)
	ran = random.choice(otherParent.shapes)

	return random.choice(ran.children)

# make a program into something of size 1, with each line taking a certain amount of space
# program has a name and a list of shapes - startshape and shapes
# working fairly well, will sometimes drop ones, especially at end?
def slicechildren (children, numparts):
	toReturn = [None] * numparts 
	size = int(math.ceil(len(children) / numparts))
	splitAt = [0]
	for i in range (numparts):
		splitAt.append(splitAt[-1] + size)


	for i in range (numparts):

		# ran = random.uniform(0,99)
		# # the lower the number the fewer shapes will go into final program
		# # have higher chance of overlap - good for small programs, but LOTS of repetition, since breeding takes away varience
		# if (ran < 75):
		# 	size1 = size + 1
		# else: 
		# 	size1 = size - 1

		# start = i * size
		toReturn[i] = children[splitAt[i]: splitAt[i + 1]]
		
	return toReturn

# knows how to cross shapes - a single one at a time
def crossSequences (s1, s2):
	splits = [3, 4, 5, 8, 34]
	numparts = random.choice(splits)
	print(numparts, "numparts")
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
	crosschildren = crossSequences(rule.children, partner.children)

	# call cross attributes 
	weight = random.choice([rule.weight, partner.weight])

	return ShapeDef(None, crosschildren, weight)

# crosses nonterminals, which calls the crossing of its children: shapedefs
def crossNT (nt1, nt2, p1, p2):
	rules = crossSequences(nt1.children, nt2.children)
	# print("rules", rules, "rules")
	result = []
	
	for rule in rules:
		partner = pickPartner (rule, p1, p2) # a shapedef 
		print("rule", rule)
		print("partner", partner)
		newShapeDef = crossShapeDef(rule, partner, p1, p2)
		print("new shape", newShapeDef)
		result.append(newShapeDef)

	ran = random.uniform(0,99)
	if ran > 50:
		name = nt1.name
	else:
		name = nt2.name

	returnNT = NonTerminal(name, *result)
	return flattenNT(returnNT)

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
	print("result", result, "result")

	# scramblenames(result)                                           #does this mean we won't call any shapes correctly?
	return (Program(result[0].name, result))

# breeding and reproduction

def programreproduce(arr, prog1, prog2):
	for i in range(100):
		child = newprogram(prog1, prog2)
		arr[i] = child


def programbreed (programarr):
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

