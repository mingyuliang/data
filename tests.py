import unittest

from translator import englishToFrench,frenchToEnglish

class TestEnglishToFrench(unittest.TestCase):
    def test1(self):
        self.assertEqual(englishToFrench('Hello'),'Bonjour')
        self.assertEqual(englishToFrench('Hats'),'Chapeaux')


class TestfrenchToEnglish(unittest.TestCase):
    def test1(self):
       self.assertEqual(frenchToEnglish('Bonjour'),'Hello')
       self.assertEqual(frenchToEnglish('Chapeaux'),'Hats')

unittest.main()
