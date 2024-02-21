from django.urls import path
from accountapp import views

urlpatterns=[
    path('',views.index,name='home'),
    path('vendor/',views.vnd_views,name='vendor'),
    path('customer/',views.cst_views,name='customer'),
]
