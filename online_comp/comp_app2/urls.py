from django.conf.urls import url
from comp_app2 import views

urlpatterns=[
    url(r'^$',views.index)
]
