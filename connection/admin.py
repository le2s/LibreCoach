from django.contrib import admin
from connection.models import ContactF, SuperUser, Disponibilite
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User


# Define an inline admin descriptor for Employee model
# which acts a bit like a singleton
class SuperUserInline(admin.StackedInline):
    model = SuperUser
    can_delete = False
    verbose_name_plural = 'superuser'

# Define a new User admin
class UserAdmin(UserAdmin):
    inlines = (SuperUserInline, )

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Disponibilite)
# Register your models here.







