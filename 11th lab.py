i=0
def monkey_go_box(x,y):
    global i
    i= i+1
    print("step :",i,"monkey slave",x,"go to"+y)
def monkey_move_box(x,y):
    global i
    i= i+1
    print("step :",i,"monkey take the box from",x,"delivers it to"+y)
def monkey_on_box(x,y):
    global i
    i=i+1
    print("step :",i,"monkey climbs up the box")
def monkey_get_banana(x,y):
    global i
    i=i+1
    print("step :",i,"monkey picked up a banana")

import sys
codeIn=sys.stdin.read()
codeInList=codeIn.split()
monkey=codeInList[o]
banana=codeInList[1]
box=codeInList[2]
print("the steps are as follows:")
monkey_go_box(monkey,box)
monkey_move_box(box,banana)
monkey_on_box()
monkey_get_banana()