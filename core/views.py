from django.shortcuts import render
from .models import Message
from .forms import MessageForm
from django.http import JsonResponse
from django.contrib.auth.models import User

user_jon = User.objects.get(id=2)

def send_message(request):
    print(request.user)
    print(user_jon)
    form = MessageForm(request.POST)
    messages = Message.objects.all()
    context = {
        'form': form,
        'messages': messages
    }
    if form.is_valid():
        if str(request.user) != 'AnonymousUser':
            form.instance.sender = request.user
        else:
            form.instance.sender = user_jon
        form.save()
    if request.is_ajax():
        return JsonResponse({}, status=201)
    return render(request, 'home.html', context)

def message_lists(request):
    qs = Message.objects.all()
    messages = [{'id':i.id, 'sender':i.sender.username, 'message':i.sender_text} for i in qs]
    return JsonResponse(messages, safe=False)