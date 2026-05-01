from django.urls import path
from . import views
    
urlpatterns = [
    path("users/", views.UserListView.as_view(), name="user_list"),
    path("create/", views.UserCreate.as_view(), name="user_create"),
    path('user/<slug:slug>/update/', views.UserUpdate.as_view(), name='user_update'),
    path('user/<slug:slug>/delete/', views.UserDelete.as_view(), name='user_delete'),
    path('user/<slug:slug>/', views.UserDetail.as_view(), name='user_view'),
]