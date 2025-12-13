from django.urls.conf import path, include
from rest_framework import routers

from .views import DepartmentViewSet

router = routers.DefaultRouter()

router.register(r'department', DepartmentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]