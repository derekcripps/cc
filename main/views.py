from .models import Customer, Company, Warehouse, Item, UOM
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .serializers import UserSerializer, GroupSerializer, CustomerSerializer, CompanySerializer, WarehouseSerializer, \
    ItemSerializer, UOMSerializer, CompanyListSerializer, WarehouseListSerializer
from . permissions import HasModelPermission
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


# Function Based API - Does not need queryset, and requires different URL formatting
@permission_classes(IsAuthenticated, )
@api_view()
def permission_view(request):
    logged_in_user = request.user
    return Response(data=logged_in_user.get_all_permissions())


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class CustomerViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,SessionAuthentication)
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class CompanyViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication, SessionAuthentication)
    permission_classes = [HasModelPermission]
    required_model = {
        'GET': ['company'],
        'POST': ['company'],
        'PUT': ['company'],
        'DELETE': ['company'],
    }
    queryset = Company.objects.all().select_related('customer')
    serializer_class = CompanySerializer
    action_serializers = {
        'list': CompanyListSerializer
    }

    def get_serializer_class(self):

        if hasattr(self, 'action_serializers'):
            if self.action in self.action_serializers:
                return self.action_serializers[self.action]

        return super(CompanyViewSet, self).get_serializer_class()


class WarehouseViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication, SessionAuthentication)
    permission_classes = [HasModelPermission]
    required_model = {
        'GET': ['warehouse'],
        'POST': ['warehouse'],
        'PUT': ['warehouse'],
        'DELETE': ['warehouse'],
    }
    queryset = Warehouse.objects.all()
    serializer_class = WarehouseSerializer
    action_serializers = {
        'list': WarehouseListSerializer
    }

    def get_serializer_class(self):

        if hasattr(self, 'action_serializers'):
            if self.action in self.action_serializers:
                return self.action_serializers[self.action]

        return super(WarehouseViewSet, self).get_serializer_class()


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class UOMViewSet(viewsets.ModelViewSet):
    queryset = UOM.objects.all()
    serializer_class = UOMSerializer

