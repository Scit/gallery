# coding: utf-8
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.conf import settings


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, u'Вы успешно зарегистрированы')
            new_user = authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password1'])

            login(request, new_user)
            return HttpResponseRedirect(reverse('owner', args=(new_user.pk,)))
    else:
        form = UserCreationForm()

    return render(request, 'registration/register.html',
            {'form': form})
