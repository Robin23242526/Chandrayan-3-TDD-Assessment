import unittest
import string

class controlTest(unittest.TestCase):
    def setUp(self):
        self.inputCommands = ['f', 'r', 'u', 'b','l','d']
        
    def test_inputExists(self):
        self.assertIsNotNone(self.inputCommands)
    
    def test_inputType(self):
        for i in self.inputCommands:
            self.assertIn(i,"fblrud")
        self.assertIsInstance(self.inputCommands,list)

if __name__ == "__main__":
    unittest.main()