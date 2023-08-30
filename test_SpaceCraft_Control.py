import unittest
from SpaceCraft_Control import chandrayaan3 as chandrayaan

class controlTest(unittest.TestCase):
    def setUp(self):
        self.inputCommands = ['f', 'r', 'u', 'b','l','d']
        
    def test_inputExists(self):
        self.assertIsNotNone(self.inputCommands)
    
    def test_inputType(self):
        for i in self.inputCommands:
            self.assertIn(i,"fblrud")
        self.assertIsInstance(self.inputCommands,list)

    def test_moveForward(self):
        spaceCraft = chandrayaan(0, 0, 0, 'N')
        spaceCraft.moveForward()
        self.assertEqual((spaceCraft.x, spaceCraft.y, spaceCraft.z), (0, 1, 0))

    def test_moveBackward(self):
        spaceCraft = chandrayaan(0, 0, 0, 'N')
        spaceCraft.moveBackward()
        self.assertEqual((spaceCraft.x, spaceCraft.y, spaceCraft.z), (0, -1, 0))
    
    def test_turnUp(self):
        spaceCraft = chandrayaan(0, 0, 0, 'N')
        spaceCraft.turnUp()
        self.assertEqual(spaceCraft.direction, 'U')


if __name__ == "__main__":
    unittest.main()