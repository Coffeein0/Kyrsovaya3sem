from django.shortcuts import render


def index(request):
    return render(request,'main/mainpage.html' )

def about(request):
    return render(request,'main/about.html')

def testpic(request):
    return render(request, 'main/testpic.html')