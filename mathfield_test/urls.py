from django.conf.urls import url
from django.views.generic import RedirectView

from mathfield_test import views


urlpatterns = [
    url(r'^$', RedirectView.as_view(url='mathfield/', permanent=False)),

    url(r'^mathfield/$', views.MathfieldListView.as_view(), name='mathfield_list'),
]
