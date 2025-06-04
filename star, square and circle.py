from turtle import *      # use the turtle library
import math
import tkinter as tk
root = tk.Tk()
root.withdraw() #hide the main window / 隐藏主窗口
space = Screen()            # create a turtle space
k = tk.simpledialog.askstring("Input", "What do you want? Star, square or circle?") #k = kind 种类
t = tk.simpledialog.askinteger("Input", f"How many {k} do you want?") #t = time 次数
length = tk.simpledialog.askinteger("Input", "Side length?")

while True:
    if length < 0:
        length = tk.simpledialog.askinteger("Input", "Length can not smaller than 0 :(   Please input the length again ↓")
    else:
        break

angstar = math.radians(18) # angstar means angle of star

""" angstar means angle of star """
alice = Turtle() # give the turtle name
alice.speed(0)
def correction_star_first():
        alice.penup()
        starup = math.tan(angstar)*length/2
        alice.left(90)
        alice.forward(starup)
        alice.left(90)
        alice.forward(length/2)
        alice.right(180)
        alice.pendown()
        
def correction_star_second():
    alice.penup()
    alice.right(18)
    alice.forward(length/math.cos(angstar))
    alice.left(180)
   
def correction_square_first():
    alice.penup()
    alice.left(135)
    alice.forward(math.sin(math.radians(45))*length)
    alice.right(135)
    
def correction_square_second():
    global length
    length = length + 2
    alice.penup()
    alice.goto(-length/2,length/2)
    alice.pendown()
        
def square():
    global length
    correction_square_first()
    for i in range(t):
        for p in range(4):
            alice.forward(length)
            alice.right(90)
        correction_square_second()
        length = length + 2
        
def circle():
    for i in range(t):
        radius = length + i * 10
        alice.penup()
        alice.goto(0, -radius)  
        alice.pendown()
        alice.circle(radius)       
   
def star():
    correction_star_first()
    for i in range(t): # Run the program which is under the sentence for t times, where t is the variable and defined above.
        for p in range(5): 
            alice.forward(length)
            alice.right(144)  # turn by 144 degrees
        correction_star_second()
        correction_star_first()
        alice.right(7)

if k == "star":
    star()
elif k == "square":
    square()
elif k == "circle":
    circle()
else:
    print("We do not have this figure!")
    
input("Press Enter to exit.")
exit()
