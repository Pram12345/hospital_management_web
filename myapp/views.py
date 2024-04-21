from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import *
from django.core.mail import send_mail


# Create your views here.
def home(request):
    data = carausel.objects.all()
    data1 = card1.objects.all()
    data2 = card2.objects.all()
    

    
    context = {
              'data':data,
              'data1':data1,
              'data2':data2,
              

    }
    
    return render(request, 'home.html', context)

def appoint(request):
    appointment.objects.all()
    a = request.POST['fname']
    b = request.POST['faddress']
    c = request.POST['email']
    d = request.POST['age']
    e = request.POST['Date']
    f = request.POST['Time']
    g = request.POST['Doctor']
    m = appointment(yourname = a, youraddress = b, emailaddress = c, yourage = d, Date = e, Time = f, Doctor = g)
    m.save()
    y = request.POST['Time']
    j = appointment.objects.get(Time = y)
    x = j.id
    w = j.yourname
    n = j.emailaddress
    k = j.Time
    A = j.Doctor
    # l = 'bubugulshan509@gmail.com'
    temp = loader.get_template('demo.html')
    context = {
        'm':m,
        'j':j,
    }
    # send_mail(
    #     "CardioCare_Heart_Hospital", # sub 
    #    "Welcome to cardiocare_helth_hospital "'\n'"-------------------------------------------------------------" '\n''\n'"Your Appointment number = "+ str(x)+ '\n'"Patent Name = Mr." + w + '\n'"Doctor Name = " + A + '\n'"Time = " + k,   # msg Body
    #     l,# sender mail
    #     [n], # recvier mail
    #     fail_silently=False,
    #     )
    return HttpResponse(temp.render(context, request))

def contactus(request):
    contact.objects.all()
    p = request.POST['email']
    q = request.POST['phone']
    r = request.POST['address']
    s = request.POST['city']
    t = request.POST['state']
    u = request.POST['zip']
    v = request.POST['details']
    n = contact(memail=p, mphone=q, maddress=r, mcity=s, mstate=t, mpinno=u, mdetails=v)
    n.save()
    tem = loader.get_template('contact.html')
    context={
        'n':n,
    }
    return HttpResponse(tem.render(context, request))

def read(request):
    return render(request, 'demo.html', {} )

def contacts(request):
    return render(request, 'contact.html', {})
    





