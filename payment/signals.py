from django.conf import settings
from store.models import Order
from store.models import OrderItem
from paypal.standard.models import ST_PP_COMPLETED
from paypal.standard.ipn.signals import valid_ipn_received
from django.core.mail import send_mail
from django.shortcuts import render, get_object_or_404

def customer_payment_notification(sender, **kwargs):
    ipn_obj = sender
    if ipn_obj.payment_status == ST_PP_COMPLETED:
        # payment was successful
        order = get_object_or_404(Order, orderID=ipn_obj.invoice)
        orderItem=OrderItem.objects.filter(orderID=order.orderID).select_related()
        fromEmail=settings.EMAIL_HOST_USER
        subject = 'Order ID {} has been sucessfully processed'.format(order.orderID)
        totalcost=0
        for item in orderItem:
            totalcost=totalcost+item.get_cost()
        message = 'Dear customer,\n\nThe payment has been processed successfully. Your order id is {}. The total cost is ${}. The mailling address is {} {}, {} {}'.format(order.orderID,totalcost,order.address,order.city,order.state,order.postalCode)
        mail_sent = send_mail(subject,message,fromEmail,[order.email])
valid_ipn_received.connect(customer_payment_notification)

def payment_notification(sender, **kwargs):
    ipn_obj = sender
    if ipn_obj.payment_status == ST_PP_COMPLETED:
        # payment was successful
        order = get_object_or_404(Order, orderID=ipn_obj.invoice)

        # mark the order as paid
        order.paid = True
        order.save()

valid_ipn_received.connect(payment_notification)
