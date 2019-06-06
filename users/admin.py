from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from django.contrib.auth.models import User
from users.models import Profile
# Register your models here.
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """Profile admin."""
    list_display = ('pk', 'user', 'phone', 'website', 'picture')
    list_display_links = ('pk', 'user')
    list_editable = ('phone', 'website', 'picture')
    search_fields = ('user__username', 'user__email', 'user__first_name', 'user__last_name', 'phone')
    list_filter = ('user__is_active', 'user__is_staff','created_at', 'updated_at')

    fieldsets = (
      ('Profile', {
          'fields': (('user', 'picture'),),
      }),
      ('Extra Info', {
          'fields': (
            ('website', 'phone'),
            ('biography'),
          ),
      }),
      ('Meta Data', {
        'fields': (('created_at', 'updated_at'),)
      })
    )

    readonly_fields = ('created_at', 'updated_at')

class ProfileInline(admin.StackedInline):
    """Profile in-line admin for users"""
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profiles'

class UserAdmin(BaseUserAdmin):
    """Add profile admin to base user admin"""
    inlines = (ProfileInline,)
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_active', 'is_staff')

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
