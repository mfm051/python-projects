# Part of "Scientific Computing with Python Certification" on FreeCodeCamp
# Creates a class "Rectangle" with methods to get the area, perimeter, and a graphic representation on terminal
# Creates a subclass "Square" based on Rectangle


class Rectangle:
    def __init__(self,width=0,height=0):
        self.width = width
        self.height = height

    def set_width(self,new_width):
        self.width = new_width

    def set_height(self,new_height):
        self.height = new_height

    def get_area(self):
        self.area = self.width * self.height
        return self.area

    def get_perimeter(self):
        self.perimeter = 2*self.width + 2*self.height
        return(self.perimeter)

    def get_diagonal(self):
        self.diagonal = (self.width**2 + self.height**2)**.5
        return self.diagonal

    def get_picture(self):
        self.pic = ''
        for line in range(self.height):
            self.pic = self.pic + '*'*self.width + '\n'
        if self.width > 50 or self.height > 50:
            self.pic = 'Too big for picture.'
        return self.pic

    def get_amount_inside(self,shape):
        self.times = self.get_area()//shape.get_area()
        return self.times

    def __str__(self):
        self.rg = f'Rectangle(width={self.width}, height={self.height})'
        return self.rg

class Square(Rectangle):
    def __init__(self,side=0):
        self.side = side
        self.width = side
        self.height = side

    def set_side(self,new_side):
        self.side = new_side
        self.width = new_side
        self.height = new_side

    def set_width(self,new_side):
        self.set_side(new_side)

    def set_height(self,new_side):
        self.set_side(new_side)

    def __str__(self):
        self.rg = f'Square(side={self.side})'
        return self.rg
