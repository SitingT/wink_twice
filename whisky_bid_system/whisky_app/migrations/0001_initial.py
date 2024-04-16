# Generated by Django 3.2 on 2024-04-16 18:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(db_column='UserID',
                 primary_key=True, serialize=False)),
                ('name', models.CharField(
                    db_column='Username', max_length=255, unique=True)),
                ('first_name', models.CharField(blank=True,
                 db_column='FirstName', max_length=255, null=True)),
                ('last_name', models.CharField(blank=True,
                 db_column='LastName', max_length=255, null=True)),
                ('email', models.EmailField(
                    db_column='Email', max_length=254, unique=True)),
                ('password', models.CharField(db_column='Password', max_length=255)),
                ('is_staff', models.BooleanField(
                    db_column='IsStaff', default=False)),
                ('is_superuser', models.BooleanField(
                    db_column='IsSuperuser', default=False)),
                ('is_active', models.BooleanField(
                    db_column='IsActive', default=True)),
                ('registration_date', models.DateTimeField(
                    auto_now_add=True, db_column='RegistrationDate')),
                ('last_login', models.DateTimeField(
                    blank=True, db_column='LastLoginDate', null=True)),
                ('overall_rating', models.DecimalField(
                    blank=True, db_column='OverallRating', decimal_places=2, max_digits=10, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
                 related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.',
                 related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'db_table': 'Users',
            },
        ),
        migrations.CreateModel(
            name='PaymentMethod',
            fields=[
                ('MethodID', models.AutoField(
                    db_column='MethodID', primary_key=True, serialize=False)),
                ('MethodName', models.CharField(
                    db_column='MethodName', max_length=255)),
                ('MethodType', models.CharField(choices=[
                 ('Online', 'Online'), ('Offline', 'Offline')], db_column='MethodType', max_length=10)),
                ('Description', models.TextField(db_column='Description')),
                ('Status', models.BooleanField(db_column='Status')),
            ],
            options={
                'db_table': 'PaymentMethods',
            },
        ),
        migrations.CreateModel(
            name='WhiskyDetail',
            fields=[
                ('ItemID', models.AutoField(db_column='ItemID',
                 primary_key=True, serialize=False)),
                ('StartPrice', models.DecimalField(
                    db_column='StartPrice', decimal_places=2, max_digits=10)),
                ('BuyNowPrice', models.DecimalField(
                    db_column='BuyNowPrice', decimal_places=2, max_digits=10)),
                ('HighestBid', models.DecimalField(db_column='HighestBid',
                 decimal_places=2, max_digits=10, null=True)),
                ('Description', models.TextField(db_column='Description')),
                ('AuctionStatus', models.CharField(choices=[('Active', 'Active'), ('Inactive', 'Inactive'), (
                    'Canceled', 'Canceled')], db_column='AuctionStatus', max_length=10)),
                ('StartTime', models.DateTimeField(db_column='StartTime')),
                ('EndTime', models.DateTimeField(db_column='EndTime')),
                ('Category', models.CharField(db_column='Category', max_length=255)),
                ('Availability', models.BooleanField(db_column='Availability')),
                ('Condition', models.CharField(choices=[('Unopened', 'Unopened'), ('OpenedButSealed', 'OpenedButSealed'), (
                    'OpenedWithoutSeal', 'OpenedWithoutSeal')], db_column='Condition', max_length=20)),
                ('TastingNotes', models.TextField(db_column='TastingNotes')),
                ('Region', models.CharField(db_column='Region', max_length=255)),
                ('SellerID', models.ForeignKey(db_column='SellerID',
                 on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'WhiskyDetails',
            },
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('TransactionID', models.AutoField(
                    db_column='TransactionID', primary_key=True, serialize=False)),
                ('FinalPrice', models.DecimalField(
                    db_column='FinalPrice', decimal_places=2, max_digits=10)),
                ('TransactionStatus', models.CharField(choices=[('Initiated', 'Initiated'), (
                    'Completed', 'Completed'), ('Cancelled', 'Cancelled')], db_column='TransactionStatus', max_length=10)),
                ('PaymentStatus', models.CharField(choices=[('Pending', 'Pending'), (
                    'Completed', 'Completed'), ('Failed', 'Failed')], db_column='PaymentStatus', max_length=10)),
                ('UPSTrackingNumber', models.CharField(blank=True,
                 db_column='UPSTrackingNumber', max_length=255, null=True)),
                ('TransactionDate', models.DateTimeField(
                    db_column='TransactionDate')),
                ('BuyerID', models.ForeignKey(db_column='BuyerID', on_delete=django.db.models.deletion.CASCADE,
                 related_name='transactions_as_buyer', to=settings.AUTH_USER_MODEL)),
                ('ItemID', models.ForeignKey(db_column='ItemID',
                 on_delete=django.db.models.deletion.CASCADE, to='whisky_app.whiskydetail')),
                ('PaymentMethodID', models.ForeignKey(db_column='PaymentMethodID',
                 on_delete=django.db.models.deletion.CASCADE, to='whisky_app.paymentmethod')),
                ('SellerID', models.ForeignKey(db_column='SellerID', on_delete=django.db.models.deletion.CASCADE,
                 related_name='transactions_as_seller', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'Transactions',
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('ReviewID', models.AutoField(
                    db_column='ReviewID', primary_key=True, serialize=False)),
                ('Rating', models.DecimalField(
                    db_column='Rating', decimal_places=2, max_digits=3)),
                ('Comment', models.TextField(db_column='Comment')),
                ('CommentTime', models.DateTimeField(
                    db_column='CommentTime', default=django.utils.timezone.now)),
                ('IsDeleted', models.BooleanField(
                    db_column='IsDeleted', default=False)),
                ('ItemID', models.ForeignKey(db_column='ItemID',
                 on_delete=django.db.models.deletion.CASCADE, to='whisky_app.whiskydetail')),
                ('RevieweeID', models.ForeignKey(db_column='RevieweeID', on_delete=django.db.models.deletion.CASCADE,
                 related_name='reviewee_reviews', to=settings.AUTH_USER_MODEL)),
                ('ReviewerID', models.ForeignKey(db_column='ReviewerID', on_delete=django.db.models.deletion.CASCADE,
                 related_name='reviewer_reviews', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'Reviews',
            },
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('MessageID', models.AutoField(
                    db_column='MessageID', primary_key=True, serialize=False)),
                ('Content', models.TextField(db_column='Content')),
                ('SendTime', models.DateTimeField(db_column='SendTime')),
                ('IsSensitive', models.BooleanField(db_column='IsSensitive')),
                ('ReceiverID', models.ForeignKey(db_column='ReceiverID', on_delete=django.db.models.deletion.CASCADE,
                 related_name='received_messages', to=settings.AUTH_USER_MODEL)),
                ('RelatedItemID', models.ForeignKey(db_column='RelatedItemID', null=True,
                 on_delete=django.db.models.deletion.SET_NULL, to='whisky_app.whiskydetail')),
                ('SenderID', models.ForeignKey(db_column='SenderID', on_delete=django.db.models.deletion.CASCADE,
                 related_name='sent_messages', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'Messages',
            },
        ),
        migrations.CreateModel(
            name='Bid',
            fields=[
                ('BidID', models.AutoField(primary_key=True, serialize=False)),
                ('BidAmount', models.DecimalField(
                    db_column='BidAmount', decimal_places=2, max_digits=10)),
                ('BidTime', models.DateTimeField(db_column='BidTime')),
                ('BidderID', models.ForeignKey(db_column='BidderID',
                 on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('ItemID', models.ForeignKey(db_column='ItemID',
                 on_delete=django.db.models.deletion.CASCADE, to='whisky_app.whiskydetail')),
            ],
            options={
                'db_table': 'Bids',
            },
        ),
    ]
