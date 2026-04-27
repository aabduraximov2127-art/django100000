from django.shortcuts import render
from . import models


# Create your views here.
def mypro(request):

    users=models.User.objects.all()
    return render(request,'index.html',context={'users':users})

def user_view(request, slug):
    user = models.User.objects.get(slug=slug)
    return render(request, 'user.html', {'user': user})