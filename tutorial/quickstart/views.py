# -*- coding: utf-8 -*-
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User, Group
from rest_framework import viewsets, permissions
from tutorial.quickstart.serializers import UserSerializer, GroupSerializer
from tutorial.quickstart import models, serializers

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by("-date_joined")
    serializer_class = UserSerializer
    permission_classes = []
	

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_class = []

class AuthGroupViewSet(viewsets.ModelViewSet):
	queryset = models.AuthGroup.objects.all()
	serializer_class = serializers.AuthGroupSerializer

class AuthGroupPermissionsViewSet(viewsets.ModelViewSet):
	queryset = models.AuthGroupPermissions.objects.all()
	serializer_class = serializers.AuthGroupPermissionsSerializer

class AuthPermissionViewSet(viewsets.ModelViewSet):
	queryset = models.AuthPermission.objects.all()
	serializer_class = serializers.AuthPermissionSerializer

class AuthUserViewSet(viewsets.ModelViewSet):
	queryset = models.AuthUser.objects.all()
	serializer_class = serializers.AuthUserSerializer

class AuthUserGroupsViewSet(viewsets.ModelViewSet):
	queryset = models.AuthUserGroups.objects.all()
	serializer_class = serializers.AuthUserGroupsSerializer

class AuthUserUserPermissionsViewSet(viewsets.ModelViewSet):
	queryset = models.AuthUserUserPermissions.objects.all()
	serializer_class = serializers.AuthUserUserPermissionsSerializer

class CustomersViewSet(viewsets.ModelViewSet):
	queryset = models.Customers.objects.all()
	serializer_class = serializers.CustomersSerializer

class DjangoAdminLogViewSet(viewsets.ModelViewSet):
	queryset = models.DjangoAdminLog.objects.all()
	serializer_class = serializers.DjangoAdminLogSerializer

class DjangoContentTypeViewSet(viewsets.ModelViewSet):
	queryset = models.DjangoContentType.objects.all()
	serializer_class = serializers.DjangoContentTypeSerializer

class DjangoMigrationsViewSet(viewsets.ModelViewSet):
	queryset = models.DjangoMigrations.objects.all()
	serializer_class = serializers.DjangoMigrationsSerializer

class DjangoSessionViewSet(viewsets.ModelViewSet):
	queryset = models.DjangoSession.objects.all()
	serializer_class = serializers.DjangoSessionSerializer

class EmployeePrivilegesViewSet(viewsets.ModelViewSet):
	queryset = models.EmployeePrivileges.objects.all()
	serializer_class = serializers.EmployeePrivilegesSerializer

class EmployeesViewSet(viewsets.ModelViewSet):
	queryset = models.Employees.objects.all()
	serializer_class = serializers.EmployeesSerializer

class InventoryTransactionTypesViewSet(viewsets.ModelViewSet):
	queryset = models.InventoryTransactionTypes.objects.all()
	serializer_class = serializers.InventoryTransactionTypesSerializer

class InventoryTransactionsViewSet(viewsets.ModelViewSet):
	queryset = models.InventoryTransactions.objects.all()
	serializer_class = serializers.InventoryTransactionsSerializer

class InvoicesViewSet(viewsets.ModelViewSet):
	queryset = models.Invoices.objects.all()
	serializer_class = serializers.InvoicesSerializer

class OrderDetailsViewSet(viewsets.ModelViewSet):
	queryset = models.OrderDetails.objects.all()
	serializer_class = serializers.OrderDetailsSerializer

class OrderDetailsStatusViewSet(viewsets.ModelViewSet):
	queryset = models.OrderDetailsStatus.objects.all()
	serializer_class = serializers.OrderDetailsStatusSerializer

class OrdersViewSet(viewsets.ModelViewSet):
	queryset = models.Orders.objects.all()
	serializer_class = serializers.OrdersSerializer

class OrdersStatusViewSet(viewsets.ModelViewSet):
	queryset = models.OrdersStatus.objects.all()
	serializer_class = serializers.OrdersStatusSerializer

class OrdersTaxStatusViewSet(viewsets.ModelViewSet):
	queryset = models.OrdersTaxStatus.objects.all()
	serializer_class = serializers.OrdersTaxStatusSerializer

class PrivilegesViewSet(viewsets.ModelViewSet):
	queryset = models.Privileges.objects.all()
	serializer_class = serializers.PrivilegesSerializer

class ProductsViewSet(viewsets.ModelViewSet):
	queryset = models.Products.objects.all()
	serializer_class = serializers.ProductsSerializer

class PurchaseOrderDetailsViewSet(viewsets.ModelViewSet):
	queryset = models.PurchaseOrderDetails.objects.all()
	serializer_class = serializers.PurchaseOrderDetailsSerializer

class PurchaseOrderStatusViewSet(viewsets.ModelViewSet):
	queryset = models.PurchaseOrderStatus.objects.all()
	serializer_class = serializers.PurchaseOrderStatusSerializer

class PurchaseOrdersViewSet(viewsets.ModelViewSet):
	queryset = models.PurchaseOrders.objects.all()
	serializer_class = serializers.PurchaseOrdersSerializer

class SalesReportsViewSet(viewsets.ModelViewSet):
	queryset = models.SalesReports.objects.all()
	serializer_class = serializers.SalesReportsSerializer

class ShippersViewSet(viewsets.ModelViewSet):
	queryset = models.Shippers.objects.all()
	serializer_class = serializers.ShippersSerializer

class StringsViewSet(viewsets.ModelViewSet):
	queryset = models.Strings.objects.all()
	serializer_class = serializers.StringsSerializer

class SuppliersViewSet(viewsets.ModelViewSet):
	queryset = models.Suppliers.objects.all()
	serializer_class = serializers.SuppliersSerializer