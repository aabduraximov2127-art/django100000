from django.urls import path
from . import views

urlpatterns = [
    path("",views.mypro,name='user_list'),
    path("user/<int:user_id>/", views.user_view, name='user_view')
]