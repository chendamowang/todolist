from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, TodoListViewSet

router = DefaultRouter()
router.register(r'todolists', TodoListViewSet)
router.register(r'users', UserViewSet)

app_name = 'api'
urlpatterns = [
    url(r'', include(router.urls)),
    url(r'api-auth/', include('rest_framework.urls')),
]
