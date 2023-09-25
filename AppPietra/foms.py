from django import forms


class UserForm (forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    mail = forms.EmailField()

class LocForm (forms.Form):
    localidad = forms.CharField()
    calle = forms.CharField()
    altura = forms.IntegerField()
    fecha_envio = forms.DateField()

class WishForm (forms.Form):
    articulo = forms.CharField()
    color = forms.CharField()
