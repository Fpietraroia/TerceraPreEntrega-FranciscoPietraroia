from django.shortcuts import render
from django.http import HttpResponse
from AppPietra.models import Buyer, Purchase, Location
from AppPietra.foms import UserForm , LocForm, WishForm
# Create your views here.

def inicio(request):

    return render(request, "AppPietra/inicio.html")

def buyer(request):

    return render(request, "AppPietra/buyer.html")

def compra(request):

    return render(request, "AppPietra/compra.html")

def envio(request):

    return render(request, "AppPietra/envio.html")

def uform(request):

    if request.method == "POST":

        formulario1 = UserForm(request.POST)

        if formulario1.is_valid():

            info = formulario1.cleaned_data

            user = Buyer(name=info["nombre"], sname=info["apellido"], mail=info["mail"])

            user.save()
            respuesta ="Usuario creado con exito!"
            return render(request, "AppPietra/inicio.html")
        
    else:

        formulario1 = UserForm()

    return render (request, "AppPietra/buyer.html",{"form_u":formulario1})

def lform(request):

    if request.method == "POST":

        formulario2 = LocForm(request.POST)

        if formulario2.is_valid():

            info = formulario2.cleaned_data

            direc = Location(country=info["localidad"], hood=info["calle"], num=info["altura"], d_date=info["fecha_envio"])

            direc.save()
            return render(request, "AppPietra/inicio.html")
        
    else:

        formulario2 = LocForm()

    return render (request, "AppPietra/envio.html",{"form_l":formulario2})

def wform(request):

    if request.method == "POST":

        formulario3= WishForm(request.POST)

        if formulario3.is_valid():

            info = formulario3.cleaned_data

            product = Purchase(obj=info["articulo"], color=info["color"])

            product.save()
            return render(request, "AppPietra/inicio.html")
        
    else:

        formulario3 = WishForm()

    return render (request, "AppPietra/compra.html",{"form_w":formulario3})

def busqueda(request):
    return render(request, "AppPietra/inicio.html")

def results(request):
    articulo = request.GET["articulo"]

    if articulo:
        color = Purchase.objects.filter(obj__icontains=articulo)
        if color:
            return render(request, "AppPietra/inicio.html", {"articulo": articulo, "color": color})
        else:
            respuesta = "No se encontraron resultados para el producto."
    else:
        respuesta = "No se proporcionó un término de búsqueda."

    return HttpResponse(respuesta)
