from django.shortcuts import render, redirect, get_object_or_404
from .models import Board
from django.utils import timezone
from datetime import datetime

# Create your views here.
def home(request):
    return render(request,'home.html')

def check(request):
    boards=Board.objects
    return render(request,'check.html',{'boards':boards})

def count(request):
    full_text=request.GET['fulltext']
    word_list=full_text.split()
    word_dictionary={}
    for word in word_list:
        if word in word_dictionary:
            # Increase
            word_dictionary[word] += 1
        else:
            # add to the dictionary
            word_dictionary[word] = 1
    return render(request,"count.html",{'fulltext':full_text,'total':len(word_list),'dictionary':word_dictionary.items()})

def write(request):
    return render(request,'write.html')

def send(request):
    board = Board()
    board.title = request.GET['title']
    board.body = request.GET['body']
    board.pub_date = timezone.datetime.now()
    board.save()
    return redirect('check')

def detail(request,board_id):
    board_detail = get_object_or_404(Board, pk=board_id)
    return render(request,'detail.html',{"boardNumb":board_detail})