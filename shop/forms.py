from django import forms
from .models import Product, Order


class CheckoutForm(forms.ModelForm):

    class Meta:
        model = Order
        exclude = ['product']
        labels = {
            'customername': 'Name',
            'customeremail': 'Email',
            'customerphone': 'Phone Number',
            'customeraddress': 'Shipping Address',
            'customercity': 'Shipping City',
            'customerstate': 'Shipping State',
            'customerzip': 'Shipping Zip',
            'billingaddress': 'Billing Address',
            'billingcity': 'Billing City',
            'billingstate': 'Billing State',
            'billingzip': 'Billing Zip'
        }
