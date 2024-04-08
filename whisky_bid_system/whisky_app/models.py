from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.contrib.auth.models import Group, Permission


# # UserManager for custom user management functionalities

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)

        if not extra_fields.get('is_superuser'):
            raise ValueError('Superuser must have is_superuser=True.')
        if not extra_fields.get('is_staff'):
            raise ValueError('Superuser must have is_staff=True.')
        return self.create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    userid = models.AutoField(primary_key=True, db_column='UserID')
    username = models.CharField(
        max_length=255, unique=True, db_column='Username')
    first_name = models.CharField(
        max_length=255, null=True, blank=True, db_column='FirstName')
    last_name = models.CharField(
        max_length=255, null=True, blank=True, db_column='LastName')
    email = models.EmailField(unique=True, db_column='Email')
    password = models.CharField(max_length=255, db_column='Password')
    is_staff = models.BooleanField(default=False, db_column='IsStaff')
    is_superuser = models.BooleanField(default=False, db_column='IsSuperuser')
    is_active = models.BooleanField(default=True, db_column='IsActive')
    registration_date = models.DateTimeField(
        auto_now_add=True, db_column='RegistrationDate')
    last_login = models.DateTimeField(
        null=True, blank=True, db_column='LastLoginDate')

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta:
        db_table = 'Users'

    def get_full_name(self):
        # Assuming full name is a combination of first_name and last_name
        full_name = f"{self.first_name} {self.last_name}".strip()
        return full_name or self.username

    def get_short_name(self):
        # Assuming short name is the first name
        return self.first_name or self.username

# class User(models.Model):
#     UserID = models.AutoField(primary_key=True)
#     Username = models.CharField(max_length=255)
#     Email = models.EmailField(unique=True)
#     Password = models.CharField(max_length=255)
#     UserType = models.CharField(max_length=10, choices=[
#         ('Admin', 'Admin'), ('Normal', 'Normal')])
#     RegistrationDate = models.DateTimeField()
#     LastLoginDate = models.DateTimeField(null=True, blank=True)
#     IsBlocked = models.BooleanField(default=False)
#     OverallRating = models.DecimalField(
#         max_digits=3, decimal_places=2, null=True, blank=True)

#     class Meta:
#         db_table = 'Users'


class WhiskyDetail(models.Model):
    ItemID = models.AutoField(primary_key=True, db_column='ItemID')
    SellerID = models.ForeignKey(
        'User', on_delete=models.CASCADE, db_column='SellerID')
    StartPrice = models.DecimalField(
        max_digits=10, decimal_places=2, db_column='StartPrice')
    BuyNowPrice = models.DecimalField(
        max_digits=10, decimal_places=2, db_column='BuyNowPrice')
    HighestBid = models.DecimalField(
        max_digits=10, decimal_places=2, db_column='HighestBid', null=True)
    Description = models.TextField(db_column='Description')
    AuctionStatus = models.CharField(max_length=10, choices=[
        ('Active', 'Active'), ('Inactive', 'Inactive'), ('Canceled', 'Canceled')], db_column='AuctionStatus')
    StartTime = models.DateTimeField(db_column='StartTime')
    EndTime = models.DateTimeField(db_column='EndTime')
    Category = models.CharField(max_length=255, db_column='Category')
    Availability = models.BooleanField(db_column='Availability')
    Condition = models.CharField(max_length=20, choices=[
        ('Unopened', 'Unopened'), ('OpenedButSealed', 'OpenedButSealed'), ('OpenedWithoutSeal', 'OpenedWithoutSeal')],
        db_column='Condition')
    TastingNotes = models.TextField(db_column='TastingNotes')
    Region = models.CharField(max_length=255, db_column='Region')

    class Meta:
        db_table = 'WhiskyDetails'


class Bid(models.Model):
    BidID = models.AutoField(primary_key=True)
    ItemID = models.ForeignKey(
        'WhiskyDetail', on_delete=models.CASCADE, db_column='ItemID')
    BidderID = models.ForeignKey(
        'User', on_delete=models.CASCADE, db_column='BidderID')
    BidAmount = models.DecimalField(
        max_digits=10, decimal_places=2, db_column='BidAmount')
    BidTime = models.DateTimeField(db_column='BidTime')

    class Meta:
        db_table = 'Bids'
