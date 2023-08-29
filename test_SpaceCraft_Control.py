import unittest
from SpaceCraft_Control import chandrayaan3_controller as chandrayaan

class controlTest(unittest.TestCase):
    def setUp(self):
        self.inputCommands = ['f', 'r', 'u', 'b','l','d']
        
    def test_inputExists(self):
        self.assertIsNotNone(self.inputCommands)
    
    def test_inputType(self):
        for i in self.inputCommands:
            self.assertIn(i,"fblrud")
        self.assertIsInstance(self.inputCommands,list)

    def test_outputExists(self):
        self.assertIsNotNone(chandrayaan.spacecraft_controller(self.inputCommands))

    def test_outputType(self):
        self.assertIsInstance(chandrayaan.spacecraft_controller(self.inputCommands),tuple)

if __name__ == "__main__":
    unittest.main()