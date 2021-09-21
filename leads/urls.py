from django.urls import path
from leads.views import *

app_name = 'leads'

urlpatterns = [
    path('', lead_list),
    path('<pk>/', lead_detail)
]