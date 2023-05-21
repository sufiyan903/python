v=float(input("enter the wind speed in kmph:"))
t=float(input("enter the temperature in celsius:"))
c=(13.12+(0.6215*t)-(11.37*(v**0.16))+(0.3956*t*(v**0.16)))
print("the wind chill index is:",c)

