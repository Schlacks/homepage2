from django.conf.urls import url
from vib1 import views

urlpatterns=[
    url(r'^$',views.index)
]
