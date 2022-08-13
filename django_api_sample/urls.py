#
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
import apiv1.views

router = routers.DefaultRouter()
router.register('notify', apiv1.views.Apiv1APIView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('apiv1.urls'))
    # path('api/v2/', include('apiv2ß.urls'))
]
