from django.contrib import admin
from .models import CompanyGroup,BankAccount,Client,Movement,TypeofPayment

# Register your models here.
def make_checked(modeladmin, request, queryset):
    queryset.update(checked='1')
make_checked.short_description = "Mark selected movements as checked"

class MovementAdmin(admin.ModelAdmin):
    list_display = ['bank', 'amount','type','expiration_date']
    ordering = ['expiration_date']
    actions = [make_checked]

class BankInLine (admin.TabularInline):
    model=BankAccount
    choice=4

class CompanyGroupAdmin(admin.ModelAdmin):

    inlines = [BankInLine]

admin.site.register(CompanyGroup,CompanyGroupAdmin)

admin.site.register(Client)

admin.site.register(Movement,MovementAdmin)

admin.site.register(TypeofPayment)
