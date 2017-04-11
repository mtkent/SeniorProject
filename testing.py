# testing.py: where all testing and program creation happens

# imports
import classes
from classes import Triangle, Size, Square, Circle, Skew, Alpha, Brightness, Saturation, Hue, Y, Z, Rotate, Flip, X, Transform, ShapeDef, NonTerminal, Shape, Program, RuleCall, randRange
import functions
from functions import newprogram, createImage, programbreed, programreproduce, scramblenames, crossParams, fitness, avgFitness


#  -------------------------- parent definition here ----------------------------------

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


# first recursive parent
blahargs = [
	Triangle ([]), 
	]


terminatingShape = ShapeDef (None, [
	Circle([])
	])

blah2shape = ShapeDef(None, blahargs)
blah2 = NonTerminal("blah2", [blah2shape])


terminatingShape.weight = 0.1

blahargs.append(RuleCall(blah2, [Alpha (0.04), Rotate (47.83), randRange(10), X (1), Size (0.9995), Saturation(0.7)]))

blahshape = ShapeDef(None, [
	RuleCall(blah2, [Alpha (-1)]) ,
	RuleCall(blah2, [Flip (163), Alpha (-1), X (1), Brightness (1)]), 
	RuleCall(blah2, [Alpha (-10), Y (-5), Brightness(1)]), 
	RuleCall(blah2, [Flip (163), Alpha (-1), X (5), Y (-5)])
	])





nt6 = NonTerminal("blah", [blahshape])

program7 = Program ("blah", [nt6, blah2])

nt6.setProgram(program7)

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


# tendris parent: https://contextfreeart.org/gallery/view.php?id=3807

armArgs1 = [
	Circle ([]), 
	]

armArgs2 = [
	Circle ([]), 
	]

armShape1 = ShapeDef(None, armArgs1, 98)
armShape2 = ShapeDef(None, armArgs2, 2)

arm = NonTerminal("arm", [armShape1, armShape2])
armArgs1.append(Circle([Size (0.9), Brightness (1)]))
armArgs1.append(RuleCall (arm, [Y (0.2), Size (0.99), Rotate (3)]))


armArgs2.append(
	Circle([Size (0.9), Brightness (1)])
	)
armArgs2.append(RuleCall (arm, [Y (0.2), Size (0.99), Flip (90)]))
armArgs2.append(RuleCall (arm, [Y (0.2), Size (0.6), Brightness(0.2)]))

tendrisShape = ShapeDef (None, [
	RuleCall (arm, [Hue (348.16), Saturation (0.7039), Brightness (1.0000)]),
	RuleCall (arm, [Flip (90), Hue (282.99), Saturation (0.7412), Brightness (1)])
])
 


tendris = NonTerminal("tendris", [tendrisShape])

online1 = Program("tendris", [tendris, arm])

tendris.setProgram(online1)
arm.setProgram(online1)



# flower parent: https://contextfreeart.org/gallery/view.php?id=122
cs1args = [
	Square([])
]
cs2args = [
	Circle ([Size (3.5), Brightness (0.5)])
]
cs3args = [
	Square([])
]

flowerArgs = [
	Triangle([Size (15, 1), Rotate (45)])
]
flowerShape = ShapeDef(None, flowerArgs)
flower = NonTerminal("flower", [flowerShape])
flowerArgs.append(RuleCall(flower, [Size (0.9), Rotate(45)]))

startArgs = []
sceneArgs = []

curveShape1 = ShapeDef(None, cs1args, 1)
curveShape2 = ShapeDef(None, cs2args, 0.007)
curveShape3 = ShapeDef(None, cs3args, 0.01)

sceneShape = ShapeDef(None, sceneArgs)
startShape = ShapeDef(None, startArgs)
start = NonTerminal("start", [startShape])


curve = NonTerminal("curve", [curveShape1, curveShape2, curveShape3])
cs1args.append(RuleCall(curve, [Y (1), Size (0.997), Rotate (5)])) 
cs2args.append(RuleCall(curve, [Y (1), Size (0.99), Rotate (10)]))
cs3args.append(RuleCall(flower, []))
cs3args.append(RuleCall(curve, [Y (1), Size (0.99), Rotate (-40), Skew (10, 0)]))

scene = NonTerminal("scene", [sceneShape])
sceneArgs.append(RuleCall(curve, []))
sceneArgs.append(RuleCall(start, [Size (0.995), Rotate (20), Brightness (0.01), Hue (0.1), Saturation (0.8)]))

startArgs.append(RuleCall(scene, [Brightness (0.01), Hue (0), Saturation (0.8)]))

online2 = Program("start", [start, scene, curve, flower])
curve.setProgram(online2)
scene.setProgram(online2)
flower.setProgram(online2)
start.setProgram(online2)



# map parent: https://contextfreeart.org/gallery/view.php?id=185


wsArg1 = []
wsArg2 = [
	Square ([])
]
wsArg3 = [
	Square([])
]
wsArg4 = []

wallShape1 = ShapeDef (None, wsArg1)
wallShape2 = ShapeDef (None, wsArg2)
wallShape3 = ShapeDef (None, wsArg3, 0.09)
wallShape4 = ShapeDef (None, wsArg4, 0.005)

wall = NonTerminal("wall", [wallShape1, wallShape2, wallShape3, wallShape4])

wsArg1.append(RuleCall(wall, [Y (0.95), Rotate (1), Size (0.975)]))
wsArg2.append(RuleCall(wall, [Y (0.95), Rotate (-1), Size (0.975), Saturation (0.1), Brightness (0.01), Hue (0.1)]))
wsArg3.append(RuleCall(wall, [Y (0.95), Rotate (90), Size (0.975)]))
wsArg3.append(RuleCall(wall, [Y (0.95), Rotate (-90), Size (0.975)]))
wsArg4.append(RuleCall(wall, [Y (0.97), Rotate (90), Size (1.5)]))
wsArg4.append(RuleCall(wall, [Y (0.97), Rotate (-90), Size (1.5)]))

ancientmapShape = ShapeDef(None, [
	RuleCall(wall, [Brightness (0.1), Hue (34)]),
	RuleCall(wall, [Brightness (0.1), Rotate (180), Hue (34)])
	])
ancientmap = NonTerminal("ancientmap", [ancientmapShape])

online4 = Program("ancientmap", [ancientmap, wall])
ancientmap.setProgram(online4)
wall.setProgram(online4)



# sun parent: https://contextfreeart.org/gallery/view.php?id=1872
sunShapeArgs = []
cordShapeArgs = [
	Circle([Saturation (1), Hue (270)])
] 
sunShape = ShapeDef(None, sunShapeArgs)

cordShape = ShapeDef(None, cordShapeArgs)

 
sun = NonTerminal("sun", [sunShape])
cord = NonTerminal("cord", [cordShape])

sunShapeArgs.append(RuleCall(cord, []))
sunShapeArgs.append(RuleCall(sun, [X (1), Rotate (60), Hue (3), Saturation (-0.19), Size (0.999), Brightness (0.1)]))
cordShapeArgs.append(RuleCall(cord, [Y (1), Rotate (60.1), Size (0.98)]))

online5 = Program ("sun", [sun, cord])
sun.setProgram(online5)
cord.setProgram(online5)

#  ----------------------- testing happens here ---------------------------------------

# creates number of shapes
for i in range (9):

	# a single program generation

	# aProgram = newprogram(online1, online5)              # pick parents here

	# print(str(aProgram))                       # see the progarm text
	# print("my fitness: ", fitness(aProgram))   # testing fitness
	# createImage(str(aProgram), ("code" + str(i)), ("result" + str(i)))



	# array for breeding/reproducing 
	programarr = [None] * 100

	programreproduce(programarr, online5, online2)             # pick parents here
	# currently only doing one generation, can increase second param to however many generations wanted
	programbreed(programarr, 0)

	# name result correctly 
	createImage(str(programarr[0]), ("code" + str(i)), ("result" + str(i)))

	# print the text, fitness
	print(str(programarr[0]))
	print(avgFitness(programarr), "AVG FITNESS")
	print(fitness(programarr[0]), "THIS FITNESS")
