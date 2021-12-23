class rectangle():
    def __init__(self , l , w):
        self.width = w
        self.length = l

    def rectanglearea(self):
        return self.length*self.width

l = input("please input the length of the rectangle: ")
w = input("please input the width of the rectangle: ")
l=int(l)
w=int(w)
new_rectangle = rectangle(l,w)


print("the area of the rectangle is: " ,new_rectangle.rectanglearea())