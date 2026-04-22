from django.shortcuts import render
from . import models


# Create your views here.
def mypro(request):

    users=models.User.objects.all()
    return render(request,'index.html',context={'users':users}) 