from django.shortcuts import render
from django.http import HttpResponse
from customer.models import Order
from customer.models import Customer
from django.http import JsonResponse
# Create your views here.


def recentOrders(request):
	orders_list = Order.objects.all()
	recent_orders_list = Order.objects.order_by('-order_date')[:25]
	#output = ','.join([p.order_name for p in recent_orders_list])
	context_dict = {'orders_list':recent_orders_list}
	return render(request,"orders.html",context_dict)

def testView(request):
	return render(request,"index.html")

def searchView(request):
	name  = request.GET.get('name')
	data = [] 	
	if name:	
		customers = Customer.objects.filter(customer_name__icontains = name)
		print(customers)
		data = [ {'id':customer.id,'name':customer.customer_name } for customer in customers]
	return JsonResponse(data={'customers':data})


def orderView(request):
	cid  = request.GET.get('id')
	data = []
		
	if cid:	
		orders = Order.objects.filter(ordered_by__id=cid).order_by('-order_date')
		print(orders)
		data = [ {'id':o.id,'name':o.order_name, 'date':o.order_date,'order_status':o.order_status,'amount':o.order_amount,'amount_status':o.order_amount_status } for o in orders]
	return JsonResponse(data={'orders':data})

def filterOrdersView(request):
	status  = request.GET.get('orderStatus')
	data = []
	orders =[]	
	if(status == '0'):
		orders = Order.objects.all().order_by('-order_date')[:50]		
	else:	
		orders = Order.objects.filter(order_status = status).order_by('-order_date')[:50]
		#print(orders)
	data = [ {'id':o.id,'name':o.order_name, 'date':o.order_date,'order_status':o.order_status,'amount':o.order_amount,'amount_status':o.order_amount_status } for o in orders]
	return JsonResponse(data={'orders':data})

def customersView(request):
	customers_list = Customer.objects.all()
	recent_customers_list = Customer.objects.order_by('customer_name')
	#output = ','.join([p.order_name for p in recent_orders_list])
	urlList = []	
	#for x in recent_customers_list:
	#	urlList.append("/admin/customer/customer/"+x.id+"/change/")
	context_dict = {'customers_list':recent_customers_list}
	return render(request,"customers.html",context_dict)
def updateCardView(request):
	id  = request.GET.get('id')
	data = []
		
	customers = Customer.objects.filter(id = id)
	data = [ {'id':customer.id,'name':customer.customer_name ,'age':customer.customer_age ,'sex':customer.customer_sex ,'email':customer.customer_email
,'phone':customer.customer_phone ,'details':customer.customer_details } for customer in customers]
	print(data)
	return JsonResponse(data={'customers':data})
