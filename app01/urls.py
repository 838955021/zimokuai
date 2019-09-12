
from django.urls import path
from .views import *
urlpatterns = [
    path('index/',index),
    path('newslistpic/',newslistpic),
    path('listpic/',listpic),
    path('about/',about),
    path('add/',add),
    path('select/',select),
    path('change/',change),
    path('yiadd/',yiadd),
    path('manytomanyadd/', manytomanyadd),
    path('manytomanysel/',manytomanysel),
    path('manytomanychange/',manytomanychange),
    path('manytomanydelete/',manytomanydelete),
    path('jttest/',jttest),
]