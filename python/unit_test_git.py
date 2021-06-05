import unittest
from git_test import GitTest

class TestStringMethods(unittest.TestCase):
	def __init__(self, *args, **kwargs):
		unittest.TestCase.__init__(self, *args, **kwargs)
		self.gt = GitTest()
		self.default_data = 'qwertyuiop[]\n'

	def test_convert_all(self):
		self.assertEqual('TestGit123456gmail', self.gt.get_uset())

	def test_get_content(self):
		self.assertEqual(self.default_data, self.gt.get_content('test/unit_test.txt'))

	def test_write_content(self):
		data = '][poiuytrewq'
		self.gt.write_content(data, 'test/unit_test.txt')
		self.assertEqual(data, self.gt.get_content('test/unit_test.txt'))

		self.gt.write_content(self.default_data, 'test/unit_test.txt')
		self.assertEqual(self.default_data, self.gt.get_content('test/unit_test.txt'))

	#def tearDown(self):
	#	del self.gt


if __name__ == '__main__':
	unittest.main()