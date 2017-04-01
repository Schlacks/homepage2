from django.conf.urls import url
from comp_app import views

urlpatterns=[
    url(r'^$',views.index)
]
