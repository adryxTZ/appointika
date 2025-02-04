from django.contrib import admin

from user.models import User


# Register your models here.
class UserProfile(admin.ModelAdmin):
    list_display = ["id", "email", "role", 'first_name', 'last_name', 'phone', 'gender']


#
#
admin.site.register(User, UserProfile)
