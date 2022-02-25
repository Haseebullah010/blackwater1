from django.shortcuts import render

# Create your views here.

def index(request):

    return render(request,"Client/index.html")

def Dispute_Details(request):

    return render(request,"Client/dispute_detail.html")


def chat(request):

    return render(request,"Client/chat.html")


def CreditInfo(request):

    return render(request,"Client/credit_info.html")


def Resources(request):

    return render(request,"Client/resources.html")


def Setting(request):

    return render(request,"Client/setting.html")