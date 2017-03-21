# imports
import classes
from classes import Triangle, Size, Square, Circle, Skew, Alpha, Brightness, Saturation, Hue, Y, Z, Rotate, Flip, X, Transform, ShapeDef, NonTerminal, Shape, Program, RuleCall
import functions
from functions import newprogram, createImage, programbreed, programreproduce, scramblenames, crossParams

# starter parents
parent1 = Triangle([Skew(20, 30), Brightness(.5)] ) #, Hue(41312), Y(100)) 
parent2 = Square([Transform(45, 100), Flip(5)]) #, Alpha(3), Saturation(44))

# more complicated parents 
parent3 = ShapeDef(None, [
	Square([Transform(-3, -3)]), 
	Square([Transform(3, 3)]), 
	Square([Transform(3, -3)]), 
	Square([Transform(-3, 3)]) ])

nt5 = NonTerminal("nt5", [])


parent4 = ShapeDef(None, [
	Triangle([Y (10)]), 
	Triangle([Y (5)]), 
	Triangle([Y (0)]),
	RuleCall(nt5,[Size (0.90)]) 
	])
nt4 = NonTerminal("nt4", [parent4])  # <- adding another parent just adds it to it as a rule

parent5 = ShapeDef(None, [
	Circle ([X (2), Skew (12, 45), Hue (45), Rotate (33) ]), 
	Square([Transform(3, 3), Hue (12)]), 
	Square([Transform(3, 13), Hue (12)]), 
	Triangle([Saturation (300), Alpha (43), Transform(4)]),
	RuleCall(nt4, [])

	# Shape(nt4.__copy__(), parent4)
	])

nt5.addShapeDef(parent5)

# parent4 = ShapeDef(None, [
# 	Triangle([Y (10)]), 
# 	Triangle([Y (5)]), 
# 	Triangle([Y (0)]), 
# 	])
# nt4 = NonTerminal("nt4", parent4)  # <- adding another parent just adds it to it as a rule

# parent4 = ShapeDef(None, [
# 	Triangle(Skew (10, 12)), 
# 	Triangle(Skew (5, 40)), 
# 	Triangle(Skew (0, 11)) ])
blahargs = [
	Triangle ([]), 
	]


terminatingShape = ShapeDef (None, [
	Circle([])
	])

blah2shape = ShapeDef(None, blahargs)
blah2 = NonTerminal("blah2", [blah2shape, terminatingShape])


terminatingShape.weight = 0.01

blahargs.append(RuleCall(blah2, [Alpha (0.8), Rotate (47.8), X (1), Saturation (0.9995)]))

blahshape = ShapeDef(None, [
	RuleCall(blah2, [Alpha (-1)]) ,
	RuleCall(blah2, [Flip (163), Alpha (-1), X (5), Brightness (1)])
	])





nt6 = NonTerminal("blah", [blahshape])

program7 = Program ("blah", [nt6, blah2])

nt6.setProgram(program7)

# blah2 = ShapeDef(None, [

# 	Shape ("blah2", Alpha (0.02), Rotate  (6.14), X (1), S (0.995))

# 	])

# blah = ShapeDef (None, [
# 	Shape ("blah", )

# 	])


# shape blah {
# blah2 [alpha -1]
# blah2 [ flip 146 alpha -1 x 5 b 1]
# blah2 [alpha - 2 y -5 b 1]
# blah2 [flip  146 alpha -1 x 5 y -5]
# }



# nonterminals from more complicated parents
nt3 = NonTerminal("nt3", [parent3])
# nt4 = NonTerminal("nt4", parent4)  # <- adding another parent just adds it to it as a rule
# nt41 = NonTerminal("nt41", parent4)
nt5 = NonTerminal("nt5", [parent5])
# nt6 = NonTerminal("nt6", blah2)
# nt7 = NonTerminal("nt7", blah)

# programs from nonterminals
program1 = Program("nt3", [nt3])
program2 = Program("nt4",[nt4, nt5])
program3 = Program("nt5",[nt5, nt4.__copy__()])

# need to set parents after 
nt3.setProgram(program1)
nt4.setProgram(program2)
nt5.setProgram(program3)

# # # # a single program
# aProgram = newprogram(program7, program3)
# # # print("P1 HERE", str(program1))
# # # print("P3 HERE", str(program3))

# print(str(aProgram))

# createImage(str(aProgram))


# for breeding/reproducing
programarr = [None] * 100

programreproduce(programarr, program3, program7)
programbreed(programarr)
createImage(str(programarr[0]))
print(str(programarr[0]))






# print("program 2: ", str(programarr[1]))

# print("new program: ", str(newprogram(program1, program2)))

# scramblenames(program3.shapes)
# print(str(program3))

# createImage(str(program3))
# print(str(program7))