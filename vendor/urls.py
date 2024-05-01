from django.contrib import admin
from django.urls import path, include
from vendor import views

urlpatterns = [
    path('vendors/', views.VendorListCreateAPIView.as_view()),
    path('vendors/<int:pk>', views.VendorRetrieveUpdateDestroyAPIView.as_view()),
    path('purchase_orders/', views.PurchaseOrderListCreateAPIView.as_view()),
    path('purchase_orders/<slug:pk>', views.PurchaseOrderRetrieveUpdateDestroyAPIView.as_view()),
    path('vendors/<int:pk>/performance', views.PerformanceAPIview.as_view())
]
