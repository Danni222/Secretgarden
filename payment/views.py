from django.shortcuts import render
from decimal import Decimal
from django.conf import settings
from django.core.urlresolvers import reverse
from django.shortcuts import render, get_object_or_404
from paypal.standard.forms import PayPalPaymentsForm
from store.models import Order
from store.models import OrderItem
from django.views.decorators.csrf import csrf_exempt
from paypal.standard.models import ST_PP_COMPLETED
from paypal.standard.ipn.signals import valid_ipn_received
from django.core.mail import send_mail


def payment_process(request):
    order_id = request.session.get('order_id')
    order = get_object_or_404(Order, orderID=order_id)
    host = request.get_host()
    paypal_dict = { 'business': settings.PAYPAL_RECEIVER_EMAIL,
                    'amount': '%.2f' % order.get_total_cost().quantize(Decimal('.01')),
                    'item_name': 'Order {}'.format(order.orderID),
                    'invoice': str(order.orderID),
                    'currency_code': 'USD',
                    'notify_url': 'http://{}{}'.format(host,reverse('paypal-ipn')),
                    'return_url': 'http://{}{}'.format(host, reverse('payment:done')),
                    'cancel_return': 'http://{}{}'.format(host, reverse('payment:canceled')),
                    }
    form = PayPalPaymentsForm(initial=paypal_dict)
    return render(request,'process.html',{'order': order, 'form':form})


@csrf_exempt
def payment_done(request):
    displayCartSummary=1
    return render(request, 'done.html',locals())

@csrf_exempt
def payment_canceled(request):
    displayCartSummary=1
    return render(request, 'canceled.html',locals())


