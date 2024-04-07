# Generated by Django 3.2 on 2024-04-07 05:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('UserID', models.AutoField(primary_key=True, serialize=False)),
                ('Username', models.CharField(max_length=255)),
                ('Email', models.EmailField(max_length=254, unique=True)),
                ('Password', models.CharField(max_length=255)),
                ('UserType', models.CharField(choices=[('Admin', 'Admin'), ('Normal', 'Normal')], max_length=10)),
                ('RegistrationDate', models.DateTimeField()),
                ('LastLoginDate', models.DateTimeField(blank=True, null=True)),
                ('IsBlocked', models.BooleanField(default=False)),
                ('OverallRating', models.DecimalField(blank=True, decimal_places=2, max_digits=3, null=True)),
            ],
            options={
                'db_table': 'Users',
            },
        ),
        migrations.CreateModel(
            name='WhiskyDetail',
            fields=[
                ('ItemID', models.AutoField(db_column='ItemID', primary_key=True, serialize=False)),
                ('StartPrice', models.DecimalField(db_column='StartPrice', decimal_places=2, max_digits=10)),
                ('BuyNowPrice', models.DecimalField(db_column='BuyNowPrice', decimal_places=2, max_digits=10)),
                ('Description', models.TextField(db_column='Description')),
                ('AuctionStatus', models.CharField(choices=[('Active', 'Active'), ('Inactive', 'Inactive'), ('Canceled', 'Canceled')], db_column='AuctionStatus', max_length=10)),
                ('StartTime', models.DateTimeField(db_column='StartTime')),
                ('EndTime', models.DateTimeField(db_column='EndTime')),
                ('Category', models.CharField(db_column='Category', max_length=255)),
                ('Availability', models.BooleanField(db_column='Availability')),
                ('Condition', models.CharField(choices=[('Unopened', 'Unopened'), ('OpenedButSealed', 'OpenedButSealed'), ('OpenedWithoutSeal', 'OpenedWithoutSeal')], db_column='Condition', max_length=20)),
                ('TastingNotes', models.TextField(db_column='TastingNotes')),
                ('Region', models.CharField(db_column='Region', max_length=255)),
                ('SellerID', models.ForeignKey(db_column='SellerID', on_delete=django.db.models.deletion.CASCADE, to='whisky_app.user')),
            ],
            options={
                'db_table': 'WhiskyDetails',
            },
        ),
        migrations.CreateModel(
            name='Bid',
            fields=[
                ('BidID', models.AutoField(primary_key=True, serialize=False)),
                ('BidAmount', models.DecimalField(db_column='BidAmount', decimal_places=2, max_digits=10)),
                ('BidTime', models.DateTimeField(db_column='BidTime')),
                ('BidderID', models.ForeignKey(db_column='BidderID', on_delete=django.db.models.deletion.CASCADE, to='whisky_app.user')),
                ('ItemID', models.ForeignKey(db_column='ItemID', on_delete=django.db.models.deletion.CASCADE, to='whisky_app.whiskydetail')),
            ],
            options={
                'db_table': 'Bids',
            },
        ),
    ]