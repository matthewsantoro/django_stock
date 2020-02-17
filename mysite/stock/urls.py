from django.urls import path
from .views import *

urlpatterns = [
    path('', ProductInStock.as_view(), name='product_in_stock_url'),
    path('modal_product_detail/<int:product_id>',
         ModalProductDetail.as_view(), name='modal_product_detail_url'),
    path('discarded', ProductDiscarded.as_view(), name='product_discarded_url'),
    path('delivered', ProductdDelivered.as_view(), name='product_delivered_url')

]
