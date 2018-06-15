from django.shortcuts import render, get_object_or_404, redirect
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


class LoanRequestListView(View):
    def get(self, request):
        content = {'loans': LoanRequest.objects.order_by('-id')}
        return render(request, 'loans/list.html', content)


class LoanRequestEditView(View):
    def get(self, request, loan_request_id):
        loan = get_object_or_404(LoanRequest, id=loan_request_id)
        form = LoanRequestForm(instance=loan)
        return render(request, 'loans/edit.html', dict(form=form))

    def post(self, request, loan_request_id):
        loan = get_object_or_404(LoanRequest, id=loan_request_id)
        form = LoanRequestForm(request.POST, instance=loan)

        if form.is_valid():
            form.save()
            return redirect('loan-request-list')

        return render(request, 'loans/edit.html', dict(form=form))


class LoadRequestDeleteView(View):
    def get(self, request, loan_request_id):
        loan = get_object_or_404(LoanRequest, id=loan_request_id)
        loan.delete()
        return redirect('loan-request-list')
