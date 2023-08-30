import unittest
from SpaceCraft_Control import chandrayaan3 as chandrayaan

class controlTest(unittest.TestCase):
    def setUp(self):
        self.inputCommands = ['f', 'r', 'u', 'b','l','d']
        
    # tests for input-------------------------------------------------------- 
    def test_inputExists(self):
        self.assertIsNotNone(self.inputCommands)
    
    def test_inputType(self):
        for i in self.inputCommands:
            self.assertIn(i,"fblrud")
        self.assertIsInstance(self.inputCommands,list)

    # tests for rotate and move functions------------------------------------
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

    def test_turnDown(self):
        spaceCraft = chandrayaan(0, 0, 0, 'N')
        spaceCraft.turnDown()
        self.assertEqual(spaceCraft.direction, 'D')

    def test_turnLeft(self):
        spaceCraft = chandrayaan(0, 0, 0, 'N')
        spaceCraft.turnLeft()
        self.assertEqual(spaceCraft.direction, 'W')
    
    def test_turnRight(self):
        spaceCraft = chandrayaan(0, 0, 0, 'N')
        spaceCraft.turnRight()
        self.assertEqual(spaceCraft.direction, 'E')
    # tests for chandrayaan3 craft controller ----------------------------------
    def test_spacecraft_controller(self):
        spaceCraft = chandrayaan(0, 0, 0, 'N')
        commands = ['f', 'r', 'u', 'b', 'l']
        x, y, z, direction = spaceCraft.spacecraft_controller(commands)
        self.assertEqual((x, y, z), (0, 1, -1))
        self.assertEqual(direction, 'N')
    
    # Test for turning up/down when current direction N/S 
    def test_turnUpDownInNSDirection(self):
        spaceCraft = chandrayaan(0, 0, 0, 'N')
        spaceCraft.turnUp()
        self.assertEqual(spaceCraft.direction, 'U')
        spaceCraft.turnDown()
        self.assertEqual(spaceCraft.direction, 'D')

     # Test turning left/right when facing U/D directions
    def test_turnLeftRightInUDDirection(self):
        spaceCraft = chandrayaan(0, 0, 0, 'U')
        spaceCraft.turnLeft()
        self.assertEqual(spaceCraft.direction, 'U')
        spaceCraft.turnRight()
        self.assertEqual(spaceCraft.direction, 'U')

if __name__ == "__main__":
    unittest.main()