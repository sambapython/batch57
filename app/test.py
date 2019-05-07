import unittest
from main import fun
class FunTest(unittest.TestCase):

	@classmethod
	def setUpClass(cls):
		print("login")
		cls.user="USER!"
	@classmethod
	def tearDownClass(cls):
		print("logout")
		cls.user=None
	def setUp(self):
		print("creating resource")
	def tearDown(self):
		print("deleting resource")
	def test_10_20(self):
		print(self.user)
		act=fun(10,20)
		exp=30
		self.assertEqual(act, exp, "test_10_20 failed")
	def test_10_str1(self):
		print(self.user)
		act=fun(10,"str1")
		exp=None
		self.assertEqual(act, exp, "test_10_str1 failed")
	def test_str2_20(self):
		print(self.user)
		act=fun("str2",20)
		exp=None
		self.assertEqual(act, exp, "test_str2_20 failed")
	def test_str1_str2(self):
		print(self.user)
		act=fun("str1","str2")
		exp="str1str2"
		self.assertEqual(act, exp, "test_str1_str2 failed")
unittest.main()