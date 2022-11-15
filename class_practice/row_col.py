class Sep:
    def __init__(self, row, col):
        self.row = row
        self.col = col
    def get_width(self):
        return (self.row * self.col)/2
    def get_circle_width(self):
        return (self.row/2)**2 * 3.14