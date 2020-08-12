from django.urls import path
from . import views


app_name='authentication'
urlpatterns=[
path('',views.index,name='index'),
path('auth',views.auth,name='auth'),
path('logout',views.logout,name='logout'),
path('register/',views.register,name='register'),
path('submit',views.submitDetails,name='submit')

]
