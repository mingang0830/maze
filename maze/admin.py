from django.contrib import admin
from .models import User, Now


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'username',
        'password'
    )


# Register your models here.
