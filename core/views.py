from django.shortcuts import render
from .models import Message
from .forms import MessageForm
from django.http import JsonResponse
from django.contrib.auth.models import User
import random
import string


def create_cid():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=20))

def get_user(request):
    if str(request.user) != 'AnonymousUser':
        return 'anonymous'
    return request.user.username

def send_message(request):
    client_id = request.COOKIES.get('client_id')
    context = None
    if request.method == 'POST':
        form = MessageForm(request.POST)
        messages = Message.objects.all()
        context = {'form': form, 'messages': messages}
        if form.is_valid():
            if str(request.user) == 'AnonymousUser' and client_id is not None:
                form.instance.client = str(client_id)
            else:
                form.instance.client = request.user.username
            form.save()
    if request.is_ajax():
        response = JsonResponse({}, status=201)
    else:
        response = render(request, 'home.html', context)
    if client_id == None:
        response.set_cookie('client_id', create_cid())
    return response

def message_lists(request):
    print(request.user)
    if request.user.is_authenticated:
        client = request.user.username
    elif request.COOKIES.get('client_id') is not None:
        client = request.COOKIES.get('client_id') 
    else:
        client = str(request.GET.get('cid'))
    print(client)
    qs = Message.objects.filter(client = client)
    messages = [{'id':i.id, 'client':i.client, 'admin_message':i.admin_message, 'client_message':i.client_message} for i in qs]
    return JsonResponse(messages, safe=False)