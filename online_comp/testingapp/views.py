from django.shortcuts import render

from testingapp.models import Button1Form, Button2Form

def index(request):
    outcome=None
    if request.method=='POST' and 'button1' in request.POST:
        form=Button1Form(request.POST)
        if form.is_valid():
            form2=form.save(commit=False)
            outcome=form2.b1+10000
    if request.method=='POST' and 'button2' in request.POST:
        form=Button2Form(request.POST)
        if form.is_valid():
            form2=form.save(comit=False)
            outcome=form2.b2-10000

    return render(request,'C:/Users/Jan/PycharmProjects/Newversion/newattempt/online_comp/templates/testingapp/index.html',{'outcome':outcome})
# Create your views here.
