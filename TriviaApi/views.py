from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect


# Create your views here.
from TriviaApi.models import TriviaModel

Name=""
Player_Name=""
def index(request):
     return render(request,'index.html')

def FirstPage(request):
     if request.method == "POST":
          if request.POST.get('Name'):
               global Name
               Name= request.POST.get('Name')
               return redirect('/SecondPage')

     return render(request, 'FirstPage.html')

def SecondPage(request):
     if request.method == "POST":
          global Player_Name
          Player_Name = request.POST.get('cricketer')
          return redirect('/ThirdPage')
     return render(request,'SecondPage.html')


def ThirdPage(request):
     if request.method == "POST":
          global  Name,Player_Name
          post = TriviaModel()
          post.player_name = Player_Name
          post.Name = Name
          post.flag_color = request.POST.getlist('Color[]')
          post.save()
          Name=""
          Player_Name=""
          return redirect('/SummaryPage')
     return render(request, 'ThirdPage.html')


def SummaryPage(request):
     return render(request, 'SummaryPage.html')

def HistoryPage(request):
    Trivia = TriviaModel.objects.all()
    return render(request,"HistoryPage.html",{'data':Trivia})