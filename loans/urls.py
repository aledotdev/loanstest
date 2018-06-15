from django.urls import path
from .views import LoanRequestView, LoanListView


urlpatterns = [
    path(r'/', LoanRequestView.as_view()),
    path(r'/list/', LoanListView.as_view())
]
