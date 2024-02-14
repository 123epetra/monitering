from django.urls import path
from .views import *


urlpatterns = [
    path('', home , name = 'home'),
    path('cpform/', cpform , name = 'cpform'),
    path('contact/', contact , name = 'contact'),
    path('coform/', coform , name = 'coform')

]