from django.shortcuts import render


# Create your views here.


def test(request):
    print(13)
    return render(request, "main.html")
