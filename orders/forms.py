from django import forms
from .models import Order
#from localflavor.ua.forms import UAPostalCodeField


class OrderCreateForm(forms.ModelForm):
    #postal_code = UAPostalCodeField()
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'city', 'address', 'delivery', 'postal_code', 'text']
        labels = {
            'first_name': 'Имя (обязательно)',
            'last_name': 'Фамилия (обязательно)',
            'email': 'email (обязательно)',
            'phone_number': 'Телефон (обязательно), код оператора + номер телефона: "0671234567". От 10 до 15 цифр.',
            'address': 'адрес',
            'postal_code': 'почтвый индекс',
            'city': 'город (обязательно)',
            'delivery': 'Доставка',
        }
        widgets = {
            'text': forms.Textarea(attrs={'cols': 80, 'rows': 5}),
        }




"""
from django import forms
from .models import Order


class OrderCreateForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'address', 'postal_code', 'city']
        labels = {
            'first_name': 'Имя',
            'last_name': 'Фамилия',
            'address': 'адрес',
            'postal_code': 'почтвый индекс',
            'city': 'город',
        }

"""
