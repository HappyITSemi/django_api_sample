#
from django.urls import path
from . import views

app_name = 'apiv1'

urlpatterns = [
    path('notify/', views.Apiv1APIView.as_view({'get': 'list'}))
]
