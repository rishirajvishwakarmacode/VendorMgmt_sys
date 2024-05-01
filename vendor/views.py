from rest_framework import generics, response
from .models import Vendor, Performance, PurchaseOrder
from .serializers import VendorSerializer, PerformanceSerializer, PurchaseOrderSerializer
from  django_filters.rest_framework import DjangoFilterBackend

class VendorListCreateAPIView(generics.ListCreateAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer

class VendorRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer

class PurchaseOrderListCreateAPIView(generics.ListCreateAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['vendor']

class PurchaseOrderRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer


class PerformanceAPIview(generics.RetrieveAPIView):
    queryset = Vendor.objects.all()
    serializer_class = PerformanceSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        performances = Performance.objects.filter(vendor = instance)
        serializer = self.get_serializer(performances, many=True)
        return response.Response(serializer.data)