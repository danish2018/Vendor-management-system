from .models import PurchaseOrder,HistoricalPerformance,Vendor
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
import datetime



@receiver(post_save,sender=PurchaseOrder)
def evaluation(sender, instance,created,**kwargs):

    if instance.status == "completed":
        if not instance.delivered_on_time and str(instance.delivery_date)[:11]  >= str(datetime.datetime.now())[:11]:
            instance.delivered_on_time = True
            instance.save()
        
        po_queryset = PurchaseOrder.objects.filter(vendor = instance.vendor)
        sum_delivery_po = 0
        sum_quality_po= 0
        sum_response_po= 0
        sum_fulfilled_po= 0
        total_completed_POs = 0
        total_POs= len(po_queryset)
        for i in po_queryset:
            if i.delivered_on_time : 
                sum_delivery_po +=1 
            if i.status == "completed":
                sum_quality_po += i.quality_rating
                if i.acknowledgment_date:
                    duration = i.acknowledgment_date - i.issue_date
                    sum_response_po += divmod(duration.total_seconds(), 3600)[0]
                sum_fulfilled_po +=1
                total_completed_POs +=1
        
        on_time_delivery_rate = sum_delivery_po / total_completed_POs
        quality_rating_avg = sum_quality_po / total_completed_POs
        average_response_time = sum_response_po / total_POs
        fulfillment_rate = sum_fulfilled_po /total_POs

        Vendor.objects.filter(id = instance.vendor.id).update(on_time_delivery_rate = on_time_delivery_rate,quality_rating_avg = quality_rating_avg,average_response_time = average_response_time,fulfillment_rate = fulfillment_rate)
        
        performance = HistoricalPerformance.objects.filter(vendor = instance.vendor)
        if performance:
            performance.update(date = datetime.datetime.now(tz=timezone.utc),on_time_delivery_rate = on_time_delivery_rate,quality_rating_avg = quality_rating_avg,average_response_time = average_response_time,fulfillment_rate = fulfillment_rate)
        else:
           HistoricalPerformance(vendor = instance.vendor,on_time_delivery_rate = on_time_delivery_rate,quality_rating_avg = quality_rating_avg,average_response_time = average_response_time,fulfillment_rate = fulfillment_rate).save()
         