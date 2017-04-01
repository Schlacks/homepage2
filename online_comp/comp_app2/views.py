
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
#from django.http import HttpResponse
from comp_app2.models import InputForm
from comp_app2.compute import compute
# Create your views here.
def index(request):
    s=None
    if request.method=='POST':
        form=InputForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            r=form.r
            s=compute(r)
    else:
        form=InputForm()

    return render(request, 'C:/Users/Jan/PycharmProjects/Newversion/newattempt/online_comp/templates/comp_app2/index.html',
                 {'form': form,
                     's': '%.5f' % s if isinstance(s, float) else ''})
