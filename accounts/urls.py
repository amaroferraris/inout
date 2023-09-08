from django.urls import path
from . import views

urlpatterns = [

    path('register/', views.registerUser, name="register"),
    path('login/', views.loginUser, name="login"),
    path('logout/', views.logoutUser, name="logout"),

    path('home', views.home, name="home"),
    path('create_in/', views.createIn, name="create_in"),
    path('create_out/', views.createOut, name="create_out"),
    
    path('update_in/<str:pk>/', views.updateIn, name="update_in"),
    path('delete_in/<str:pk>/', views.deleteIn, name="delete_in"),

    path('update_out/<str:pk>/', views.updateOut, name="update_out"),
    path('delete_out/<str:pk>/', views.deleteOut, name="delete_out"),
    
    path('', views.userPage, name="user"),
    # path('user/<str:pk>/', views.userPage, name="user"),

    path('admin/', views.adminPage, name="admin"),

]