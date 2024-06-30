from django.contrib import admin

from users.models import User


@admin.register(User)
class UserAdmin(admin.Admin):
    list_display = ('pk', 'first_name', 'last_name', 'email', 'role')
