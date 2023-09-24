def circle_calc(r):
    r=float(r)
    area=3.143*(r**2)
    circumference=2*3.143*r
    diameter=2*r
    print(f'''Area={area},
Circumference={circumference},
diameter={diameter}''')
    return
redius=input("Write down the redius of the circle:")
circle_calc(redius)


