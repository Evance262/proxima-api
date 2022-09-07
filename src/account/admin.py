from django.contrib import admin
from account.models import Identity
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseAdmin

from django.contrib.auth import get_user_model

User = get_user_model()


class IdentityInline(admin.StackedInline):
    model = Identity
    extra = 1


class UserAdmin(BaseAdmin):
    list_display = ['username', 'first_name', 'last_name', 'gender',]
    inlines = [IdentityInline,]
    search_fields = ['username', 'first_name', 'last_name']
    ordering = ('gender',)
    add_fieldsets = (
        (None, {
            'fields': ('username', 'first_name', 'last_name', 'email', 'gender', 'date_of_birth', 
            'password1', 'password2',)
        }),
        ('permissions', {
            'fields': ('is_superuser',)
        })
    )
    fieldsets = (
        (None, {
                'fields': ('username', 'first_name', 'last_name', 'password')
        }),
        ('permissions', {
            'fields': ('is_superuser',)
        })
    )


admin.site.register(User, UserAdmin)