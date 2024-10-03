from django.urls import include, path
from rest_framework import routers
from .views import TaskViewSet

router = routers.DefaultRouter()
router.register(r'tasks', TaskViewSet, 'tasks')

urlpatterns = [
    path('v1/', include(router.urls))
]
