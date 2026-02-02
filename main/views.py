from django.shortcuts import render
from .models import UserData

def home(request):
    users = UserData.objects.all()
    total_users = users.count()

    return render(request, 'index.html', {
        'users': users,
        'total_users': total_users
    })