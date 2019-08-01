from django.urls import path, re_path

from . views import *


app_name = 'shop'

urlpatterns = [
    path('', home, name='home'),
    path('category/<path:hierarchy>/', show_category, name='category'),

]