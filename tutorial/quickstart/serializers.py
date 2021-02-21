# -*- coding: utf-8 -*-
from django.contrib.auth.models import User, Group
from rest_framework import serializers
from ..quickstart import models

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class AuthGroupSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = models.AuthGroup
		fields = ['url', 'name']

class AuthGroupPermissionsSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = models.AuthGroupPermissions
		fields = ['url', 'group', 'permission']

class AuthPermissionSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = models.AuthPermission
		fields = ['url', 'name', 'content_type', 'codename']

class AuthUserSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = models.AuthUser
		fields = ['url', 'password', 'last_login', 'is_superuser', 'username', 'first_name', 'last_name', 'email', 'is_staff', 'is_active', 'date_joined']

class AuthUserGroupsSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = models.AuthUserGroups
		fields = ['url', 'user', 'group']

class AuthUserUserPermissionsSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = models.AuthUserUserPermissions
		fields = ['url', 'user', 'permission']

class CustomersSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = models.Customers
		fields = ['url', 'company', 'last_name', 'first_name', 'email_address', 'job_title', 'business_phone', 'home_phone', 'mobile_phone', 'fax_number', 'address', 'city', 'state_province', 'zip_postal_code', 'country_region', 'web_page', 'notes', 'attachments']

class DjangoAdminLogSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = models.DjangoAdminLog
		fields = ['url', 'action_time', 'object_id', 'object_repr', 'action_flag', 'change_message', 'content_type', 'user']

class DjangoContentTypeSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = models.DjangoContentType
		fields = ['url', 'app_label', 'model']

class DjangoMigrationsSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = models.DjangoMigrations
		fields = ['url', 'app', 'name', 'applied']

class DjangoSessionSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = models.DjangoSession
		fields = ['url', 'session_key', 'session_data', 'expire_date']

class EmployeePrivilegesSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = models.EmployeePrivileges
		fields = ['url', 'employee', 'privilege']

class EmployeesSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = models.Employees
		fields = ['url', 'company', 'last_name', 'first_name', 'email_address', 'job_title', 'business_phone', 'home_phone', 'mobile_phone', 'fax_number', 'address', 'city', 'state_province', 'zip_postal_code', 'country_region', 'web_page', 'notes', 'attachments']

class InventoryTransactionTypesSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = models.InventoryTransactionTypes
		fields = ['url', 'id', 'type_name']

class InventoryTransactionsSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = models.InventoryTransactions
		fields = ['url', 'transaction_type', 'transaction_created_date', 'transaction_modified_date', 'product', 'quantity', 'purchase_order', 'customer_order', 'comments']

class InvoicesSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = models.Invoices
		fields = ['url', 'order', 'invoice_date', 'due_date', 'tax', 'shipping', 'amount_due']

class OrderDetailsSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = models.OrderDetails
		fields = ['url', 'order', 'product', 'quantity', 'unit_price', 'discount', 'status', 'date_allocated', 'purchase_order_id', 'inventory_id']

class OrderDetailsStatusSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = models.OrderDetailsStatus
		fields = ['url', 'id', 'status_name']

class OrdersSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = models.Orders
		fields = ['url', 'employee', 'customer', 'order_date', 'shipped_date', 'shipper', 'ship_name', 'ship_address', 'ship_city', 'ship_state_province', 'ship_zip_postal_code', 'ship_country_region', 'shipping_fee', 'taxes', 'payment_type', 'paid_date', 'notes', 'tax_rate', 'tax_status', 'status']

class OrdersStatusSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = models.OrdersStatus
		fields = ['url', 'id', 'status_name']

class OrdersTaxStatusSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = models.OrdersTaxStatus
		fields = ['url', 'id', 'tax_status_name']

class PrivilegesSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = models.Privileges
		fields = ['url', 'privilege_name']

class ProductsSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = models.Products
		fields = ['url', 'supplier_ids', 'product_code', 'product_name', 'description', 'standard_cost', 'list_price', 'reorder_level', 'target_level', 'quantity_per_unit', 'discontinued', 'minimum_reorder_quantity', 'category', 'attachments']

class PurchaseOrderDetailsSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = models.PurchaseOrderDetails
		fields = ['url', 'purchase_order', 'product', 'quantity', 'unit_cost', 'date_received', 'posted_to_inventory', 'inventory']

class PurchaseOrderStatusSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = models.PurchaseOrderStatus
		fields = ['url', 'id', 'status']

class PurchaseOrdersSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = models.PurchaseOrders
		fields = ['url', 'supplier', 'created_by', 'submitted_date', 'creation_date', 'status', 'expected_date', 'shipping_fee', 'taxes', 'payment_date', 'payment_amount', 'payment_method', 'notes', 'approved_by', 'approved_date', 'submitted_by']

class SalesReportsSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = models.SalesReports
		fields = ['url', 'group_by', 'display', 'title', 'filter_row_source', 'default']

class ShippersSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = models.Shippers
		fields = ['url', 'company', 'last_name', 'first_name', 'email_address', 'job_title', 'business_phone', 'home_phone', 'mobile_phone', 'fax_number', 'address', 'city', 'state_province', 'zip_postal_code', 'country_region', 'web_page', 'notes', 'attachments']

class StringsSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = models.Strings
		fields = ['url', 'string_id', 'string_data']

class SuppliersSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = models.Suppliers
		fields = ['url', 'company', 'last_name', 'first_name', 'email_address', 'job_title', 'business_phone', 'home_phone', 'mobile_phone', 'fax_number', 'address', 'city', 'state_province', 'zip_postal_code', 'country_region', 'web_page', 'notes', 'attachments']
