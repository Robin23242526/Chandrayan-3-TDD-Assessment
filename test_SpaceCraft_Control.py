import unittest

class controlTest(unittest.TestCase):
    def setUp(self):
        self.inputCommands = 1
        
    def test_inputExists(self):
        self.assertIsNotNone(self.inputCommands)

if __name__ == "__main__":
    unittest.main()