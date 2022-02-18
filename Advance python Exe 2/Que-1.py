# Create a unittest for a module which has a class caled Calculator. It has 5 methods
# add, sub, mul, div and mod. All these methods must be tested with positive,
# negative float and integers including zero.


import unittest
from calc import mul,add,sub,div,mod

class MulTest(unittest.TestCase):
#add method
    def test_add1(self):
        res = add(4,5)
        self.assertEqual(9, res)
    def test_add2(self):
        res = add(4,-5)
        self.assertEqual(-1, res)
    def test_add3(self):
        res = add(-4,-5)
        self.assertEqual(-9, res)
    def test_add4(self):
        res = add(2.5, 4)
        self.assertEqual(6.5, res)
    def test_add5(self):
        res = add(4.0,-2.5)
        self.assertEqual(1.5, res)
    def test_add6(self):
        res = add(-4.0,-5.0)
        self.assertEqual(-9.0, res)
    def test_add7(self):
        res = add(0,0)
        self.assertEqual(0, res)
#sub method
    def test_sub1(self):
        res = sub(4,5)
        self.assertEqual(-1, res)
    def test_sub2(self):
        res = sub(4,-5)
        self.assertEqual(9, res)
    def test_sub3(self):
        res = sub(-4,-5)
        self.assertEqual(1, res)
    def test_sub4(self):
        res = sub(2.5, 4)
        self.assertEqual(-1.5, res)
    def test_sub5(self):
        res = sub(4.0,-2.5)
        self.assertEqual(6.5, res)
    def test_sub6(self):
        res = sub(-4.0,-5.0)
        self.assertEqual(1.0, res)
    def test_sub7(self):
        res = sub(0,0)
        self.assertEqual(0, res)
#mul method
    def test_mul1(self):
        res = mul(4,5)
        self.assertEqual(20, res)
    def test_mul2(self):
        res = mul(4,-5)
        self.assertEqual(-20, res)
    def test_mul3(self):
        res = mul(-4,-5)
        self.assertEqual(20, res)
    def test_mul4(self):
        res = mul(2.5, 4)
        self.assertEqual(10, res)
    def test_mul5(self):
        res = mul(4.0,-2.5)
        self.assertEqual(-10.0, res)
    def test_mul6(self):
        res = mul(-4.0,-5.0)
        self.assertEqual(20.0, res)
    def test_mul7(self):
        res = mul(0,0)
        self.assertEqual(0, res)
#division method
    def test_div1(self):
        res = div(10,5)
        self.assertEqual(2, res)
    def test_div2(self):
        res = div(10,-5)
        self.assertEqual(-2, res)
    def test_div3(self):
        res = div(-10,-5)
        self.assertEqual(2, res)
    def test_div4(self):
        res = div(10, 2.5)
        self.assertEqual(4, res)
    def test_div5(self):
        res = div(10.0,-2.0)
        self.assertEqual(-5.0, res)
    def test_div6(self):
        res = div(-4.0,-5.0)
        self.assertEqual(0.8, res)
    def test_div7(self):
        res = div(0,1)
        self.assertEqual(0, res)
    # mod method
    def test_mod1(self):
        res = mod(4,5)
        self.assertEqual(4, res)
    def test_mod2(self):
        res = mod(4,-5)
        self.assertEqual(-1, res)
    def test_mod3(self):
        res = mod(-4,-5)
        self.assertEqual(-4, res)
    def test_mod4(self):
        res = mod(2.5, 4)
        self.assertEqual(2.5, res)
    def test_mod5(self):
        res = mod(4.0,-2.5)
        self.assertEqual(-1.0, res)
    def test_mod6(self):
        res = add(-4.0,-5.0)
        self.assertEqual(-9.0, res)
    def test_mod7(self):
        res = mod(0,1)
        self.assertEqual(0, res)



if __name__ == '__main__':
     unittest.main()