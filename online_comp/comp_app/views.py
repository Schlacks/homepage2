from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse
from comp_app.models import InputForm
from comp_app.compute import compute

def index(request):
    if request.method == 'POST':
        form = InputForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            return present_output(form)
    else:
        form = InputForm()

    return render(request, 'C:/Users/Jan/PycharmProjects/Newversion/newattempt/online_comp/templates/comp_app/index.html',
            {'form': form})

def present_output(form):
    r = form.r
    s = compute(r)
    return HttpResponse('Hello, World! sin(%s)=%s' % (r, s))
# Create your views here.
