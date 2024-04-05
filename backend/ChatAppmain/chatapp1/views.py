from django.shortcuts import render
from django.shortcuts import get_object_or_404  # Added import
from .models import Room, Message

def rooms(request):
    rooms = Room.objects.all()
    return render(request, "Room.html", {'rooms': rooms})


def room(request, slug):
    room = get_object_or_404(Room, slug=slug)
    room_name = room.name
    messages=Message.objects.filter(room=Room.objects.get(slug=slug))
    context = {"slug": slug, "room_name": room_name, "messages": messages}
    return render(request, "inside.html", context)

