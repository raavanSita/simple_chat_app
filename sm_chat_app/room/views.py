from django.shortcuts import render,redirect
from .models import Message ,Room
from django.http import HttpResponse,JsonResponse
# Create your views here.
def home (request):
    return render(request,'cred.html')

def room (request,room):
    username = request.GET.get('username')
    room_details = Room.objects.get(name=room)
    context={'username':username,'room':room,
    'room_details':room_details}
    return render(request,'index.html',context) 

def checkView(request):
    room = request.POST['room_name']
    username = request.POST['username']

    if Room.objects.filter(name=room).exists():
        return redirect('/'+room+'/?username='+username)
    else:
        new_room=Room.objects.create(name=room)
        new_room.save()
        return redirect('/'+room+'/?username='+username)



def send(request):
    message=request.POST['message']
    room_id = request.POST['room_id']
    username = request.POST['username']

    new_msg=Message.objects.create(value=message,user=username,room=room_id)
    new_msg.save()
    print('httpp')
    return  HttpResponse('message sent')


def getMessages(request,room):
    room_details= Room.objects.get(name=room)
    print("details",room_details)
    message = Message.objects.filter(room=room_details.id)
    print("message",message)
    return JsonResponse({"message":list(message.values())})


