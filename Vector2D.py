class Vector2D:
    def __init__(self, x, y):
        self.x = x;
        self.y = y;

    def __eq__(self, otroVector):
        return self.x == otroVector.x and self.y == otroVector.y;
