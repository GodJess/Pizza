from django.contrib import admin
from .models import Articles, Public, Drink, Dessert, Combo, Role, MainProduct


admin.site.register(Articles)
admin.site.register(Drink)
admin.site.register(Dessert)
admin.site.register(Combo)
admin.site.register(Public)
admin.site.register(Role)
admin.site.register(MainProduct)
# Register your models here.
