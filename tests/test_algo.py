import unittest
from frequency import Note_Freq

class MyTestCase(unittest.TestCase):
    def test_0(self):
        n = Note_Freq("a4")
        self.assertAlmostEquals(n.frequency(), 440)
        self.assertEquals(str(type(n.frequency())), "<class 'float'>")

    def test_1(self):
        n = Note_Freq("a 4")
        self.assertEquals(False, n.frequency())

    def test_2(self):
        n = Note_Freq("A4")
        self.assertAlmostEquals(n.frequency(), 440)

    def test_3(self):
        n = Note_Freq("4a")
        self.assertEquals(False, n.frequency())

    def test_4(self):
        n = Note_Freq("# a 4")
        self.assertEquals(False, n.frequency())

    def test_5(self):
        n = Note_Freq("Asharp4")
        self.assertEquals(False, n.frequency())

    def test_6(self):
        n = Note_Freq("@$%^")
        self.assertEquals(False, n.frequency())


if __name__ == '__main__':
    unittest.main()
