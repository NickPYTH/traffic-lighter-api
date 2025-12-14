from django.urls.conf import path, include
from rest_framework import routers
from .views import (DepartmentViewSet, ProfileViewSet, IndicatorViewSet)

router = routers.DefaultRouter()
router.register(r'department', DepartmentViewSet)
router.register(r'profile', ProfileViewSet)
router.register(r'indicator', IndicatorViewSet)

urlpatterns = [
    path('', include(router.urls)),
]