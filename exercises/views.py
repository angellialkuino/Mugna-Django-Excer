from django.shortcuts import render
from django.http import HttpResponse, Http404
from datetime import datetime
from django.shortcuts import render

# Create your views here.


def mathed2(request, num1, num2):
    try:
        num1 = int(num1)
        num2 = int(num2)
        if num2 == 0:
            raise Http404()
    except ValueError:
        raise Http404()

    return render(
        request,
        "math.html",
        {"sum": num1+num2, "diff": num1-num2, "prod": num1*num2, "quo": num1/num2}
    )

def mathed3(request, num1, num2, num3):
    try:
        num1 = int(num1)
        num2 = int(num2)
        num3 = int(num3)
        if num2 == 0 or num3 ==0:
            raise Http404()
    except ValueError:
        raise Http404()
    return render(
        request,
        "math.html",
        {"sum": num1+num2+num3, "diff": num1-num2-num3, "prod": num1*num2*num3, "quo": (num1/num2)/num3}
    )

def date_format(request, year, month, day):
    try:
        year = int(year)
        month = int(month)
        day = int(day)
        datetime(year,month,day)        
    except ValueError:
        return render(
        request,
        "date_format.html",
        {"status": "Invalid"}
        )

    return render(
        request,
        "date_format.html",
        {"status": "Valid"}
    )
