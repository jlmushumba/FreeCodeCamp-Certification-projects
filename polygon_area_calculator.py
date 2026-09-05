class Rectangle:
    def __init__(self,width, height):
        if not isinstance(width, (float, int)) or isinstance(width, bool):
            return
        if not isinstance(height, (float, int)) or isinstance(height, bool):
                    return
        if width <= 0 or height <= 0:
            print("Width or height must be a positive value different of 0")
            return
        

        self._width = width
        self._height = height
    
    def set_width(self, new_width):
        self._width = new_width
    
    def set_height(self, new_height):
        self._height = new_height


    def get_area(self):
        return self._width * self._height

    def get_perimeter(self):
        return 2 * (self._width + self._height)

    def get_diagonal(self):
        return (self._width ** 2 + self._height ** 2) ** 0.5
    

    def get_picture(self):
        if self._height > 50 or self._width > 50:
            return "Too big for picture."
        else:
            return f"{self._width * "*"}\n" * self._height
        
    def get_amount_inside(self, object):
        obj_width = object._width
        obj_height = object._height

        vertical_fit = self._height // obj_height
        horizontal_fit = self._width // obj_width
        total_fits = vertical_fit * horizontal_fit
        return total_fits
        
    def __str__(self):
        return f"Rectangle(width={self._width}, height={self._height})"


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)
    def set_width(self, new_side):
        self._width = new_side
        self._height = new_side
        

    def set_height(self, new_side):
        self._width = new_side
        self._height = new_side

    def set_side(self, new_side):
        self._width = new_side
        self._height = new_side

    def __str__(self):
        return f"Square(side={self._width})"
    

rect = Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))
