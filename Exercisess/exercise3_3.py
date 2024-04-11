#Write circle_calc() function that takes radius of a circle as an input from user and
#  then it calculates and returns area, circumference and diameter. 
# You should get these values in your main program by calling circle_calc function and then print them

def circle_calc(radius):
    area= 3.14*radius**2
    circumference=2*3.14*radius
    diameter=2*radius
    return area,circumference,diameter
def main():
    radius=float(input("Enter the radius of circle: "))
    A,C,D=circle_calc(radius)
    print(f"Area of cirlce : {A}\nCircumference of circle: {C}\nDiameter of Circle: {D}")


if __name__=='__main__':
    main()

#solution
# import math

# def circle_calc(radius):
#     area=math.pi*(radius**2)
#     circumference=2*math.pi*radius
#     diameter=2*radius
#     return area, circumference,diameter

# if __name__=="__main__":
#     r=input("Enter a radius:")
#     r=float(r)
#     area, c, d = circle_calc(r)
#     print(f"area {area}, circumference {c}, diameter {d}")