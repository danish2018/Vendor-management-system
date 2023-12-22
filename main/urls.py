from django.urls import path
from .views import *
urlpatterns = [
    path('vendors/', VendorView.as_view()),
    path('vendors/<int:vendor_id>/', VendorViewAPI.as_view()),
    path('purchase_orders/', PurchaseOrderView.as_view()),
    path('purchase_orders/<int:po_id>/', PurchaseOrderViewAPI.as_view()),
    path('vendors/<int:vendor_id>/performance/',VendorPerformanceView.as_view()),
    path('purchase_orders/<int:po_id>/acknowledge/',AcknowledgmentView.as_view())
    # path('login/',UserLoginView.as_view()),
    
]