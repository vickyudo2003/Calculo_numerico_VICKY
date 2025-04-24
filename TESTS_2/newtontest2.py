#! /var/bin/env python3
import unittest
from newton_Rapson import *

class test(unittest.TestCase):
	def test_newton_raphson_method(self):
		print("\n\n==========  METODO DE NEWTHON RAPHSON  ===============================")
		f1 = lambda x: math.exp(x) - 2*x**2
		f2 = lambda x: pow((x-2),2) - math.log(x)
		f3 = lambda x: math.sin(x) - math.exp(-x)
		self.assertEqual(newton_raphson(f1,0.5,0.02,10),2.6212275327680024)
		self.assertEqual(newton_raphson(f2,1,0.05,20),1.4124215461418443)
		self.assertEqual(newton_raphson(f3,0.5,0.02,10),0.5885488916184832)

if __name__ == '__main__':
	unittest.main()