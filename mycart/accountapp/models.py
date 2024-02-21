from django.db import models

# Create your models here.
class customer(models.Model):
    username=models.CharField(max_length=50)
    first_name=models.CharField(max_length=50,blank=True,default=None,null=True)
    last_name=models.CharField(max_length=50)
    user_email=models.EmailField()
    user_phone_no=models.IntegerField()
    user_address1=models.CharField(max_length=100)
    user_address2=models.CharField(max_length=100)
    street=models.CharField(max_length=50)
    city=models.CharField(max_length=50)
    state=models.CharField(max_length=50)
    pincode=models.IntegerField
    password1=models.CharField(max_length=30)
    password2=models.CharField(max_length=30)

class vendor(models.Model):
    vendor_name=models.CharField(max_length=50)
    shop_name=models.CharField(max_length=50)
    shop_address=models.CharField(max_length=100)
    shop_licience=models.ImageField(blank=True,upload_to='licience')
    vendor_email=models.EmailField()
    vendor_phone=models.IntegerField()
    pswd1=models.CharField(max_length=30)
    pswd2=models.CharField(max_length=30)
    is_approved=models.BooleanField(default=False)
