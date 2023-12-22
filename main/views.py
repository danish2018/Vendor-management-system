from .serializers import VendorSerializer,PurchaseOrderSerializer,VendorPerformanceSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Vendor,PurchaseOrder,HistoricalPerformance
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from django.utils import timezone
from rest_framework import status
from django.http import Http404
import datetime

# Create your views here.

class VendorView(APIView):
    
    def get(self,request):
        authentication_classes = [JWTAuthentication]
        permission_classes = [IsAuthenticated]
        vendor_obj = Vendor.objects.all()
        serializer = VendorSerializer(vendor_obj, many = True)
        return Response({'status':200 , 'payload':serializer.data})

    def post(self,request):
        serializer = VendorSerializer(data = request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response({'status':200, 'payload':serializer.data , 'message':'Vendor Added Successfully '})
        return Response({'status':403,'message':serializer.errors})
        

class VendorViewAPI(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get_object(self, vendor_id):
        try:
            return Vendor.objects.get(id=vendor_id)
        except Vendor.DoesNotExist:
            raise Http404

    def get(self, request, vendor_id, format=None):
        vendor = self.get_object(vendor_id)
        serializer = VendorSerializer(vendor)
        return Response({'status':200 , 'payload':serializer.data})

    def put(self, request, vendor_id, format=None):
        vendor = self.get_object(vendor_id)
        serializer = VendorSerializer(vendor, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'status':200 , 'payload':serializer.data,'message':"Vendor's details updated Successfully"})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, vendor_id, format=None):
        authentication_classes = [JWTAuthentication]
        permission_classes = [IsAuthenticated]
        vendor = self.get_object(vendor_id)
        vendor.delete()
        return Response({'message':'Vendor deleted Successfully '})


class PurchaseOrderView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self,request):
        purchase_obj = PurchaseOrder.objects.all()
        serializer = PurchaseOrderSerializer(purchase_obj, many = True)
        return Response({'status':200 , 'payload':serializer.data})

    def post(self,request):
        serializer = PurchaseOrderSerializer(data = request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response({'status':200, 'payload':serializer.data , 'message':'Purchase Order Added Successfully '})
        return Response({'status':403,'message':serializer.errors})


class PurchaseOrderViewAPI(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get_object(self,po_id):
        try:
            return PurchaseOrder.objects.get(id=po_id)
        except Vendor.DoesNotExist:
            raise Http404

    def get(self, request, po_id, format=None):
        order = self.get_object(po_id)
        serializer = PurchaseOrderSerializer(order)
        return Response({'status':200 , 'payload':serializer.data})

    def put(self, request, po_id, format=None):
        order = self.get_object(po_id)
        serializer = PurchaseOrderSerializer(order, data=request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response({'status':200 , 'payload':serializer.data,'message':'Purchase Order Updated Successfully '})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, po_id,  format=None):
        order = self.get_object(po_id)
        order.delete()
        return Response({'message':'Purchase Order Deleted Successfully '})

class VendorPerformanceView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self,request,vendor_id):
        vendor_obj = HistoricalPerformance.objects.filter(vendor = vendor_id)
        serializer = VendorPerformanceSerializer(vendor_obj, many = True)
        return Response({'status':200 , 'payload':serializer.data})

class AcknowledgmentView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self,request,po_id):
        purchase_obj = PurchaseOrder.objects.get(id = po_id)
        purchase_obj.acknowledgment_date = datetime.datetime.now(tz=timezone.utc)
        purchase_obj.save()
        
        return Response({'status':200 , 'payload':'Acknowledged Succesfully'})


