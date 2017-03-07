# imports
import classes
from classes import Triangle, Square, Circle, Skew, Alpha, Brightness, Saturation, Hue, Y, Z, Rotate, Flip, X, Transform, ShapeDef, NonTerminal, Shape, Program
import functions
from functions import newprogram, createImage, programbreed, programreproduce, scramblenames

# starter parents
parent1 = Triangle(Skew(20, 30), Brightness(.5) ) #, Hue(41312), Y(100)) 
parent2 = Square(Transform(45, 100), Flip(5)) #, Alpha(3), Saturation(44))

# more complicated parents 
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
	Shape("nt4", Transform(1, 2)),
	])

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
nt3 = NonTerminal("nt3", parent3)
nt4 = NonTerminal("nt4", parent4) 
nt5 = NonTerminal("nt5", parent5, parent3.__copy__())
# nt6 = NonTerminal("nt6", blah2)
# nt7 = NonTerminal("nt7", blah)

# programs from nonterminals
program1 = Program("nt3", [nt3])
program2 = Program("nt4",[nt4])
program3 = Program("nt5",[nt5, nt4.__copy__()])

# need to set parents after 
nt3.setProgram(program1)
nt4.setProgram(program2)
nt5.setProgram(program3)


aProgram = newprogram(program1, program3)
print(str(aProgram))

createImage(str(aProgram))


# programreproduce(programarr, program1, program3)
# programbreed(programarr = [None] * 100)
# createImage(str(programarr[0]))
# print(str(programarr[0]))

# print("program 2: ", str(programarr[1]))

# print("new program: ", str(newprogram(program1, program2)))

# scramblenames(program3.shapes)
# print(str(program3))

# createImage(str(program3))