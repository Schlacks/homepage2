from django.shortcuts import render

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse
from vib1.models import InputForm
from vib1.compute import compute
import os

def index(request):
    os.chdir(os.path.dirname(__file__))
    result = None
    if request.method == 'POST':
        form = InputForm(request.POST)
        if form.is_valid():
            form2 = form.save(commit=False)
            result = compute(form2.A, form2.b, form2.w, form2.T)
            result=result[7:]


    else:
        form = InputForm()

    return render ( request, 'C:/Users/Jan/PycharmProjects/Newversion/newattempt/online_comp/templates/vib1/vib1.html',
            {'form': form,
             'result': result,
             })

# Create your views here.
