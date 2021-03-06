# Generated by Django 3.1.6 on 2021-02-21 07:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('codename', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.IntegerField()),
                ('username', models.CharField(max_length=150, unique=True)),
                ('first_name', models.CharField(max_length=150)),
                ('last_name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.IntegerField()),
                ('is_active', models.IntegerField()),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Customers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(blank=True, max_length=50, null=True)),
                ('last_name', models.CharField(blank=True, max_length=50, null=True)),
                ('first_name', models.CharField(blank=True, max_length=50, null=True)),
                ('email_address', models.CharField(blank=True, max_length=50, null=True)),
                ('job_title', models.CharField(blank=True, max_length=50, null=True)),
                ('business_phone', models.CharField(blank=True, max_length=25, null=True)),
                ('home_phone', models.CharField(blank=True, max_length=25, null=True)),
                ('mobile_phone', models.CharField(blank=True, max_length=25, null=True)),
                ('fax_number', models.CharField(blank=True, max_length=25, null=True)),
                ('address', models.TextField(blank=True, null=True)),
                ('city', models.CharField(blank=True, max_length=50, null=True)),
                ('state_province', models.CharField(blank=True, max_length=50, null=True)),
                ('zip_postal_code', models.CharField(blank=True, max_length=15, null=True)),
                ('country_region', models.CharField(blank=True, max_length=50, null=True)),
                ('web_page', models.TextField(blank=True, null=True)),
                ('notes', models.TextField(blank=True, null=True)),
                ('attachments', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'customers',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.PositiveSmallIntegerField()),
                ('change_message', models.TextField()),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Employees',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(blank=True, max_length=50, null=True)),
                ('last_name', models.CharField(blank=True, max_length=50, null=True)),
                ('first_name', models.CharField(blank=True, max_length=50, null=True)),
                ('email_address', models.CharField(blank=True, max_length=50, null=True)),
                ('job_title', models.CharField(blank=True, max_length=50, null=True)),
                ('business_phone', models.CharField(blank=True, max_length=25, null=True)),
                ('home_phone', models.CharField(blank=True, max_length=25, null=True)),
                ('mobile_phone', models.CharField(blank=True, max_length=25, null=True)),
                ('fax_number', models.CharField(blank=True, max_length=25, null=True)),
                ('address', models.TextField(blank=True, null=True)),
                ('city', models.CharField(blank=True, max_length=50, null=True)),
                ('state_province', models.CharField(blank=True, max_length=50, null=True)),
                ('zip_postal_code', models.CharField(blank=True, max_length=15, null=True)),
                ('country_region', models.CharField(blank=True, max_length=50, null=True)),
                ('web_page', models.TextField(blank=True, null=True)),
                ('notes', models.TextField(blank=True, null=True)),
                ('attachments', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'employees',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='InventoryTransactions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_created_date', models.DateTimeField(blank=True, null=True)),
                ('transaction_modified_date', models.DateTimeField(blank=True, null=True)),
                ('quantity', models.IntegerField()),
                ('comments', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'inventory_transactions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='InventoryTransactionTypes',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('type_name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'inventory_transaction_types',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Invoices',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invoice_date', models.DateTimeField(blank=True, null=True)),
                ('due_date', models.DateTimeField(blank=True, null=True)),
                ('tax', models.DecimalField(blank=True, decimal_places=4, max_digits=19, null=True)),
                ('shipping', models.DecimalField(blank=True, decimal_places=4, max_digits=19, null=True)),
                ('amount_due', models.DecimalField(blank=True, decimal_places=4, max_digits=19, null=True)),
            ],
            options={
                'db_table': 'invoices',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='OrderDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.DecimalField(decimal_places=4, max_digits=18)),
                ('unit_price', models.DecimalField(blank=True, decimal_places=4, max_digits=19, null=True)),
                ('discount', models.FloatField()),
                ('date_allocated', models.DateTimeField(blank=True, null=True)),
                ('purchase_order_id', models.IntegerField(blank=True, null=True)),
                ('inventory_id', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'order_details',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='OrderDetailsStatus',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('status_name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'order_details_status',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_date', models.DateTimeField(blank=True, null=True)),
                ('shipped_date', models.DateTimeField(blank=True, null=True)),
                ('ship_name', models.CharField(blank=True, max_length=50, null=True)),
                ('ship_address', models.TextField(blank=True, null=True)),
                ('ship_city', models.CharField(blank=True, max_length=50, null=True)),
                ('ship_state_province', models.CharField(blank=True, max_length=50, null=True)),
                ('ship_zip_postal_code', models.CharField(blank=True, max_length=50, null=True)),
                ('ship_country_region', models.CharField(blank=True, max_length=50, null=True)),
                ('shipping_fee', models.DecimalField(blank=True, decimal_places=4, max_digits=19, null=True)),
                ('taxes', models.DecimalField(blank=True, decimal_places=4, max_digits=19, null=True)),
                ('payment_type', models.CharField(blank=True, max_length=50, null=True)),
                ('paid_date', models.DateTimeField(blank=True, null=True)),
                ('notes', models.TextField(blank=True, null=True)),
                ('tax_rate', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'orders',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='OrdersStatus',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('status_name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'orders_status',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='OrdersTaxStatus',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('tax_status_name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'orders_tax_status',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Privileges',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('privilege_name', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'privileges',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('supplier_ids', models.TextField(blank=True, null=True)),
                ('product_code', models.CharField(blank=True, max_length=25, null=True)),
                ('product_name', models.CharField(blank=True, max_length=50, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('standard_cost', models.DecimalField(blank=True, decimal_places=4, max_digits=19, null=True)),
                ('list_price', models.DecimalField(decimal_places=4, max_digits=19)),
                ('reorder_level', models.IntegerField(blank=True, null=True)),
                ('target_level', models.IntegerField(blank=True, null=True)),
                ('quantity_per_unit', models.CharField(blank=True, max_length=50, null=True)),
                ('discontinued', models.IntegerField()),
                ('minimum_reorder_quantity', models.IntegerField(blank=True, null=True)),
                ('category', models.CharField(blank=True, max_length=50, null=True)),
                ('attachments', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'products',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PurchaseOrderDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.DecimalField(decimal_places=4, max_digits=18)),
                ('unit_cost', models.DecimalField(decimal_places=4, max_digits=19)),
                ('date_received', models.DateTimeField(blank=True, null=True)),
                ('posted_to_inventory', models.IntegerField()),
            ],
            options={
                'db_table': 'purchase_order_details',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PurchaseOrders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('submitted_date', models.DateTimeField(blank=True, null=True)),
                ('creation_date', models.DateTimeField(blank=True, null=True)),
                ('expected_date', models.DateTimeField(blank=True, null=True)),
                ('shipping_fee', models.DecimalField(decimal_places=4, max_digits=19)),
                ('taxes', models.DecimalField(decimal_places=4, max_digits=19)),
                ('payment_date', models.DateTimeField(blank=True, null=True)),
                ('payment_amount', models.DecimalField(blank=True, decimal_places=4, max_digits=19, null=True)),
                ('payment_method', models.CharField(blank=True, max_length=50, null=True)),
                ('notes', models.TextField(blank=True, null=True)),
                ('approved_by', models.IntegerField(blank=True, null=True)),
                ('approved_date', models.DateTimeField(blank=True, null=True)),
                ('submitted_by', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'purchase_orders',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PurchaseOrderStatus',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('status', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'purchase_order_status',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SalesReports',
            fields=[
                ('group_by', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('display', models.CharField(blank=True, max_length=50, null=True)),
                ('title', models.CharField(blank=True, max_length=50, null=True)),
                ('filter_row_source', models.TextField(blank=True, null=True)),
                ('default', models.IntegerField()),
            ],
            options={
                'db_table': 'sales_reports',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Shippers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(blank=True, max_length=50, null=True)),
                ('last_name', models.CharField(blank=True, max_length=50, null=True)),
                ('first_name', models.CharField(blank=True, max_length=50, null=True)),
                ('email_address', models.CharField(blank=True, max_length=50, null=True)),
                ('job_title', models.CharField(blank=True, max_length=50, null=True)),
                ('business_phone', models.CharField(blank=True, max_length=25, null=True)),
                ('home_phone', models.CharField(blank=True, max_length=25, null=True)),
                ('mobile_phone', models.CharField(blank=True, max_length=25, null=True)),
                ('fax_number', models.CharField(blank=True, max_length=25, null=True)),
                ('address', models.TextField(blank=True, null=True)),
                ('city', models.CharField(blank=True, max_length=50, null=True)),
                ('state_province', models.CharField(blank=True, max_length=50, null=True)),
                ('zip_postal_code', models.CharField(blank=True, max_length=15, null=True)),
                ('country_region', models.CharField(blank=True, max_length=50, null=True)),
                ('web_page', models.TextField(blank=True, null=True)),
                ('notes', models.TextField(blank=True, null=True)),
                ('attachments', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'shippers',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Strings',
            fields=[
                ('string_id', models.AutoField(primary_key=True, serialize=False)),
                ('string_data', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'strings',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Suppliers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(blank=True, max_length=50, null=True)),
                ('last_name', models.CharField(blank=True, max_length=50, null=True)),
                ('first_name', models.CharField(blank=True, max_length=50, null=True)),
                ('email_address', models.CharField(blank=True, max_length=50, null=True)),
                ('job_title', models.CharField(blank=True, max_length=50, null=True)),
                ('business_phone', models.CharField(blank=True, max_length=25, null=True)),
                ('home_phone', models.CharField(blank=True, max_length=25, null=True)),
                ('mobile_phone', models.CharField(blank=True, max_length=25, null=True)),
                ('fax_number', models.CharField(blank=True, max_length=25, null=True)),
                ('address', models.TextField(blank=True, null=True)),
                ('city', models.CharField(blank=True, max_length=50, null=True)),
                ('state_province', models.CharField(blank=True, max_length=50, null=True)),
                ('zip_postal_code', models.CharField(blank=True, max_length=15, null=True)),
                ('country_region', models.CharField(blank=True, max_length=50, null=True)),
                ('web_page', models.TextField(blank=True, null=True)),
                ('notes', models.TextField(blank=True, null=True)),
                ('attachments', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'suppliers',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='EmployeePrivileges',
            fields=[
                ('employee', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='tutorial.employees')),
            ],
            options={
                'db_table': 'employee_privileges',
                'managed': False,
            },
        ),
    ]
