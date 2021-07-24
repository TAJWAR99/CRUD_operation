from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('user/',views.user,name='user'),
    path('login/',views.loginPage,name='login'),
    path('logout/',views.logoutPage,name='logout'),
    path('register/',views.register,name='register'),
    path('user/',views.user,name='user'),
    path('delete/<str:pk>/',views.deleteUser,name="delete"),
    path('update/<str:pk>/',views.updateUser,name="update")
]
