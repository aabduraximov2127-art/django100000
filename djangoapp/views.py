from django.shortcuts import render, redirect, get_object_or_404
from django.urls.base import reverse_lazy
from . import models 
from django.utils.text import slugify
import uuid
from .models import User
from . import forms
from django.views.generic import CreateView,ListView,UpdateView,DeleteView,DetailView


class UserListView(ListView):
    model=models.User
    template_name='index.html'
    context_object_name='users'
    
class UserCreate(CreateView):
    model=models.User
    template_name='user_create.html'
    form_class=forms.UserForm
    success_url=reverse_lazy('user_list')



class UserDetail(DetailView):
    model = models.User
    template_name = 'user.html'
    context_object_name = 'user'
    slug_field='slug'
    slug_url_kwarg='slug'
    
class UserUpdate(UpdateView):
    model=models.User
    template_name = 'user_update.html'
    form_class=forms.UserForm
    context_object_name = 'form'
    slug_field='slug'
    slug_url_kwarg='slug'
    success_url=reverse_lazy('user_list')

class UserDelete(DeleteView):
    model = models.User
    template_name = 'user_delete.html'
    context_object_name = 'user'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    success_url = reverse_lazy('user_list')


        























# -------------------------------------------
# def mypro(request):
#     users = models.User.objects.all()
#     return render(request, "index.html", {"users": users})


# def user_view(request, slug):
#     user =models.User.objects.filter(slug=slug)
#     return render(request, "user.html", {"user": user})


# #CREATE 
# from django.shortcuts import render, redirect
# from .forms import UserForm

# def user_create(request):
#     if request.method == "POST":
#         form = UserForm(request.POST, request.FILES)
#         if form.is_valid():
#             user = form.save(commit=False)
#             user.save()
#             return redirect('user_list')


#     return render(request, "user_create.html", {"form": form})


# #UPDATE 
# def user_update(request, slug):
#     user = get_object_or_404(User, slug=slug)
#     form=forms.UserForm(request.POST,request.FILES,instance=user)
#     if request.POST:
#         if form.is_valid():
#             form.save()
#         return redirect('user_list')
   
#     return render(request, "user_update.html", {"form": form})
    
    
# # delete

# def user_delete(request, slug):
#     user = get_object_or_404(User, slug=slug)

#     if request.method == "POST":
#         user.delete()
#         return redirect("user_list")

#     return render(request, "user_delete.html", {"user": user})