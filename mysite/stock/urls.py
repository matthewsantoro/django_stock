from django.urls import path
from .views import *
urlpatterns = [
    path('', ProductInStock.as_view()  , name='index'),
    path('discarded', ProductDiscarded.as_view(), name='discarded'),
    path('delivered', ProductdDelivered.as_view(), name='delivered')

]