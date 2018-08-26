import turtle
def fractal(size, depth=0):
    if depth <= 0:
        forward(size)                          #直線
    else:
        fractal(size/3, depth-1); left(60)     #1/3の長さでフラクタル描画、左に60度向く
        fractal(size/3, depth-1); left(-120)   #1/3の長さでフラクタル描画、右に120度向く
        fractal(size/3, depth-1); left(60)     #1/3の長さでフラクタル描画、左に60度向く
        fractal(size/3, depth-1)               #1/3の長さでフラクタル描画
    
    reset(); fractal(200)
    reset(); fractal(200, 1)
    reset(); fractal(200, 2)
    reset(); fractal(200, 3)