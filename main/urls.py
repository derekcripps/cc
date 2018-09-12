
from django.conf.urls import url, include
from django.urls import path
from rest_framework import routers
from . import views
from .auth import login

router = routers.DefaultRouter()
router.register(r'user', views.UserViewSet)
router.register(r'group', views.GroupViewSet)
router.register(r'customer', views.CustomerViewSet)
router.register('company', views.CompanyViewSet)
router.register('warehouse', views.WarehouseViewSet)
router.register('item', views.ItemViewSet)
router.register('uom', views.UOMViewSet)
#router.register('perms', views.permission_view)

from . import views

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'permissions_view', views.permission_view, name='permissions_view'),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('login', login)
]