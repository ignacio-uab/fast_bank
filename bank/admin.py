from django.contrib import admin
from .models import CompanyGroup,BankAccount,Client

# Register your models here.

class BankInLine (admin.TabularInline):
    model=BankAccount
    choice=4

class CompanyGroupAdmin(admin.ModelAdmin):

    inlines = [BankInLine]

admin.site.register(CompanyGroup,CompanyGroupAdmin)

admin.site.register(Client)

