import math
import subprocess 
import os

class Shape:
	def __str__(self):
		return "{} [{}]".format(self.name, self.argsStr() )
	def __init__(self, args):
		self.args = args
	def argsStr(self):
		return " ".join("{} {}".format(k, str(self.args[k])) for k in self.args)

class Square(Shape):
	name = "SQUARE"

class Circle(Shape):
	name = "CIRCLE"

class Triangle(Shape):
	name = "TRIANGLE"

class Value:
	def __str__(self):
		return repr(self.val)
	def __init__(self, val):
		self.val = val

# class Number, variable - name that is a string, want without quotes 
# repr of a string 
# repr of a string adds quotes

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

# class parameter also 






test = Square({"x":Value(2), "b":Value(.5)}) #[Plus(Value(3), Value(5)), Value(4)])
print (str(test))

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

createImage(templateBuild(test))

