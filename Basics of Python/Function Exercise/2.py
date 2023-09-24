def calculate_area(l,w,shape="triangle"):
    if shape=="triangle":
        area= (1/2)*l*w
    elif shape=="rectangle":
        area=l*w
    else:
        print("Error! Area Not found.")
    return area
area_of_rectangle=calculate_area(4,6,"rectangle")
area_of_triangle=calculate_area(4,6)
print("Area of triangle=",area_of_triangle)
print("Area of rectangle=",area_of_rectangle)
