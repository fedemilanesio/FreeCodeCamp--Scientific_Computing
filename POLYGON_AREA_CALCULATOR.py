class Rectangle:
    def __init__(self,width,height):
        self.width=width
        self.height=height

    def __repr__(self):
        return f'''{'Rectangle('}{'width='}{self.width}{', height='}{self.height}{')'}'''

    def set_width(self,width):
        self.width=width
        return (width,self.height)

    def set_height(self,height):
        self.height=height
        return (height,self.width)
    def get_area(self):
        area=self.width*self.height
        return area
    def get_perimeter(self):
        perimeter=2*(self.width+self.height)
        return perimeter
    def get_diagonal(self):
        diag=((self.width**2+self.height**2)**0.5)
        return diag

    def get_picture(self):
        stato=False
        pic=''
        for x in range(self.height):
            for j in range(self.width):
                if ((self.height <= 50) and (self.width <= 50)):
                    stato = True
                    pic+='*'
                else:
                    return 'Too big for picture.'
            pic += '\n'
            if stato==False:break
        return pic

    def get_amount_inside(self,instance):
        insta_area=instance.get_area()
        return int(self.get_area()/insta_area)

class Square(Rectangle):
    new_side=0
    def __init__(self,width,*args):
        super().__init__(width,args)
        if not args:
            self.height=self.width
    def __repr__(self):
        return f'''{'Square('}{'side='}{self.height}{')'}'''
    def set_side(self, new_side):
        self.width=new_side
        self.height=new_side
        return (new_side)
    def set_height(self,height):
        return self.set_side(height)
    def set_width(self,width):
        return self.set_side(width)


ret=Rectangle(8,16)
sq=Square(4)
print(sq.set_side(3))
print(sq.set_width(6))
print(sq)
print(sq.get_picture())
