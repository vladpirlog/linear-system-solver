import unittest
from program import program


class Test(unittest.TestCase):
    def test01_program(self):
        self.assertEqual(program('input/test01.in'),
                         [(0.1333, -0.3667, -1.4222, 1)])

    def test02_program(self):
        self.assertEqual(program('input/test02.in'),
                         [(-0.3333, 1, 0, 0), (0.3333, 0, 1, 0), (-0.6667, 0, 0, 1)])

    def test03_program(self):
        self.assertEqual(program('input/test03.in'), [(3, -2, 1)])

    def test04_program(self):
        self.assertEqual(program('input/test04.in'),
                         [(0.8, -0.44, 0.76, -1.6, 1)])

    def test05_program(self):
        self.assertEqual(program('input/test05.in'),
                         [(0, 1, 1, 0), (-1.3333, 0.3333, 0, 1)])

    def test06_program(self):
        self.assertEqual(program('input/test06.in'), [(1, -2, 1)])

    def test07_program(self):
        self.assertEqual(program('input/test07.in'), [(0, 0, 0)])

    def test08_program(self):
        self.assertEqual(program('input/test08.in'),
                         [('x[1]', 'x[2]', 'x[3]')])

    def test09_program(self):
        self.assertEqual(program('input/test09.in'),
                         [(-2, 1, 0, 0), (3.5, 0, -2.5, 1)])

    def test10_program(self):
        self.assertEqual(program('input/test10.in'), [(0, 0, 0, 0)])

    def test11_program(self):
        self.assertEqual(program('input/test11.in'), None)

    def test12_program(self):
        self.assertEqual(program('input/test12.in'), None)

    def test13_program(self):
        self.assertEqual(program('input/test13.in'), [(0, 1, -2, 1)])

    def test14_program(self):
        self.assertEqual(program('input/test14.in'), [(0, 0, 0, 0)])

    def test15_program(self):
        self.assertEqual(program('input/test15.in'),
                         [(-2, 1, 0, 0), (-3, 0, 1, 0), (-4, 0, 0, 1)])

    def test16_program(self):
        self.assertEqual(program('input/test16.in'),
                         [(-2, 1, 0, 0), (5, 0, -3, 1)])

    def test17_program(self):
        self.assertEqual(program('input/test17.in'),
                         [(-2, 1, 0, 0), (8, 0, -4, 1)])

    def test18_program(self):
        self.assertEqual(program('input/test18.in'), [(-0.2222, 0.6667, -1, -0.7778, 1, 0, 0, 0),
                                                      (-0.717, 1.8667, -2.7684, -
                                                       0.1778, 0, 1, 0, 0),
                                                      (-0.5684, 3.4, -2.0105, -
                                                       1.8, 0, 0, 1, 0),
                                                      (-0.4865, 4.7333, -3.8526, -1.3556, 0, 0, 0, 1)])

    def test19_program(self):
        self.assertEqual(program('input/test19.in'), [(-1, 1, 0, 0)])

    def test20_program(self):
        self.assertEqual(program('input/test20.in'), [(0, 0, -1, 1)])

    def test21_program(self):
        self.assertEqual(program('input/test21.in'), [(0, -1, 1, 0)])

    def test22_program(self):
        self.assertEqual(program('input/test22.in'),
                         [(0, 0, 1, 0), (0, 0, 0, 1)])

    def test23_program(self):
        self.assertEqual(program('input/test23.in'), [(0, 0, 0, 0, 0)])


if __name__ == "__main__":
    unittest.main()
