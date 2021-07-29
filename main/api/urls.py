from django.urls import path, include
from main.api import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('task', views.TaskViewSet)




urlpatterns = [
      path('v1/', include(router.urls)),
]