from microbit import *

x = 2
y = 2
xb = 2
yb = 2
p = 0

print (button_a.was_pressed())
print (button_b.was_pressed())
display.clear()

while True:
    x= (x)%5
    y= (y)%5
    display.set_pixel(x, y, 3)
    display.set_pixel(xb, yb, 1)
    sleep(350)
    if button_a.was_pressed() >= 1:
        xb=x
        yb=y
        y += -abs(p-2)+1
        x += abs(p - 1) - 1
        p= (p+1)%4
        display.clear()
    elif button_b.was_pressed() >= 1:
        xb=x
        yb=y
        y += abs(p-2) - 1
        x += -abs(p - 1)+1
        p= (p-1)%4
        display.clear()
    else:
        xb=x
        yb=y
        y += abs(p-1) - 1
        x += abs(p - 2) - 1
        display.clear()