from django.contrib import admin
from Authentication.models import user_detail,providerdetails

# Register your models here.

admin.site.register(user_detail)
admin.site.register(providerdetails)

