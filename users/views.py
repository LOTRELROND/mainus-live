from django.shortcuts import render,redirect
from .forms import RegisterForm,LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from .models import CustomUser
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes, force_str, DjangoUnicodeDecodeError
from .utils import generate_token
from django.core.mail import EmailMessage
from django.conf import settings
from django.urls import reverse
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
import ssl
import smtplib

# Create your views here.

def register(request):

    form = RegisterForm(request.POST or None)
    if form.is_valid():
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")

        newUser = CustomUser(email =email)
        newUser.set_password(password)

        newUser.save()

        current_site = get_current_site(request)
        email_body = render_to_string('activate.html', {
            'newUser': newUser,
            'domain': current_site,
            'uid': urlsafe_base64_encode(force_bytes(newUser.pk)),
            'token': generate_token.make_token(newUser)
        })

        send_mail('Activate your account',email_body,
                        'mehmetkemalkayam@gmail.com',
                         [newUser.email])


        return redirect("users:login")
    context = {
            "form" : form
        }
    return render(request,"register.html",context)
  
def loginUser(request):
    form = LoginForm(request.POST or None)

    context = {
        "form":form
    }

    if form.is_valid():
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")

        CustomUser = authenticate(email = email,password = password)



        if CustomUser is None:
            return render(request,"login.html",context)

        if not CustomUser.is_email_verified:
            raise ValueError('check your email box')
            return render(request, 'login.html',context)

        login(request,CustomUser)
        return redirect("index")
    return render(request,"login.html",context)

@login_required
def logoutUser(request):
    logout(request)
    return redirect('index')

def activate(request,uidb64,token):

    #try except bloğunu kaldırdım 
    uid = force_str(urlsafe_base64_decode(uidb64))
    newUser = CustomUser.objects.get(pk=uid)

    #############################################################
    if newUser and generate_token.check_token(newUser,token):
        newUser.is_email_verified = True

        newUser.save()
        return redirect(reverse('users:login'))
    return render(request, 'activatefail.html', {'newUser': newUser})
