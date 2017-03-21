import unittest
import classes
from classes import Triangle, Square, Circle, Skew, Alpha, Brightness, Saturation, Hue, Y, Z, Rotate, Flip, X, Transform, ShapeDef, NonTerminal, Shape, Program

# unittesting refuses to work because does not consider objects equal since at different memory

# parent3 = ShapeDef(None, [
#     Square(Transform(-3, -3)), 
#     Square(Transform(3, 3)), 
#     Square(Transform(3, -3)), 
#     Square(Transform(-3, 3)) ])

# parent4 = ShapeDef(None, [
#     Triangle(Y (10)), 
#     Triangle(Y (5)), 
#     Triangle(Y (0)) ])


p1 = ShapeDef(None, [
    Circle ([X (2)])    ])



# # nonterminals from more complicated parents
# nt3 = NonTerminal("nt3", parent3)
# nt4 = NonTerminal("nt4", parent4) 
# nt5 = NonTerminal("nt5", parent5, parent3.__copy__())
# # nt6 = NonTerminal("nt6", blah2)
# # nt7 = NonTerminal("nt7", blah)

# # programs from nonterminals
# program1 = Program("nt3", [nt3])
# program2 = Program("nt4",[nt4])
# program3 = Program("nt5",[nt5]) #, nt4.__copy__()])

# # need to set parents after 
# nt3.setProgram(program1)
# nt4.setProgram(program2)
# nt5.setProgram(program3)

class TestCopy(unittest.TestCase):

    def test_shapedef(self):
        # self.assertEqual(parent3, parent3.__copy__())
        # self.assertEqual(parent4, parent4.__copy__())
        self.assertEqual(str(p1.children[0].children[0]), str(p1.__copy__().children[0].children[0]) ) #.__copy__().parent)
        # print("p5 parent:", parent5.parent, "copy: ", parent5.__copy__().parent)
        # self.assertEqual(parent5.children, parent5.__copy__().children)

    # def test_nonterminal(self):
    #     # self.assertEqual(nt3, nt3.__copy__())
    #     # self.assertEqual(nt4, nt4.__copy__())
    #     self.assertEqual(nt5, nt5.__copy__())       

    # def test_isupper(self):
    #     self.assertTrue('FOO'.isupper())
    #     self.assertFalse('Foo'.isupper())

    # def test_split(self):
    #     s = 'hello world'
    #     self.assertEqual(s.split(), ['hello', 'world'])
    #     # check that s.split fails when the separator is not a string
    #     with self.assertRaises(TypeError):
    #         s.split(2)

if __name__ == '__main__':
    unittest.main()