x, y = input('Enter x,y cordinates: ').split()
x = int(x)
y = int(y)
if x == 0 and y == 0:
  print("The point is at the Origin.")
elif x > 0 and y > 0:
  print("in the first quadrant .")
elif x < 0 and y > 0:
  print("The point is in quadrant 2.")
elif x < 0 and y < 0:
  print("The point is in quadrant 3.")
elif x > 0 and y < 0:
  print("The point is in quadrant 4.")
else:
  print("Error!") 
