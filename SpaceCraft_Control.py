class chandrayaan3:
    def __init__(self, startx, starty, startz, startDirection):
        self.x = startx
        self.y = starty
        self.z = startz
        self.direction = startDirection
        self.data = [startDirection,startDirection]

    def moveForward(self):
        if self.direction == 'E':
            self.x += 1
        elif self.direction == 'W':
            self.x -= 1
        elif self.direction == 'N':
            self.y += 1
        elif self.direction == 'S':
            self.y -= 1
        elif self.direction == 'U':
            self.z += 1
        elif self.direction == 'D':
            self.z -= 1

    def moveBackward(self):
        if self.direction == 'E':
            self.x -= 1
        elif self.direction == 'W':
            self.x += 1
        elif self.direction == 'N':
            self.y -= 1
        elif self.direction == 'S':
            self.y += 1
        elif self.direction == 'U':
            self.z -= 1
        elif self.direction == 'D':
            self.z += 1

    def turnUp(self):
            self.direction = 'U'
            self.data.append(self.direction)