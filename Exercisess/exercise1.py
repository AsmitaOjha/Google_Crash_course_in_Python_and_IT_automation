#Write a function called calculate_area that takes base and height as an input and returns and area of a triangle. Equation of an area of a triangle is,
# area = (1/2)*base*height
def calculate_area(base,height):
    area=(1/2)*base*height
    print(f"Area of triangle with base:{base} and height:{height} is:",area)

calculate_area(8,3)
#Modify above function to take third parameter shape type. It can be either "triangle" or "rectangle". Based on shape type it will calculate area. Equation of rectangle's area is,
#rectangle area=length*width

        
def calculate_area(base,height,shape):
    if shape.lower()=='triangle':
        area=(1/2)*base*height
        return area
    elif shape.lower()=='rectangle':
        area=base*height
        return area
print(f"Area of triangle is {calculate_area(8, 9, 'triangle')}")

#If no shape is supplied then it should take triangle as a default shape
def calculate_area(base,height,shape='triangle'):
    if shape.lower()=='triangle':
        area=(1/2)*base*height
        return area
    elif shape.lower()=='rectangle':
        area=base*height
        return area
print(f"Area of is {calculate_area(8, 5,'Rectangle')}")