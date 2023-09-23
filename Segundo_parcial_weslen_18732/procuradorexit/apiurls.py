from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .apiviews import *

router = DefaultRouter()
router.register(r'procurador', ProcuradorViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
]