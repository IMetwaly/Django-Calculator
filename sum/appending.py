from django.http import request
import sum.views as sv
listofnum=[]
x=0
ry=0
y=0
def appending(num):
    global listofnum
    global listofnum2
    global x
    global ry
    global y
    listofnum.append(num)
    listofnum2=listofnum
    ry=0
    for i in listofnum:
        print(i)
        y=i
        i+=1
        ry=str(ry)+str(y)
    x=ry[1:]
    sv.diplaying(request)


def clearer():
    global x, y, listofnum2, listofnum, ry
    listofnum=[]
    listofnum2=[]
    x=None 
    y=None
    ry=None