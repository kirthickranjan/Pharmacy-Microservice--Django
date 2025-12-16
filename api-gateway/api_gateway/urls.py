from django.urls import path, re_path
from gateway import views

urlpatterns = [
    path('health', views.health),
    re_path(r'^api/auth/(?P<path>.*)$', 
            lambda request, path: views.proxy_request(request, 'auth', f'api/auth/{path}')),
    re_path(r'^api/prescriptions/?(?P<path>.*)$', 
            lambda request, path: views.proxy_request(request, 'prescription', f'api/v1/prescription/{path}')),
    re_path(r'^api/stocks/products/?(?P<path>.*)$', 
            lambda request, path: views.proxy_request(request, 'stock', f'api/v1/products/{path}')),
    re_path(r'^api/stocks/orders/?(?P<path>.*)$', 
            lambda request, path: views.proxy_request(request, 'stock', f'api/v1/orders/{path}')),
]