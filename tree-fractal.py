import math
import turtle

class Coordinate:
    def __init__ (self, x, y):
        self.x = x
        self.y = y


class Branch:
    def __init__ (self, root, length, weight, angle, color):
        self.root = root
        self.length = length
        self.weight = weight
        self.angle = angle
        self.color = color

    def growUp(self, pen):
        pen.setposition(self.root.x, self.root.y)
        pen.pendown()
        pen.pensize(self.weight)
        pen.color(self.color)
        pen.setheading(self.angle)
        pen.forward(self.length)
        pen.penup()


class Tree:
    pen = turtle.Turtle()

    def __init__ (self, root):
        self.root = root
        self.pen.speed("fastest")
        self.pen.penup()
        self.pen.setposition(root.x, root.y)
        self.pen.pendown()

    def done(self):
        self.pen.hideturtle()

    def growUp(self, branch, trunkHeight):
        if trunkHeight == 0:
            return
        branch.growUp(self.pen)
        newRoot = self.pen.position()

        currentAngle = self.pen.heading()

        leftBranch = Branch(Coordinate(newRoot[0], newRoot[1]), branch.length - 6.2, 
                    branch.weight - 1, currentAngle - 20, branchColor[trunkHeight])
        self.growUp(leftBranch, trunkHeight - 1)

        rightBranch = Branch(Coordinate(newRoot[0], newRoot[1]), branch.length - 6.2, 
                    branch.weight - 1, currentAngle + 20, branchColor[trunkHeight])
        self.growUp(rightBranch, trunkHeight - 1)

        

# Array color
branchColor = ["#E14B42", "#7c4743", "#7A6458", "#D1E883", 
            "#44E440", "#4FEDB9", "#56F1F2", "#42C3E9", "#4869EA", 
            "#BA82F0", "#E071E7", "#E75BC7"]

# Root properties
rootPoint = Coordinate(0, -200)
rootHeight = 70
rootWeight = 12
rootAngle = 90
rootColor = branchColor[0]
trunkHeight = 11

tree = Tree(rootPoint)
tree.growUp(Branch(rootPoint, rootHeight, rootWeight, rootAngle, rootColor), trunkHeight)
tree.done()

turtle.done()