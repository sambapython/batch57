from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def fun(request):
	# takes the data from html form and fill into DB.
	# takes the data from DB and send to the front end as a report
	return HttpResponse(["cust1","cus2","cus3","cust4"])

