from django.shortcuts import render, render_to_response
from django import forms
from accounts.models import User
from django.template import RequestContext

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from datetime import datetime

class UserForm(forms.Form):
    username = forms.CharField(label = 'Username', max_length = 30)
    password = forms.CharField(label = 'Password', max_length = 30)
    pwconfirmed = forms.CharField(label = 'Re-enter password', max_length = 30)
    email = forms.EmailField(label = 'Email address')

def hello_world(request):
    return render(request, 'hello_world.html',{
        'current_time': str(datetime.now()),
    })

def login(request):
    if request.method == "POST":
        uf = UserForm(request.POST)
        if uf.is_valid():
            username = uf.cleaned_data['Username']
            password = uf.cleaned_data['Password']
            user = User.Objects.filter(get_username = username, get_passworld = password)
            if user:
                return render(request, 'hello_world.html',{
                    'current_time': str(datetime.now()),
                    })
            else:
                return HttpResponseRedirect('/login/')
    else:
        uf = UserForm()
        return HttpResponseRedirect('/login/')
    
def register(request):
    if request.method == "POST":
        uf = UserForm(request.POST)
        if uf.is_valid():
            username = uf.cleaned_data('Usernme')
            userChecked = User.Objects.filter(get_username = username)
            if userChecked:
                return render_to_response('register.html', {
                    'error': 'Error! Username existed!'
                    })
            else:
                password = uf.cleaned_data['Password']
                pwconfirmed = uf.cleaned_data['Re-enter password']
                if(password == pwconfirmed):
                    email = uf.cleaned_data['Email address']
                    user = User.obejcts.Create(username = username, password = password, email = email)
                    user.save()
                    return HttpResponseRedirect('/login/')
                else:
                    return render_to_response('register.html', {
                        'error': 'Password does not match! Re-enter the password.'
                        })
    else:
        uf = UserForm()
        return HttpResponseRedirect('/register/')