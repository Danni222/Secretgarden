from django.shortcuts import render
from store.models import Collection
from django.http import HttpResponse,HttpResponseRedirect
from store.forms import SignInForm
from store.forms import CustomerForm
from store.forms import CartAddProductForm
from store.forms import OrderCreateForm
from store.forms import OrderCreateBouquetForm
from .cart import Cart
from store.models import Product
from store.models import Customer
from store.models import Collection
from store.models import Flower
from store.models import Order
from store.models import OrderItem
from django.shortcuts import redirect, get_object_or_404
from django.core.urlresolvers import reverse
from django.core.mail import send_mail
from django.conf import settings
from django.template import RequestContext
from django.template.loader import get_template
from email.mime.image import MIMEImage
from django.core.mail import EmailMultiAlternatives
from django.template import Context
from datetime import date
# Create your views here.

def homepage(request):
 #   if request.session['signin']:
  #      user=User(requestion)
   # if request.method=='POST':
    #    if request.POST.get('signin')=='signin':
    if request.session.has_key('customerName'):
        customerName=request.session.get('customerName')
    if request.session.has_key('customerEmail'):
        customerEmail=request.session.get('customerEmail')
    if request.session.has_key('coltype'):
        coltype=request.session.get('coltype')

    if ((request.POST.get('submit')=='Cart')):
        return redirect ('shoppingcart')
    homeProInf=Product.objects.filter(collection__bestseller=True)     
    return render (request,'homepage.html',locals())

def menuproduct(request,menutype):
    if request.session.has_key('customerName'):
        customerName=request.session.get('customerName')
    if request.session.has_key('customerEmail'):
        customerEmail=request.session.get('customerEmail')
    

    if ((request.POST.get('submit')=='Cart')):
        return redirect ('shoppingcart')
    
    if (str(menutype)=='bestseller'):        
        productlist=Product.objects.filter(collection__bestseller=True)
        request.session['coltype']='bestseller'
        
    elif (str(menutype)=='birthday'):        
        productlist=Product.objects.filter(collection__collectiontype='Birthday')
        request.session['coltype']='birthday'
        
    elif (str(menutype)=='anniversary'):        
        productlist=Product.objects.filter(collection__collectiontype='Anniversary')
        request.session['coltype']='anniversary'
        
    elif (str(menutype)=='sympathy'):        
        productlist=Product.objects.filter(collection__collectiontype='Sympathy')
        request.session['coltype']='sympathy'

    elif (str(menutype)=='love'):        
        productlist=Product.objects.filter(flower__flowerdiyocategory='Romantic Love')
        request.session['coltype']='love'

    elif (str(menutype)=='family'):        
        productlist=Product.objects.filter(flower__flowerdiyocategory='Family')
        request.session['coltype']='family'

    elif (str(menutype)=='friendship'):        
        productlist=Product.objects.filter(flower__flowerdiyocategory='Friendship')
        request.session['coltype']='friendship'
    else:
        productlist=Product.objects.filter(collection__bestseller=True)
        request.session['coltype']='bestseller'

    return render (request,'menuproduct.html',locals())


def signin(request):

    #if this is a POST request, process the data
    if request.method == 'POST':
        #create a form instance and populate it with data from the request
        form = SignInForm(request.POST)
        #check if this form is valid based on field rules
        if ((request.POST.get('submit')=='Cart')):
            return redirect ('shoppingcart')
        if (form.is_valid()):
            #if is_valid() method returns true, the form's data is place
            #in its cleaned_data attribute
            #Query Customer table to find out if the email address and password provided exists in Customer table

            registeredUser=Customer.objects.filter(email=form.cleaned_data['email'],
                                                   password=form.cleaned_data['password'])
            #user exists in Customer table then retrieve customer name and redirect to welcome url
            if registeredUser.exists():
                 for user in registeredUser:
                    customerName=user.fname + ' ' + user.lname
                    customerEmail=user.email
                 request.session['customerEmail']=customerEmail
                 request.session['customerName']=customerName
                 return HttpResponseRedirect('/homepage/') 

            else:
                message2='Incorrect username or password, please try again:'
                form=SignInForm()            
    else:
        form = SignInForm() 
    return render(request, 'signin.html', locals())

def signout(request):
    if ((request.POST.get('submit')=='Cart')):
        return redirect ('shoppingcart')
    del request.session['customerEmail']
    del request.session['customerName']
    del request.session['cart']
    del request.session['coltype']
    return HttpResponseRedirect('/homepage/')

def register(request):
    if ((request.POST.get('submit')=='Cart')):
        return redirect ('shoppingcart')
    if request.method == 'POST':
          #create a form instance and populate it with data from the request
          form = CustomerForm(request.POST)
          #check if this form is valid based on the rules provided to the fields under the customer model
          if (form.is_valid()):
               #save() method accepts an optional commit keyword argument,
               #which accepts either True or False, where commit is true by default.
               #if commit=false, then it will return an object that hasn’t yet been 
               #saved to the database.  This is useful if you want to preprocess the data or change it
               newCustomer=form.save()
               #you can modify the input data at this point if needed or use it 
               customerName=newCustomer.fname + ' ' + newCustomer.lname

               #save record to Customer Model
               #newCustomer.save()
               #go to welcome.html template if customer record was added successfully
               #go to welcome.html template if customer record was added successfully
              #create session variables for welcome view to use them
               request.session['customerEmail']=newCustomer.email
               request.session['customerName']=customerName
               newCustomer.save()
               return HttpResponseRedirect('/homepage/')

    else:
          #If not POST then set form to BLANK Customer form (with no POST variables)
          form = CustomerForm()
    return render(request, 'register.html', locals())

def productdetails(request,productID):
    if request.session.has_key('customerName'):
        customerName=request.session.get('customerName')
    if request.session.has_key('customerEmail'):
        customerEmail=request.session.get('customerEmail')
    if request.session.has_key('coltype'):
        coltype=request.session.get('coltype')
    if ((request.POST.get('submit')=='Cart')):
        return redirect ('shoppingcart')
    productInfo = Product.objects.filter(productID=productID).select_related()
    if request.method == 'POST':
        #create a form instance and populate it with data from the request
        form = CartAddProductForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            
            for product in productInfo:
                if(request.POST.get('submit')=='addtocart'):
                    if request.session.has_key('customerEmail'):
                        quantity=cd['quantity']
                        price=product.productprice
                    else:
                        return redirect ('signin')
        if(coltype=='sympathy'):
            price=price
        cart_add(request,productID,price,quantity,cd['update'])
        return redirect ('cart_detail')
    else:
        form= CartAddProductForm()
    return render(request, 'productdetails.html', locals())

#view for detail template
def cart_detail(request):
    customerName=None
    customerEmail=None
    if request.session.has_key('customerName'):
        customerName=request.session.get('customerName')
    if request.session.has_key('customerEmail'):
        customerEmail=request.session.get('customerEmail')
    if request.session.has_key('coltype'):
        coltype=request.session.get('coltype')
    if ((request.POST.get('submit')=='Cart')):
        return redirect ('shoppingcart')
    cart = Cart(request)
    cart_product_form = CartAddProductForm()
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(initial={'quantity': item['quantity'],'update': True})
    return render(request, 'shoppingcart.html', {'cart': cart, 'cart_product_form':cart_product_form,'customerName':customerName,'customerEmail':customerEmail})

#add to cart through product template
def cart_add(request,productID, price,quantity, update):
    cart = Cart(request)
    product = get_object_or_404(Product, productID=productID)
    cart.add(product,price,quantity=quantity,update_quantity=update)

def cart_add_from_detail(request,productID,price):
    cart = Cart(request)
    product = get_object_or_404(Product, productID=productID)
    form = CartAddProductForm(request.POST)
    if request.session.has_key('coltype'):
        coltype=request.session.get('coltype')
    if(coltype=='sympathy'):
            price=price
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product,price,quantity=cd['quantity'],update_quantity=cd['update'])
    return redirect('cart_detail')

#view for removing item from cart
def cart_remove(request, productID):
    cart = Cart(request)
    product = get_object_or_404(Product, productID=productID)
    cart.remove(product)
    return redirect('cart_detail')

def order_create(request):
    cart = Cart(request)
    if request.session.has_key('customerName'):
        customerName=request.session.get('customerName')
    if request.session.has_key('customerEmail'):
        customerEmail=request.session.get('customerEmail')
    displayCartSummary=1
    countFlower=0
    error=None
    for item in cart:
            for product in Product.objects.filter(productID=item['product'].productID):
                if product.producttype=='Flower':
                    countFlower+=item['quantity']
    if request.method == 'POST':
        form=OrderCreateForm(request.POST)
        if countFlower>5:
            form = OrderCreateBouquetForm(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            if 78501<=int(cd['postalCode'])<=78599 and cd['deliverydate']>date.today():
                orderInfo=form.save(commit=False)
                orderInfo.email=customerEmail
                order = form.save()
                totalcost=0
                for item in cart:
                    OrderItem.objects.create(orderID=order,productID=item['product'],price=item['price'], quantity=item['quantity'])
                    totalcost=item['price']*item['quantity']+totalcost
             # clear the cart
                cart.clear()
            #send email to customer
                order_created(order.orderID,customerName,customerEmail,form['address'].value(),form['city'].value(),form['postalCode'].value(),totalcost)

            # set the order in the session
                request.session['order_id'] = order.orderID
            # redirect to the payment
                return redirect(reverse('payment:process'))
            #return render(request,'created.html',{'order': order,'bodyStyle':bodyStyle,'templateCSS':templateCSS,'displayCartSummary':displayCartSummary})
            elif int(cd['postalCode'])<78501 or int(cd['postalCode'])>78599:
                error='invalid postal code!'
            elif cd['deliverydate']<=date.today():
                error='invalid delivery date!'
    else:
        if countFlower>5:
            form = OrderCreateBouquetForm()
        else:
            form = OrderCreateForm()
    return render(request,  'create.html',{'cart': cart, 'form': form,'displayCartSummary':displayCartSummary,'customerName':customerName,'customerEmail':customerEmail,'error':error})
        
def order_created(orderID,customerName,customerEmail,mailaddress,city,zipcode,totalcost):
    #Task to send an e-mail notification when an order is successfully created.
    fromEmail=settings.EMAIL_HOST_USER
    subject = 'Order ID is  {}'.format(orderID)
    message = 'Dear {},\n\nYou have successfully placed an order. Your order id is {}. The total cost is ${}. The mailling address is {} {}, {}'.format(customerName,orderID,totalcost,mailaddress,city,zipcode,)
    mail_sent = send_mail(subject,message,fromEmail,[customerEmail])
    return mail_sent
