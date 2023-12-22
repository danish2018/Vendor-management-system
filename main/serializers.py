from rest_framework.serializers import ModelSerializer 
from .models import *

class VendorSerializer(ModelSerializer):
    class  Meta:
        model = Vendor
        fields = '__all__'

class PurchaseOrderSerializer(ModelSerializer):
    class  Meta:
        model = PurchaseOrder
        fields = '__all__'

class VendorPerformanceSerializer(ModelSerializer):
    class Meta:
        model =  HistoricalPerformance
        fields = '__all__'