from django.shortcuts import render,redirect
from .models import Home,produce,market,Sell
from .forms import SellForm,HelpForm

# Create your views here.
def homep(request):
    all3 = Home.all_home()
    return render(request,'all/home.html',{"all3":all3})
def prod(request):
    all4 = produce.all_produce()
    return render(request,'all/prod.html',{"all4":all4})
def mkt(request):
    all01 = market.all_mkt()
    return render(request,'farmerz/home.html',{"all01":all01})
def detail(request,slug):
    ail = Home.url11(slug)
    return render(request,'all/detail.html',{"ail":ail})
def sell(request):
    alls = Sell.all_sell()
    current_user = request.user
    if request.method == "POST":
        form = SellForm(request.POST,request.FILES)
        if form.is_valid():
            seeL = form.save(commit=False)
            seeL.save()
    else:
        form = SellForm()
    return render(request,'farmerz/sell.html',{"form":form,"alls":alls})
def help(request):
    current_user = request.user
    if request.method == "POST":
        form = HelpForm(request.POST)
        if form.is_valid():
            elp = form.save(commit=False)
            # elp.name = current_user
            elp.save()
            return redirect('mkt')
    else:
        form = HelpForm()
    return render(request,'farmerz/help.html',{"form":form})
