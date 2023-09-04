from . import views
from django.urls import path

urlpatterns = [
    path('', views.homepage, name='homepage'),
    # path('districts/', views.district_list, name='district_list'),
    path('redirect/<int:district_id>/', views.redirect_to_wikipedia, name='redirect_to_wikipedia'),

    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),



    path('button/',views.button,name='button'),
    path('form/',views.form,name='form'),


    ]



