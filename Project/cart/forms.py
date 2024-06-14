from .models import Orders
from django.forms import ModelForm, TextInput
from django.conf import settings

class OrderForm(ModelForm):
    
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super().__init__(*args, **kwargs)
        self.fields['login'].widget.attrs['readonly'] = True
        self.fields['login'].widget.attrs['value'] = self.getLogin()
        

    def getLogin(self):
        ak = self.request.session.get(settings.USER_SESSION_ID, {})
        login = ak.get('login')
        if login is not None:
            return login
        else:
            return ""
    
    class Meta:
        
        model = Orders
        fields = ['login', 'name', 'surname', 'adress','price']
        
        widgets={
            "login": TextInput(attrs={
                "class": "inputcart-login pass",
                "name": 'login',
                "readonly": "",
                'id':'login',
            }),
            "name": TextInput(attrs={
                'class': "inputcart",
                'name': 'name',
                'placeholder': "Введите имя заказчика"
            }),
             "surname": TextInput(attrs={
                'class': "inputcart",
                'name': 'surname',
                'placeholder': "Введите фамилию заказчика"
            }),
              "adress": TextInput(attrs={
                'class': "inputcart",
                'name': 'adress',
                'placeholder': "Введите адрес доставки"
            }),
               "price": TextInput(attrs={
                'class': "inputcart input-price",
                'name': 'price',
                "readonly": "",
            }),
        }
