from django.urls import path
from .views import *

urlpatterns = [
    path('', ProductInStock.as_view(), name='product_in_stock_url'),
    path('product/<int:product_id>',
         ProductDetail.as_view(), name='product_detail_url'),
    path('discarded', ProductDiscarded.as_view(), name='product_discarded_url'),
    path('delivered', ProductdDelivered.as_view(), name='product_delivered_url')

]
