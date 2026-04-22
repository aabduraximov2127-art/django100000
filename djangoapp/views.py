from django.shortcuts import render
from . import models


# Create your views here.
def mypro(request):

    users=models.User.objects.all()
    return render(request,'index.html',context={'users':users})

def user_view(request, user_id):
    user = models.User.objects.get(pk=user_id)
    return render(request, 'user.html', {'user': user})