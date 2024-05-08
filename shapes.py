# Python
import math
# This will help you to calculate a shape's area.
def calculateCircleArea(radius):
    area = math.pi * radius * radius
    return area
def calculateAreaRectangle(width, height):
    area=width * height
    return area
def main():
    print("This is my shapes program")
    circleArea = calculateCircleArea(20)
    print(f"The area of the circle is : {circleArea}")
    rectangleArea = calculateAreaRectangle(10,20)
    print(f"The area of the rectangle is : {rectangleArea}")

main()