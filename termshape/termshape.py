def plot(canvas):
    res = ''
    for row in [' '.join(row) for row in canvas]:
        res += row + '\n'
    return res

def make_shape(list_x, list_y, eqs, ch='*'):
    canvas = [[' ' for _ in list_x] for _ in list_y]

    #calc min_x, min_y for range with negative values
    min_x = abs(min(list_x))
    min_y = abs(min(list_y))
    
    for x in list_x:
        index_x = x+min_x
        for y in list_y:
            index_y = len(list_y) - (y+min_y) - 1
          
            for eq in eqs:
                if eval(eq):
                    canvas[index_y][index_x] = ch

    return plot(canvas)

def get_square(size, ch='*'):
    x = y = range(size)
    eq = ["x==0", "x=="+str(size-1), "y==0", "y=="+str(size-1)]
    return make_shape(x,y,eq,ch)
    
def get_rectangle(w,h,ch='*'):
    x = range(w)
    y = range(h)
    eq = ["x==0","x=="+str(w-1),"y==0","y=="+str(h-1)]
    return make_shape(x,y,eq,ch)

def get_triangular(h,ch='*'):
    x = y = range(h)
    eq = ["x==0","x=="+str(h)+"-y-1","y==0"]
    return make_shape(x,y,eq,ch)

def get_circle(r,ch='*',t=0.05):
    size=r+1
    x = y = range(-size,size)

    #TODO calc best t
    eq = ["x**2+y**2>"+str(r**2-t*(r**2)) + " and x**2+y**2<"+str(r**2+t*(r**2))]
    return make_shape(x,y,eq,ch)