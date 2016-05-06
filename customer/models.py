from django.db import models
from django.utils import timezone

# Create your models here.
class Customer(models.Model):
	
	SEX = ( ('M',"Male") , ('F',"Female") )
	customer_name = models.CharField(max_length=128,blank=False)
	customer_phone = models.IntegerField(default=0)
	customer_email = models.EmailField(max_length=128,blank=True)
	customer_age = models.IntegerField(default=0)
	customer_sex = models.CharField(max_length=1,choices=SEX,default='M')
	customer_details = models.CharField(max_length=500,blank=True)	

	def __str__(self):
		return self.customer_name

class Order(models.Model):
	
	STATUS = ( ("1","BOOKED"),("2","COMPLETED"),("3","DELIVERED"))	
	AMOUNT_STATUS = ( ("1","UNPAID"),("2","PAID"))	
	ordered_by = models.ForeignKey(Customer)
	order_name = models.CharField(max_length = 256,blank=True)
	order_date = models.DateField(auto_now_add = True)
	order_details = models.CharField(max_length=500,blank=True)
	order_amount = models.IntegerField(default = 0)
	order_status = models.CharField(max_length = 1,choices = STATUS,default='1')
	order_amount_status = models.CharField(max_length =1,choices=AMOUNT_STATUS,default='1')

	def __str__(self):
		return self.order_name + " " + self.ordered_by.customer_name


	

