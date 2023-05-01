from django.urls import path

from transaction.views.inquiry import ListInquiryView, GetInquiryView
from transaction.views.top_up import TopUpView
from transaction.views.transfer import TransferView
from transaction.views.virtual_account import ListCreateVirtualAccountView, GetUpdateDeleteVirtualAccountView

urlpatterns = [
    path("inquiry/", ListInquiryView.as_view(), name="inquire-transactions"),
    path("inquiry/<uuid:transaction_id>", GetInquiryView.as_view(), name="inquire-transaction"),
    path("top-up/", TopUpView.as_view(), name="top-up-transactions"),
    path("virtual-account/", ListCreateVirtualAccountView.as_view(), name="virtual-account-list-create"),
    path("virtual-account/<uuid:virtual_account_id>/", GetUpdateDeleteVirtualAccountView.as_view(), name="virtual-account-update-delete"),
    path("transfer/", TransferView.as_view(), name="transfer-create")
]
