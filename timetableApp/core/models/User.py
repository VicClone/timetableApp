import uuid
from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.utils.translation import gettext as _
import datetime
from django.utils import timezone
from ..managers import UserManager

class User(AbstractBaseUser, PermissionsMixin):
    """ 
    Model of user
    """

    uid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    login = models.CharField(max_length=50, unique=True)
    email = models.EmailField(default=None, null=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)

    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'login'
    REQUIRED_FIELDS = []

    @property
    def get_fullname(self):
        return '%s %s' % (self.first_name, self.last_name)

    class Meta:
        db_table = 'users'