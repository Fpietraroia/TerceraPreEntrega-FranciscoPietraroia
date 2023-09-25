
from django.urls import path
from AppPietra.views import *

urlpatterns = [
    path("", inicio, name="home"),
    path("your_u/", uform, name="user"),
    path("wishlist/", wform, name="compra"),
    path("delivery/", lform, name="delivery"),
    path("search/", busqueda, name="search"),
    path("results/", results, name="resultados")
    

]