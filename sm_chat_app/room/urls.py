from  django.urls import  path
from .views import room,home,checkView,send,getMessages

urlpatterns = [
    path('', home, name = 'home'),
    path('<str:room>/', room, name = 'room'),
    path('checkView',checkView,name='checkView'),
    path('send',send,name='send'),
    path('getMessages/<str:room>/', getMessages, name = 'getMessages'),

]