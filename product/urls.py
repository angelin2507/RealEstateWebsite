from django.urls import path
from . import views
from .views import AboutUsView, ContactUsView, TemplateView

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('<int:product_id>/', views.product_detail, name='product_detail'),
    path('about/', AboutUsView.as_view(), name='about'),
    path('contact/', ContactUsView.as_view(), name='contact'),
    path('contact/success/', TemplateView.as_view(template_name='contact_success.html'), name='contact_success'),
]
