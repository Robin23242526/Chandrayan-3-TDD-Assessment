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
    
    def turnDown(self):
            self.direction = 'D'
            self.data.append(self.direction)
    
    def turnLeft(self):
        if self.direction in ['U','D']:
            if self.data[-2] == 'N':
                self.direction = 'W'
            elif self.data[-2] == 'S':
               self.direction = 'E'
            elif self.data[-2] == 'E':
                self.direction = 'N'
            elif self.data[-2] == 'W':
               self.direction = 'S'
        else:
            if self.direction == 'N':
                self.direction = 'W'
            elif self.direction == 'S':
               self.direction = 'E'
            elif self.direction == 'E':
                self.direction = 'N'
            elif self.direction == 'W':
               self.direction = 'S'
        self.data.append(self.direction)
    
    def turnRight(self):
        if self.direction in ['U','D']:
            if self.data[-2] == 'E':
              self.direction = 'S'
            elif self.data[-2] == 'N':
               self.direction = 'E'
            elif self.data[-2] == 'S':
               self.direction = 'W'
            elif self.data[-2] == 'W':
                self.direction = 'N'
        else:
            if self.direction == 'N':
                self.direction = 'E'
            elif self.direction == 'S':
                self.direction = 'W'
            elif self.direction == 'E':
               self.direction = 'S'
            elif self.direction == 'W':
               self.direction = 'N'
        self.data.append(self.direction)
