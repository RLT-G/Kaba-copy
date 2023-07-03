from django.contrib import admin
from c_users.models.Users.Users import *

my_models = [User]
for el in my_models:
    admin.site.register(el)
