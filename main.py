from giacpy import giac

x, y = giac('x,y')
type(x)
a = (x + 2 * y).cos().texpand()
print(a)
