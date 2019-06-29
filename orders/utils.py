import random
import string
from orders.models import Order


def id_generator(size=6, chars=string.digits):
    the_id = "".join(random.choice(chars) for x in range(size))
    try:
        order = Order.objects.get(order_id=the_id)
        id_generator()
    except Order.DoesNotExist:
        return the_id
