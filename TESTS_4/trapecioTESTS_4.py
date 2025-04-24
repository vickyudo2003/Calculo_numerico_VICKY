#! /var/bin/env python3
import unittest
from metodo_trapecio import *

class test(unittest.TestCase):
	def test_trapezoid_method(self):
		print("\n\n==========  METODO DEL TRAPECIO  =====================================")
		f1 = lambda x: x*math.cos(x**2)
		f2 = lambda x: math.sin(x) - x**2
		self.assertEqual(view_result_trapeze(f1,0,1,4),0.23858922110272346)
		self.assertEqual(view_result_trapeze(f2,0,1,4),0.046867405336244575)

if __name__ == '__main__':
	unittest.main()