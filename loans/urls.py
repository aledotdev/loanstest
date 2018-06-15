from django.urls import path
from .views import LoanRequestView, LoanRequestListView, LoanRequestEditView, LoadRequestDeleteView


urlpatterns = [
    path(r'/', LoanRequestView.as_view(), name='loan-request-form'),
    path(r'/list/', LoanRequestListView.as_view(), name='loan-request-list'),
    path(r'/edit/<int:loan_request_id>/', LoanRequestEditView.as_view(), name='loan-request-edit'),
    path(r'/delete/<int:loan_request_id>/', LoadRequestDeleteView.as_view(),
         name='loan-request-delete')
]
