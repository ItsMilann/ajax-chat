from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from core.views import send_message, message_lists
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', send_message, name='send-message'),
    path('login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('message_lists/', message_lists),
    
]
