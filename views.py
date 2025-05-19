from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    if request.method == "POST":
        num = float(request.POST.get("num", 0))  # Default value 0 if 'num' is not provided
        if request.POST.get("sqr"):
            if num > 0:
                res = num * num
                res = round(res, 2)
                msg = f"Your number {num} squared is {res}"
            else:
                msg = "Invalid input: Number must be greater than 0"
        elif request.POST.get("cub"):
            if num > 0:
                res = num * num * num
                res = round(res, 2)
                msg = f"Your number {num} cubed is {res}"
            else:
                msg = "Invalid input: Number must be greater than 0"
        elif request.POST.get("sqrt"):
            if num >= 0:
                res = num ** 0.5
                res = round(res, 2)
                msg = f"Your number {num} square root is {res}"
            else:
                msg = "Invalid input: Number must be non-negative"
        else:
            msg = "Invalid operation"

        return render(request, "home.html", {"msg": msg})

    # If the request method is not POST, render the empty form
    return render(request, "home.html")
