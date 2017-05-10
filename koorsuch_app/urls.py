from django.conf.urls import url

from . import views
from koorsuch_app.views import CableFormView

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^extra/$', CableFormView.as_view()),
]
