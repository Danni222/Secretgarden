from django.db import models
from datetime import date
from datetime import datetime, timedelta
from django.utils import timezone
class Customer(models.Model):
#max_length is the maximum number of characters allowed on the field
#blank = if true, allows the user to leave it blank on a form using this model#null = if true, allows  the field to be empty#primary_key = if true, indicates that the field is the primary key for the model
#verbose_name is the label of the field displayed on a form when using this model#help_text can be used to provide instructions on the input for the field
 fname = models.CharField(max_length=30,verbose_name='First Name', blank=False,null=False)
 lname = models.CharField(max_length=30,verbose_name='Last Name', blank=False,null=False)
#the databsase field is not allowed to be null and the form field is not allowed to be blank.
#this is the primary key 
 email = models.EmailField(null=False,verbose_name='Email',blank=False,primary_key=True)
 phoneNumber =models.CharField(max_length=12,verbose_name='phoneNumber',null=False,blank=False)
 

 password=models.CharField(max_length=100,verbose_name='Password', help_text='Please use at least one uppercase and a number', null=False,blank=False)
#auto_now_add is used to set the field to now when the object is first created 
#auto_now is false to do not update the field when the record is updated
 registeredDate=models.DateTimeField(auto_now_add=True,auto_now=False)
#auto_now_add is false to allow to update this field every time the record is updated#auto_now is true to update the field with current date
 updatedDate=models.DateTimeField(auto_now_add=False,auto_now=True)

class Product(models.Model):
    producttype=(('Collection','Collection'),('Flower','Flower'),('Plant','Plant'),
                 ('Accessory','Accessory'))

    productID=models.AutoField(primary_key=True)
    created=models.DateTimeField(auto_now_add=True)
    productname=models.CharField(max_length=50,verbose_name='ProductName', blank=False, null=False)
    productdescription=models.CharField(max_length=300,verbose_name='ProductDescription', blank=False, null=False)
    producttype=models.CharField(choices=producttype,max_length=100,verbose_name='ProductType',null=False,blank=False,default=None)
    productprice=models.DecimalField(max_digits=7,decimal_places=2)
    productimage=models.ImageField(upload_to='product')

    class Meta:
        ordering = ('-created',)
    def __str__(self):
        return 'product {}'.format(self.productID)
    
class Flower(models.Model):
    categoryList=(('Rose','Rose'),('Lily','Lily'),('Tulip','Tulip'),
                  ('Calla Lily','Calla Lily'),('Gilly Flower','Gilly Flower'),
                  ('Sunflower','Sunflower'),('Peruvian Lily','Peruvian Lily'),
                  ('Gerbera Daisies','Gerbera Daisies'))
    colorList=(('Red','Red'),('White','White'),('Pink','Pink'),
                  ('Yellow','Yellow'),('Purple','Purple'),
                  ('Orange','Orange'),('More Than one','More Than One'))
    flowerCategory=(('Romantic Love','Romantic Love'),('Friendship','Friendship'),
                    ('Family','Family'))
    productID=models.ForeignKey('Product')
    created=models.DateTimeField(auto_now_add=True)  
    flowertype=models.CharField(choices=categoryList,max_length=100,verbose_name='FlowerType',null=False,blank=False,default=None)
    flowercolor=models.CharField(choices=colorList,max_length=100,verbose_name='FlowerColor',null=False,blank=False,default=None)
    flowerdiyocategory=models.CharField(choices=flowerCategory,max_length=100,verbose_name='Category',null=False,blank=False,default=None)
    updatedDate=models.DateTimeField(auto_now_add=False,auto_now=True)

    class Meta:
        unique_together=(('productID','flowertype','flowercolor','flowerdiyocategory'),)
        ordering = ('-created',)
    def __str__(self):
        return 'flower {}'.format(self.productID)


class Collection(models.Model):
    collectionType=(('Birthday','Birthday'),('Anniversary','Anniversary'),
                    ('Sympathy','Sympathy'))
    productID=models.ForeignKey('Product')
    bestseller = models.BooleanField(default=False)
    collectiontype=models.CharField(choices=collectionType,max_length=100,verbose_name='CollectionType',null=False,blank=False,default=None)
    updatedDate=models.DateTimeField(auto_now_add=False,auto_now=True)
    def __str__(self):
        return 'collection {}'.format(self.productID)
    class Meta:
        unique_together=(('productID','collectiontype'),)
    
class Order(models.Model):
    citys=(('McAllen','McAllen'),('Edinburg','Edinburg'),
                    ('Mission','Mission'))
    orderID=models.AutoField(primary_key=True)
    email=models.EmailField(null=False,verbose_name='Email',blank=False)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)
    address = models.CharField(max_length=250, verbose_name='Address',null=False,blank=False,default=None)
    postalCode = models.CharField(max_length=20, verbose_name='Zip Code',null=False,blank=False,default=None)
    city = models.CharField(choices=citys,max_length=100,verbose_name='City',null=False,blank=False,default=None)
    makebouquet=models.BooleanField(default=False)
    deliverydate=models.DateField(default=timezone.now()+timedelta(days=1),null=False,blank=False,verbose_name='date')
    
    class Meta:
        ordering = ('-created',)
    def __str__(self):
        return 'Order {}'.format(self.orderID)
    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())

class OrderItem(models.Model):
    orderItemID=models.AutoField(primary_key=True)
    orderID = models.ForeignKey('Order', related_name='items')    
    productID = models.ForeignKey('Product', related_name='order_items')  
    price = models.DecimalField(max_digits=9, decimal_places=2)    
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return '{}'.format(self.orderItemID)
    
    def get_cost(self):
        return self.price * self.quantity


