class Rectangle():
    def __init__(self, min_x=0, min_y=0, max_x=0, max_y=0) -> None:
        self.min_x = min_x
        self.min_y = min_y
        self.max_x = max_x
        self.max_y = max_y
    
    def area(self):
        return (self.max_x-self.min_x)*(self.max_y - self.min_y) if self.min_x< self.max_x and self.min_y < self.max_y else 0

def intersection_area(rec1: Rectangle,rec2:Rectangle):
    intersection = Rectangle()
    intersection.min_x = max(rec1.min_x, rec2.min_x)
    intersection.min_y = max(rec1.min_y, rec2.min_y)
    intersection.max_x = min(rec1.max_x, rec2.max_x)
    intersection.max_y = min(rec1.max_y, rec2.max_y)

    return intersection.area()

rec1 = Rectangle(0,0,3,2)
rec2 = Rectangle(1,1,3,3)

print(intersection_area(rec1,rec2))
