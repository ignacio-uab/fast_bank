# Create your models here.
from django.db import models
from django.utils import timezone
import datetime




class TypeofPayment (models.Model):
    payment_type = models.CharField(max_length=256)
    pub_date = models.DateTimeField('date added')
    type = models.CharField(max_length=24)
    prioridad = models.IntegerField (default=0)

    def __str__(self):
        return self.payment_type + " " + self.type


class CompanyGroup (models.Model):
    company_name = models.CharField(max_length=256)
    status_company = models.BooleanField (default =True)

    def __str__(self):
        return self.company_name

class BankAccount (models.Model):
    DIVISAS = (
        ('E', 'EUROS'),
        ('D', 'DOLARES'),
        ('L', 'LIBRAS'),
    )
    iban = models.CharField(max_length=40)
    bic = models.CharField(max_length=20)
    text = models.CharField(max_length=50)
    currency = models.CharField (max_length=1,choices=DIVISAS)
    company = models.ForeignKey(CompanyGroup, on_delete=models.CASCADE)

    def __str__(self):
        return self.bic + " " + self.text

class Client (models.Model):
    client_name = models.CharField(max_length=256)
    status_client = models.BooleanField (default=True)
    owner = models.ForeignKey(CompanyGroup, on_delete=models.CASCADE,default="")
    def __str__(self):
        return self.client_name

#class Currency (models.Model):
#    currency_name=models.CharField(max_length=128)
#    currency_symbol=models.CharField(max_length=8)
#
#    def __str__(self):
#        return self.currency_symbol


class Movement(models.Model):
#    company = models.ForeignKey(CompanyGroup, on_delete=models.CASCADE)
    FORECAST = (('C','Confirmado'),('P','Previsto'),('-','Abierto'))
#    bank = models.ForeignKey(BankAccount, on_delete=models.CASCADE)
    bank = models.OneToOneField(BankAccount, on_delete=models.CASCADE, primary_key= True)
    client = models.ForeignKey(Client,on_delete=models.CASCADE)
    type = models.ForeignKey(TypeofPayment, on_delete=models.CASCADE)
    movement_date = models.DateTimeField('date movement')
    expiration_date = models.DateTimeField('expiration date')
    text = models.CharField(max_length=256)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    estimacion = models.CharField(max_length=1, choices=FORECAST,default='-')
    checked = models.BooleanField (default=False)
#    currency=models.ForeignKey(Currency,on_delete=models.CASCADE)

    def __str__(self):
        return self.text

    def will_expire_inonemonth(self):
        return self.expiration_date >= timezone.now() - datetime.timedelta(days=30)

        will_expire_inonemonth.admin_order_field = 'expiration_date'
        will_expire_inonemonth.boolean = True
        will_expire_inonemonth.short_description = 'Vence en un mes?'
