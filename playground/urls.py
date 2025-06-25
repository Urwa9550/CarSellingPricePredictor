from django.urls import path
from . import views

# URLConfig
urlpatterns = [
    
    # we just need to pass reference of say_hello function here [ no need to pass function like this say_hello() ]
    # always end a route with forward slash
    path('home/', views.index_func, name='Predict Price'),
    path('hello/', views.say_hello, name='hellopage')
]