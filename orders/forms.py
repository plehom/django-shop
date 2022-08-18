from django.forms import ModelForm
from .models import Order

class OrderForm(ModelForm):

    def __init__(self, *args, **kwargs):
       super(OrderForm, self).__init__(*args, **kwargs)
       self.fields['full_price'].widget.attrs['readonly'] = True
    class Meta:
        model = Order
        fields = ["name","surname","country","city","zipcode","address","full_price"]
        read_only = ("full_price")