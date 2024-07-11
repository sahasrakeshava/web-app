from django.urls import path

from order import views

urlpatterns = [
    path('checkout/', views.checkout), 
    path('orders/', views.Orderslist.as_view()),
]
