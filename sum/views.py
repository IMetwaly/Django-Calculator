from io import open_code
from django.shortcuts import render
import requests

# Create your views here.
from django.http import HttpResponse
from django.template import Context, loader
from django.shortcuts import render
import sum.appending as a  
import sum.calccode as c


#def calc(request):
    #return HttpResponse("Hi")
    #clearer()
    
    

def ajax_view(request):
    return render(request,"NUM7")

def hey(request):
    return render(request, 'hey.html')


listofnum=[]
x=0
ry=0
y=0

def one(request):
    global listofnum
    global listofnum2
    global x
    global ry
    global y
    listofnum.append(1)
    listofnum2=listofnum
    ry=0
    for i in listofnum:
        print(i)
        y=i
        ry=str(ry)+str(y)
    x=ry[1:]
    return render(request, 'calc.html',{'num':x})
def two(request):
    global listofnum
    global listofnum2
    global x
    global ry
    global y
    listofnum.append(2)
    listofnum2=listofnum
    ry=0
    for i in listofnum:
        print(i)
        y=i
        ry=str(ry)+str(y)
    x=ry[1:]
    return render(request, 'calc.html',{'num':x})
def three(request):
    global listofnum
    global listofnum2
    global x
    global ry
    global y
    listofnum.append(3)
    listofnum2=listofnum
    print(listofnum)
    ry=str(0)
    for i in listofnum:
        print(i)
        y=i
        ry=str(ry)+str(y)
    x=ry[1:]
    return render(request, 'calc.html',{'num':x})
def four(request):
    global listofnum
    global listofnum2
    global x
    global ry
    global y
    listofnum.append(4)
    listofnum2=listofnum
    ry=0
    for i in listofnum:
        print(i)
        y=i
        ry=str(ry)+str(y)
    x=ry[1:]
    return render(request, 'calc.html',{'num':x})
def five(request):
    global listofnum
    global listofnum2
    global x
    global ry
    global y
    listofnum.append(5)
    listofnum2=listofnum
    ry=0
    for i in listofnum:
        print(i)
        y=i
        ry=str(ry)+str(y)
    x=ry[1:]
    return render(request, 'calc.html',{'num':x})
def six(request):
    global listofnum
    global listofnum2
    global x
    global ry
    global y
    listofnum.append(6)
    listofnum2=listofnum
    ry=0
    for i in listofnum:
        print(i)
        y=i
        ry=str(ry)+str(y)
    x=ry[1:]
    return render(request, 'calc.html',{'num':x})
def seven(request):
    global listofnum
    global listofnum2
    global x
    global ry
    global y
    listofnum.append(7)
    listofnum2=listofnum
    ry=0
    for i in listofnum:
        print(i)
        y=i
        ry=str(ry)+str(y)
    x=ry[1:]
    return render(request, 'calc.html',{'num':x})
def eight(request):
    global listofnum
    global listofnum2
    global x
    global ry
    global y
    listofnum.append(8)
    listofnum2=listofnum
    ry=0
    for i in listofnum:
        print(i)
        y=i
        ry=str(ry)+str(y)
    x=ry[1:]
    return render(request, 'calc.html',{'num':x})
def nine(request):
    global listofnum
    global listofnum2
    global x
    global ry
    global y
    listofnum.append(9)
    listofnum2=listofnum
    ry=0
    for i in listofnum:
        print(i)
        y=i
        ry=str(ry)+str(y)
    x=ry[1:]
    return render(request, 'calc.html',{'num':x})
def zero(request):
    global listofnum
    global listofnum2
    global x
    global ry
    global y
    listofnum.append(0)
    listofnum2=listofnum
    ry=0
    for i in listofnum:
        print(i)
        y=i
        ry=str(ry)+str(y)
    x=ry[1:]
    return render(request, 'calc.html',{'num':x})
def plus(request):
    global listofnum
    global listofnum2
    global x
    global ry
    global y
    listofnum.append('+')
    listofnum2=listofnum
    ry=0
    for i in listofnum:
        print(i)
        y=i
        ry=str(ry)+str(y)
    x=ry[1:]
    return render(request, 'calc.html',{'num':x})
def minus(request):
    global listofnum
    global listofnum2
    global x
    global ry
    global y
    listofnum.append('-')
    listofnum2=listofnum
    ry=0
    for i in listofnum:
        print(i)
        y=i
        ry=str(ry)+str(y)
    x=ry[1:]
    return render(request, 'calc.html',{'num':x})
def divide(request):
    global listofnum
    global listofnum2
    global x
    global ry
    global y
    listofnum.append('/')
    listofnum2=listofnum
    ry=0
    for i in listofnum:
        print(i)
        y=i
        ry=str(ry)+str(y)
    x=ry[1:]
    return render(request, 'calc.html',{'num':x})
def times(request):
    global listofnum
    global listofnum2
    global x
    global ry
    global y
    listofnum.append('*')
    listofnum2=listofnum
    ry=0
    for i in listofnum:
        print(i)
        y=i
        ry=str(ry)+str(y)
    x=ry[1:]
    return render(request, 'calc.html',{'num':x})
def decimal(request):
    global listofnum
    global listofnum2
    global x
    global ry
    global y
    listofnum.append('.')
    listofnum2=listofnum
    ry=0
    for i in listofnum:
        print(i)
        y=i
        ry=str(ry)+str(y)
    x=ry[1:]
    return render(request, 'calc.html',{'num':x})
def equals(request):
    r=c.calc(x)
    return render(request, 'calc.html', {'num':r})
def ob(request):
    global listofnum
    global listofnum2
    global x
    global ry
    global y
    listofnum.append('(')
    listofnum2=listofnum
    ry=0
    for i in listofnum:
        print(i)
        y=i
        ry=str(ry)+str(y)
    x=ry[1:]
    return render(request, 'calc.html',{'num':x})
def cb(request):
    global listofnum
    global listofnum2
    global x
    global ry
    global y
    listofnum.append(')')
    listofnum2=listofnum
    ry=0
    for i in listofnum:
        print(i)
        y=i
        ry=str(ry)+str(y)
    x=ry[1:]
    return render(request, 'calc.html',{'num':x})
def Del(request):
    global listofnum
    global listofnum2
    global x
    global ry
    global y
    a=len(listofnum)
    if a>1:
        listofnum=listofnum[:(a-1)]
        listofnum2=listofnum
        ry=0
        for i in listofnum:
            print(i)
            y=i
            ry=str(ry)+str(y)
        x=ry[1:]
        return render(request, 'calc.html',{'num':x})
    else:
        listofnum=[]
        listofnum2=[]
        x=None 
        y=None
        ry=None
        return render(request, 'calc.html',{'num':0})
    
def clearer(request):
    global x, y, listofnum2, listofnum, ry
    listofnum=[]
    listofnum2=[]
    x=None 
    y=None
    ry=None
    return render(request, 'calc.html',{'num':0})
    


def ok(request):
    render(request,'ok.html')

    
    
    


