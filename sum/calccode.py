from django.http import request
import sum.views as sv
def calc(l):
    c=eval(l)
    ans=c
    print('ans=',ans)
    sv.listofnum.clear()
    sv.listofnum.append(ans)
    return c
    



