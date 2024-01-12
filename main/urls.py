from django.urls import path
from .views import *


urlpatterns = [
    path('get_banner/', get_banner),
    path('get_about/', get_about),
    path('get_mini_about/', get_mini_about),
    path('get_products_for_main/', get_products_for_main),
    path('get_service/', get_service),
    path('get_category_for_main/', get_category_for_main),
    path('get_feedback/', get_feedback),
    path('get_about_us_number/', get_about_us_number),
    path('get_blog/', get_blog),
    path('get_faq/', get_faq),
    path('get_category/', get_category),
    path('get_description/', get_description),
    path('get_product_detail/', get_product_detail),
    path('get_product_detail/', get_product_detail),
    path('get_portfolio/', get_portfolio),
    path('get_service/', get_service),
    path('get_service_extra/', get_service_extra),
    path('get_partner/', get_partner),
    path('get_production/', get_production),
    path('get_jobs/', get_jobs),
    path('get_history/', get_history),
    path('get_blog/', get_blog),
    path('get_contact/', get_contact),
    path('get_faq/', get_faq),
    path('add_cart/', add_cart),
    path('get_cart/', get_cart),
    path('remove_cart/', remove_cart),
    path('create_order/', create_order),
    path('login_view/', login_view),
]

