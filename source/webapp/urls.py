from django.urls import path
from webapp.views import hello, display_info

urlpatterns = [
    path('', hello),
    path('cat_stats/', display_info)
]