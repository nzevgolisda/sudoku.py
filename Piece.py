
class Piece:
    def __init__(self, value, square):
        self.value = value
        self.square = square
        self.turn = 1
    ##def __str__(self):
    ##    if self.value == 0:
    ##        return str('  ')+' |'
    ##    else:
    ##        return ' '+str(self.value)+' |'
             
    def __str__(self):
        if self.value == 0:
            return ' '+str(self.square)+' | '
        else:
            return '  '+str(self.value)+' | '