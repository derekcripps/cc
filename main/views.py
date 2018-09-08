from .models import Customer, Company, Warehouse, Item, UOM
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .serializers import UserSerializer, GroupSerializer, CustomerSerializer, CompanySerializer, WarehouseSerializer, \
    ItemSerializer, UOMSerializer, CompanyListSerializer, WarehouseListSerializer
from . permissions import HasGroupPermission
from rest_framework.authentication import TokenAuthentication, SessionAuthentication


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class CustomerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    authentication_classes = (TokenAuthentication,)
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class CompanyViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication, SessionAuthentication)
    permission_classes = [HasGroupPermission]
    required_groups = {
        'main.add_company': ['CompanyMaintenance'],
        'main.change_company': ['CompanyMaintenance'],
        'main.add_company': ['__all__'],
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
