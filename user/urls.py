from django.urls.conf import include
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('login', views.login),
    path('form',views.form),
    path('update/<int:id>',views.update),
    path('log',views.login,name="log_user"),
    path('home',views.home,name="home"),
    path('logout',views.logout,name="logout_user"),
    path('profile',views.profile,name="profile"),
    # path('chpwd',views.chpwd,name="chpwd")
]
