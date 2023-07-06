#def sayhello():
 #   print("hello")
#sayhello()

#def add (a,b):
 #   print(a + b)
#add(5,6)

#imp={"fass":122,"dd":45}
#def update(imp):
 #   newimp={"ggg":54}
  #  imp.update(newimp)
   # print(imp)
#update(imp)
#print(imp)

#imp={"fass":122,"dd":45}
#def update(imp):
 #   imp={"ggg":54}
  #  imp.update(imp)
   # print(imp)
#update(imp)
#print(imp)

#l={5,6,7,8}
#l.add(9)
#print(l)




import turtle
def drawsquare():
    window=turtle.Screen()
    window.bgcolor("red")
    p=turtle.Turtle()
    p.shape("turtle")
    p.color("yellow")

    p.forward(100)
    p.right(90)
    p.forward(100)
    p.right(90)
    p.forward(100)
    p.right(90)
    p.forward(100)
    p.right(90)
    window.exitonclick()
    drawsquare()
