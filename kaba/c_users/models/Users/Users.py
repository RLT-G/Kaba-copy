# from django.contrib.auth.models import UserManager
from c_users.managers import UserManager
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.core.mail import send_mail
from django.db import models
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField


class User(AbstractBaseUser, PermissionsMixin):

    date_joined = models.DateTimeField('Дата регистрации', auto_now_add=True)
    balance = models.IntegerField('Баланс', blank=True, default=0)
    referral_token = models.CharField('Объект рефера', max_length=255, null=True, default=None, blank=True)
    STATUS = (
        ('0', 'администратор'),
        ('1', 'добросовестный пользователь'),
        ('2', 'одно предупреждение'),
        ('3', 'два предупреждения'),
        ('4', 'заблокирован')
    )
    status = models.CharField('Статус', max_length=30, choices=STATUS, default='1')
    email = models.EmailField('Электронная почта', unique=True, blank=False)
    phoneNumber = PhoneNumberField('Номер телефона', default=None, unique=True, blank=True, null=True)
    avatar = models.ImageField('Изображение аватара', upload_to='avatars/', null=True, blank=True, default=None)
    first_name = models.CharField('Имя пользователя', max_length=30, blank=True, null=True, default=None)
    GENDERS = (
        ('m', 'Мужчина'),
        ('f', 'Женщина')
    )
    gender = models.CharField('Пол', max_length=1, choices=GENDERS, null=True)
    birthday = models.DateField('Дата рождения', blank=True, null=True)
    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_("Designates whether the user can log into this admin site."),
    )
    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )

    objects = UserManager()

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "email"

    class Meta:
        verbose_name = _("Пользователь")
        verbose_name_plural = _("Пользователи")

    def get_full_name(self):
        full_name = "%s %s" % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        return self.first_name
