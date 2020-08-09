from django.urls import path
from . import views


app_name='register'
urlpatterns=[
path('index',views.index,name='index'),
path('submit',views.submitDetails,name='submit')
]
