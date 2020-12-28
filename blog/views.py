from django.shortcuts import render
from django.http import HttpResponse 

posts=[
     {
          'author':'Aadrika Bhargava',
           'title':'Post 1 ',
           'content':'First Post content'
           
     },
     
      {
          'author':'John Doe',
           'title':'Post 2 ',
           'content':'Second Post content'
           
     },
     
     {
          'author':'Ken Ferns',
           'title':'Post 3 ',
           'content':'Third Post content'
           
     }
     
]

def home(request): #handle traffic from homepage of blog , take a request arg
                   # return what we want user to see when we go to this route
    
    context={
         'posts':posts
    }
    return render(request,'blog/home.html',context)

def about(request):
     return render(request,'blog/about.html',{'title':'About'})


# Create your views here.
