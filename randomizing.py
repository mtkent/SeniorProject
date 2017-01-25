import math
import random
from cross_mutate import cross_mutate
from cross_mutate import cross_mutate_neg


hue = cross_mutate_neg(4000, 4000)
b = random.uniform(0, -.5) 
b1 = round(b, 3)
minSize = random.uniform(0, .3)
minSize1 = round(minSize, 3)
flip = cross_mutate(0, 360)
subtract = cross_mutate(1, 10)
alpha = random.uniform(0.0001, 0.05)
alpha1 = round(alpha, 2)
r = random.uniform(0, 50)
r1 = round(r, 2)
sats = [.9995, .995, .95]
sat1 = sats[random.randint(0, 2)]

shapes = ["TRIANGLE", "CIRCLE", "SQUARE"]
shape = shapes[random.randint(0, 2)]

print ("startshape blah")
print("CF::Background = [hue" ,hue, "sat 1 b" ,b1,"]") 
print ("CF::MinimumSize = ",minSize1,)

print ("shape blah {")
print ("blah2 [alpha -1]")
print  ("blah2 [ flip" ,flip, "alpha -1 x 5 b 1]")
print  ("blah2 [alpha -" ,subtract, "y -5 b 1]")
print  ("blah2 [flip " ,flip, "alpha -1 x 5 y -5]")
print ("}")

print ("shape blah2 {")
print  ("",shape, "[]")
print  ("blah2 [alpha" ,alpha1, " r ",r1,"..10 x 1 s" ,sat1, "]")
print ("}")