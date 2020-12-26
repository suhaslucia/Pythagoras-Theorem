from math import sqrt

print(" ----------Pythagoras Theorem to Find the sides of the Triangle---------- ")

base = int(input("Enter the base of the Triangle: "))
height = int(input("Enter the height of the Triangle: "))
hypotenuse = int(input("Enter the hypotenuse of the Triangle: "))

if hypotenuse == 0:
    b = base ** 2
    h = height ** 2
    hyp = b + h
    result = sqrt(hyp)
    print(f'\n Hypotenuse of Triangle is {result}')
elif height == 0:
    b = base ** 2
    hyp = hypotenuse ** 2
    h = hyp - b
    result = sqrt(h)
    print(f'\n Height of Triangle is {result}')
else:
    h = height ** 2
    hyp = hypotenuse ** 2
    b = hyp - h
    result = sqrt(b)
    print(f'\n Base of Triangle is {result}')
