from django.conf.urls import url
from testingapp import views

urlpatterns=[
    url(r'^$',views.index)
]
