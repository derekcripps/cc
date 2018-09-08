from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Customer, Company, Warehouse, Item, UOM


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('id', 'code', 'name')


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ('id', 'code', 'name', 'customer')


class CompanyListSerializer(serializers.ModelSerializer):
    customer = serializers.StringRelatedField()

    class Meta:
        model = Company
        fields = ('id', 'code', 'name', 'customer')


class WarehouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Warehouse
        fields = ('id', 'code', 'name', 'company')


class WarehouseListSerializer(serializers.ModelSerializer):
    company = serializers.StringRelatedField()

    class Meta:
        model = Warehouse
        fields = ('id', 'code', 'name', 'company')


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ('id', 'company', 'code', 'description', 'inventory_UOM', 'inventory_cost', 'notes')


class UOMSerializer(serializers.ModelSerializer):
    class Meta:
        model = UOM
        fields = ('id', 'company', 'code', 'description')
