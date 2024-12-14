from django.shortcuts import render,redirect

# Create your views here.
def index(request):
    if request.method =="POST":
        room_name=request.POST['room_name']
        return redirect('room',room=room_name)
    else:
        return render(request,'index.html')
def room(request,room):
    return render(request,'room.html',{
        'room':room
    })