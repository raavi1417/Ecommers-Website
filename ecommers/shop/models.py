from django.db import models

# Create your models here.
class Product(models.Model):
    product_id=models.AutoField
    product_name=models.CharField(max_length=100)
    cat=models.CharField(max_length=100,default="")
    sub_cat=models.CharField(max_length=100,default="")
    price=models.IntegerField(default=0)
    img=models.ImageField(upload_to='shop/images',default="") 
    desc=models.TextField()
    pub_date=models.DateField()
    def __str__(self):
        return self.product_name
class Contact(models.Model):
    msg_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    email=models.EmailField()
    phone=models.IntegerField()
    message=models.TextField()
    
    def __str__(self):
        return self.name
class Order(models.Model):
    order_id=models.AutoField(primary_key=True)
    item_json=models.CharField(max_length=500)
    name=models.CharField(max_length=100)
    email=models.EmailField()
    address1=models.CharField(max_length=200)
    address2=models.CharField(max_length=200)
    city=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    zip_code=models.IntegerField()
    phone=models.IntegerField()
    alter_phone=models.IntegerField()
    def __str__(self):
        return "order-no"+str(self.order_id)
class orderUpdate(models.Model):
    update_id=models.AutoField(primary_key=True)
    order_id=models.IntegerField(default="")
    update_desc=models.TextField()
    timestamp=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.update_desc[0:10] +"......"

