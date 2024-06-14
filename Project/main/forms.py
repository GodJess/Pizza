from .models import Articles, Public, MainProduct
from django.forms import ModelForm, TextInput, Textarea
from django.conf import settings
    
class ArticlesForm(ModelForm):
    class Meta:
        model = MainProduct
        fields = ['image', 'name', 'price', 'description', 'category']
        
        widgets={
            "image": TextInput(attrs={
                "class": "form-input",
                "placeholder": "Введите URL изображения"
            }),
            "name": TextInput(attrs={
                "class": "form-input",
                "placeholder": "Введите наименование пиццы"
            }),
            "price": TextInput(attrs={
                "class": "form-input",
                "placeholder": "Введите цену за пиццу"
            }),
            "description": Textarea(attrs={
                  "class": "form-area",
                "placeholder": "Введите описание пиццы"
            }),
            "category": TextInput(attrs={
                 "class": "form-input",
                "placeholder": "Введите категорию товара"
            })
        }

class PublicForm(ModelForm):
    class Meta:
        model = Public
        fields = ['login', 'comment']
        
        
        widgets={
            "login": TextInput(attrs={
                "class": "input-text",
                "placeholder": "Введите логин",
                'value': '',
                'readonly': '',
            }),
            "comment": Textarea(attrs={
                "class": "textarea",
                "placeholder": "Введите комментарий"
            })
        }
