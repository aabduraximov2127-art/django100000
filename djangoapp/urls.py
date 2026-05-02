from django.urls import path
from . import views
    
urlpatterns = [
    path("users/", views.UserListView.as_view(), name="user_list"),
    path("create/", views.user_create, name="user_create"),
    path('user/<slug:slug>/update/', views.user_update, name='user_update'),
    path('user/delete/<int:id>/', views.user_delete, name='user_delete'),
    path('user/<slug:slug>/', views.UserDetail.as_view(), name='user_view'),
]