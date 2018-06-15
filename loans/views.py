from django.shortcuts import render
from django.views import View

from .forms import LoanRequestForm
from .models import LoanRequest


class LoanRequestView(View):
    form_tpl = 'loans/request_form.html'

    def get(self, request):
        return render(request, self.form_tpl, {'form': LoanRequestForm()})

    def post(self, request):
        form = LoanRequestForm(request.POST)

        if not form.is_valid():
            return render(request, self.form_tpl, {'form': LoanRequestForm()})

        loan_request = form.save()

        if form.is_approved():
            loan_request.approved = True
            loan_request.save()
            tpl = "loans/request_approved.html"
        else:
            tpl = "loans/request_disapproved.html"

        return render(request, tpl)


class LoanListView(View):
    def get(self, request):
        content = {'loans': LoanRequest.objects.order_by('-id')}
        return render(request, 'loans/list.html', content)


class LoadDetailView(View):
    def get(self, request):
        pass
