from django.contrib import admin
from ad.models.ad_company.ad_company import *
# from ad.models.term.term import termModel

# Зарегистрировал ad_company
my_models = [ad_company_base]
for el in my_models:
    admin.site.register(el)
# admin.site.register(termModel)
