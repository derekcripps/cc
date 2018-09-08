from django.db import models
from django.contrib.auth.models import User


class Customer(models.Model):
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Company(models.Model):
    customer = models.ForeignKey('Customer', on_delete=models.PROTECT, related_name='companies')
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Warehouse(models.Model):
    #customer = models.ForeignKey('Customer', on_delete=models.PROTECT)
    company = models.ForeignKey('Company', on_delete=models.CASCADE, related_name='warehouses')
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class UOM(models.Model):
    #customer = models.ForeignKey('Customer', on_delete=models.PROTECT)
    company = models.ForeignKey('Company', on_delete=models.CASCADE, related_name='uoms')
    code = models.CharField(max_length=3)
    description = models.CharField(max_length=50)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.code


class Item(models.Model):
    #customer = models.ForeignKey('Customer', on_delete=models.PROTECT)
    company = models.ForeignKey('Company', on_delete=models.CASCADE)
    code = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    inventory_UOM = models.ForeignKey('UOM', on_delete=models.PROTECT)
    inventory_cost = models.DecimalField(max_digits=13, decimal_places=4)
    notes = models.CharField(max_length=200, null=True, blank=False)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)


class CountHeader(models.Model):
    #customer = models.ForeignKey('Customer', on_delete=models.PROTECT)
    company = models.ForeignKey('Company', on_delete=models.CASCADE)
    description = models.CharField(max_length=100)
    locations_to_use = models.IntegerField
    blind_count = models.BooleanField(default=True)
    show_cost = models.BooleanField(default=False)
    allow_add_new = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)


class CountDetail(models.Model):
    count_header = models.ForeignKey('CountHeader', on_delete=models.CASCADE)
    #company = models.ForeignKey('Company', on_delete=models.CASCADE)
    warehouse = models.ForeignKey('Warehouse', on_delete=models.CASCADE)
    location1 = models.CharField(max_length=50)
    location2 = models.CharField(max_length=50)
    location3 = models.CharField(max_length=50)
    location4 = models.CharField(max_length=50)
    location5 = models.CharField(max_length=50)
    item = models.ForeignKey('Item', on_delete=models.CASCADE, )
    uom = models.ForeignKey('UOM', on_delete=models.PROTECT)
    quantity1 = models.DecimalField(max_digits=13, decimal_places=4)
    counted_by = models.ForeignKey(User, on_delete=models.PROTECT)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)


class Inventory(models.Model):
    company = models.ForeignKey('Company', on_delete=models.CASCADE)
    item = models.ForeignKey('Item', on_delete=models.CASCADE)
    location1 = models.CharField(max_length=50)
    location2 = models.CharField(max_length=50)
    location3 = models.CharField(max_length=50)
    location4 = models.CharField(max_length=50)
    location5 = models.CharField(max_length=50)
    item = models.ForeignKey('Item', on_delete=models.CASCADE)
    uom = models.ForeignKey('UOM', on_delete=models.PROTECT)
    quantity1 = models.DecimalField(max_digits=13, decimal_places=4)
    unit_cost = models.DecimalField(max_digits=13, decimal_places=4)
    created_date = models.DateTimeField(auto_now_add=True)


class ItemXRef(models.Model):
    #customer = models.ForeignKey('customer', on_delete=models.PROTECT)
    company = models.ForeignKey('Company', on_delete=models.CASCADE)
    warehouse = models.ForeignKey('Warehouse', on_delete=models.CASCADE)
    external_item = models.CharField(max_length=100)
    Internal_item = models.CharField(max_length=100)


class Location(models.Model):
    company = models.ForeignKey('Company', on_delete=models.CASCADE)
    warehouse = models.ForeignKey('Warehouse', on_delete=models.CASCADE)
    location1 = models.CharField(max_length=50)
    location2 = models.CharField(max_length=50)
    location3 = models.CharField(max_length=50)
    location4 = models.CharField(max_length=50)
    location5 = models.CharField(max_length=50)
    created_date = models.DateTimeField(auto_now_add=True)