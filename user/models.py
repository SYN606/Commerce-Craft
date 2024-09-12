from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.utils.translation import gettext_lazy as _


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError(_("The Email field must be set"))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))

        return self.create_user(email, password, **extra_fields)


class Address(models.Model):
    landmark = models.CharField(max_length=255, blank=True, null=False)
    house_number = models.CharField(max_length=255, blank=True, null=False)
    area = models.CharField(max_length=255, blank=False, null=False)
    pincode = models.IntegerField()
    district = models.CharField(max_length=255, blank=False, null=False)
    state = models.CharField(max_length=255, blank=False, null=False)

    def __str__(self) -> str:
        return self.area + self.district + self.pincode # type: ignore

class Profile(models.Model):
    avatar = models.ImageField(
        upload_to="profile_avatars",
    )
    gender = models.CharField(max_length=10, blank=True, null=True)
    address = models.OneToOneField(
        Address, on_delete=models.CASCADE, blank=True, null=True
    )
    

class User(AbstractUser):
    first_name = None
    last_name = None
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255, blank=True, null=False)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    user_profile = models.OneToOneField(
        Profile, on_delete=models.CASCADE, blank=True, null=True
    )
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name","username"]

    objects = CustomUserManager()  # type: ignore

    def __str__(self):
        return self.name
