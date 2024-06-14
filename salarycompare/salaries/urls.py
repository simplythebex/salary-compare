from django.urls import path, include
from rest_framework import routers

from .views import UserListView

router = routers.DefaultRouter()
router.register(r'users', UserListView)
# router.register(r'average', SalaryAverage)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]