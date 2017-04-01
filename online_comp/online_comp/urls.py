"""online_comp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from bayes import views

urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^admin/', admin.site.urls),
    #url(r'^hw1/',include('comp_app.urls')),
    #url(r'^hw2/',include('comp_app2.urls')),
    #url(r'^vib1/',include('vib1.urls')),
    url(r'^bayes/',include('bayes.urls')),
    #url(r'^testingapp/',include('testingapp.urls')),
]

# urlpatterns = patterns('',
#     url(r'^hw1/', 'django_apps.hw1.views.index'),
