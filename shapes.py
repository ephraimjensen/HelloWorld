# Python
import math
# This will help you to calculate a shape's area.

def calculateAreaRectangle(width, height):
    area=width * height
    return area
def calculateAreaTriangle(base, height):
    area = .5 * base * height
    return area
def calculate_Circle_Area(radius):
    area = radius * math.pi * radius
    return area
def main():
    print("This is my shapes program")
    rectangleArea = calculateAreaRectangle(10,20)
    print(f"The area of the rectangle is : {rectangleArea}")

    triangleArea = calculateAreaTriangle(40,20)
    print(f"The area of the Triangle is : {triangleArea}")

    circle_area = calculate_Circle_Area(10)
    print(f"The area of the Circle is : {circle_area}")





main()