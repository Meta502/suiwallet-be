from transaction.views.inquiry import InquiryView
from django.urls import path

from transaction.views.top_up import TopUpView
from transaction.views.virtual_account import ListCreateVirtualAccountView, GetUpdateDeleteVirtualAccountView

urlpatterns = [
    path("inquiry/", InquiryView.as_view(), name="inquire-transactions"),
    path("top-up/", TopUpView.as_view(), name="top-up-transactions"),
    path("virtual-account/", ListCreateVirtualAccountView.as_view(), name="virtual-account-list-create"),
    path("virtual-account/<uuid:virtual_account_id>/", GetUpdateDeleteVirtualAccountView.as_view(), name="virtual-account-update-delete")
]
