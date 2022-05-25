from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
path("", views.index, name="ShopHome"),
path('about/', views.about,name="AboutUs"),
path("contact/", views.contact, name="ContactUs"),
path("search/", views.search, name="Search"),
path("tracker/", views.tracker, name="Tracker"),
path("products/<int:myid>", views.productview, name="View Product"),
path("checkout/", views.checkout, name="Check Out"),
path("handlerequest/", views.handlerequest, name="HandleRequest"),

]