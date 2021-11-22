from django.shortcuts import redirect, render
from .forms import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method == 'POST':
        form = UserRegistration(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username} !')
            return redirect('login')
    else:
        form = UserRegistration()
    context = {
        "form": form,
    }
    return render(request, 'register.html', context)

