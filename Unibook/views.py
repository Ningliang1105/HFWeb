from django.shortcuts import render
#from .models import Post
from django.http import HttpResponse
# Create your views here.
from.models import Book
#def index(request):
	#post_list = Post.objects.all()
	#return render(request, 'Unibook/index.html', context={'post_list':post_list})
import datetime

def index(request):
	Date = datetime.datetime.now()
	return render(request,"index.html",context = {'datetime':Date})
def donation(request):
	book_list = Book.objects.all().order_by('-post_time')
	Date = datetime.datetime.now()
	return render(request,"donation.html",context = {'book_list': book_list, 'datetime': Date})
