from django.contrib.auth import password_validation
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.core import signing
from django.db import models

from jijoo.utils import TimeStampMixin, validate_ng_mobile_number, validate_state


class UserManager(BaseUserManager):
    def create_user(self, email, password, lastname, firstname, **extrafields):
        if not email:
            ValueError("Email field is required")
        if not firstname:
            ValueError("Firstname field is required")
        if not lastname:
            ValueError("Lastname field is required")
        if not password:
            ValueError("Password field is required")

        user = self.model(
            email=self.normalize_email(email),
            password=password,
            firstname=firstname,
            lastname=lastname,
            **extrafields
        )

        user.is_active = True
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_superuser(self, email, password, lastname, firstname, **extra_fields):
        extra_fields.setdefault("is_superuser", True)
        user = self.create_user(email, password, lastname, firstname, **extra_fields)
        user.is_admin = True
        # used by the PermissionsMixin to
        # grant all permissions
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin, TimeStampMixin):
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    email = models.EmailField(
        max_length=50,
        unique=True,
        error_messages={"unique": "A user with this email already exists"},
    )
    password = models.CharField(
        max_length=128, validators=[password_validation.validate_password]
    )
    mobile = models.CharField(
        max_length=20, blank=True, null=True, validators=[validate_ng_mobile_number]
    )
    city = models.CharField(max_length=30, blank=True, null=True)
    state = models.CharField(max_length=30, validators=[validate_state])

    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    REQUIRED_FIELDS = ["firstname", "lastname", "password"]
    USERNAME_FIELD = "email"

    def __str__(self):
        return "{}".format(self.email)

    def save(self, *args, **kwargs):
        self.firstname = self.firstname.title().strip()
        self.lastname = self.lastname.title().strip()
        return super(User, self).save(*args, **kwargs)

    def has_module_perms(self, app_label):
        return True

    def get_username(self):
        return self.email

    def get_full_name(self):
        """
        Return the first_name plus the last_name, with a space in between.
        """
        full_name = "%s %s" % (self.firstname, self.lastname)
        return full_name.strip()

    def get_short_name(self):
        """Return the short name for the user."""
        return self.firstname

    @property
    def is_staff(self):
        return self.is_admin
