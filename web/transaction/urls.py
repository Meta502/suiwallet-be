from transaction.views.inquiry import InquiryView
from django.urls import path

urlpatterns = [
    path("inquiry/", InquiryView.as_view(), name="inquire-transactions")
]
