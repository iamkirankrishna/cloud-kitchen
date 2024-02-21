from django.shortcuts import render
from accountapp.forms import vendor_form,customer_form

# Create your views here.
def index(request):
    return render(request,'index.html',{})

#...................................VENDOR views............
def vnd_views(request):
    vform=vendor_form()

    if request.method=='POST':
       vform= vendor_form(request.POST)

    return render(request,'vendor.html',{'vform':vform})

#.................................CUSTOMER views.........................
def cst_views(request):
    cform=customer_form()

    if request.method=='POST':
        cform=customer_form(request.POST)

    return render(request,'customer.html',{'cform':cform})