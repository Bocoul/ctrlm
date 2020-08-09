

from django.contrib import admin
from .views import index,prm_search, etab_search, go


from .models import setup_data
from django.urls import path

app_name = 'ctrlm'


urlpatterns = [
    path('', index),
    path('go/', go),
    path('prmquery/', prm_search, name='prmquery'),
    path('etabquery/', etab_search,  name='etabquery'),
]

# print("***********$setup_data()")
# setup_data()
# print("***************$$$$$setup_data()")