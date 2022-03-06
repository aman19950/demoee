from django.http import HttpResponse
from django.shortcuts import redirect, render

# Create your views here.
from .models import Register_Info


def index(request):

    # try:
    #     fetch_info = Register_Info.objects.get(email="aman@gmail.com")
    # except:
    #     return HttpResponse("not a valid email")

    return render(request, 'home.html')


def contact(request):
    return render(request, 'contact.html')


def saveinfo(request):
    if request.method == "POST":
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')

        s = Register_Info(first_name=firstname,
                          last_name=lastname, email=email)
        s.save()

    return HttpResponse("success")


def login(request):

    if request.method == "POST":
        email_id = request.POST.get('email')
        try:
            fetch_email = Register_Info.objects.get(email=email_id)

            request.session['firstname'] = fetch_email.first_name

        except:
            return HttpResponse("wrong email")

    return render(request, 'contact.html')


def logout(request):
    request.session.clear()
    return redirect('home')
