from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin 
# Register your models here.
from account.models import Account


class AccountAdmin(UserAdmin):
    
    list_display=('pk','username', 'email', 'date_joined', 'last_login', 'is_admin', 'is_staff', )
    search_fields=('username', 'email',)
    readonly_fields= ('date_joined', 'last_login')
    filter_horizontal =()
    list_filter = (['id'])
    fieldsets = ()


admin.site.register(Account, AccountAdmin)