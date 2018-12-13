from .models import Order
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.conf import settings
import weasyprint
from io import BytesIO
from django_rq import job


@job('default')
def order_created(order_id):
    """
    Task to send an e-mail notification when an order is successfully created.
    """
    order = Order.objects.get(id=order_id)
    # create invoice e-mail
    subject = 'My Shop - Invoice no. {}'.format(order.id)
    #message = 'Please, find attached the invoice for your recent purchase.'
    message = 'Дорогой(-гая) {},\n\nВы успешно оформили заказ. Номер Вашего заказа {}.'.format(order.first_name, order.id)
    email = EmailMessage(subject, message, 'admin@myshop.com', [order.email])
    # generate PDF
    html = render_to_string('orders/order/pdf.html', {'order': order})
    out = BytesIO()
    stylesheets=[weasyprint.CSS(settings.STATIC_ROOT + 'css/pdf.css')]
    weasyprint.HTML(string=html).write_pdf(out, stylesheets=stylesheets)
    # attach PDF file
    email.attach('order_{}.pdf'.format(order.id), out.getvalue(), 'application/pdf')
    # send e-mail
    email.send()

