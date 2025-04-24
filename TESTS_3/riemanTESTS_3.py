#! /var/bin/env python3
import unittest
from integral_Rieman import *

class test(unittest.TestCase):
	def test_Rieman_method(self):
		print("\n\n==========  METODO DE RIEMAN  ========================================")
		f1 = lambda x: x / (x**2 + 1)
		f2 = lambda x: x * (x**2 + 1)**0.5
		self.assertEqual(view_result_Rieman(f1,0,1,4),0.2788235294117647)
		self.assertEqual(view_result_Rieman(f2,1,2,4),2.4116477770123668)

if __name__ == '__main__':
	unittest.main()