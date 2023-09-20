def lineup(x_0, y_0, x_1, y_1):
  x = x_0
  y = y_0
  while(x <= x_1):
    print("(" + str(x) + ", " + str(y) + ")")
    d = f(x_0, y_0, x_1, y_1, x, y)
    midpt = f(x_0, y_0, x_1, y_1, x, y + 0.5)
    if(abs(midpt) > abs(d)):
      x = x + 1
      y = y + 1
    else:
      x = x + 1

def f(x_0, y_0, x_1, y_1, x, y):
  a = y_1 - y_0
  b = -(x_1 - x_0)
  return (x * a + b * y)
