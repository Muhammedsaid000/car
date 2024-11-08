from django.urls import path
from .views import MarkViewSet, CarModelViewSet, CarViewSet

urlpatterns = [
    path('',CarViewSet.as_view({'get': 'list', 'post':'create'}), name='product_list'),
    path('<int:pk>/', CarViewSet.as_view({'get':'retrieve',
                                              'put':'update',
                                              'delete':'destroy'}), name='product_detail'),

    path('category/', CarViewSet.as_view({'get': 'list', 'post': 'create'}), name='category_list'),

    path('category/<int:pk>/', CarViewSet.as_view({'get': 'retrieve',
                                              'put': 'update',
                                              'delete': 'destroy'}), name='category_detail'),
]