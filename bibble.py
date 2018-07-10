from turtle import *
color('blue', 'white')
begin_fill()
while True:
    forward(90)
    left(65)
    if abs(pos()) < 2:
        break
end_fill()
done()
