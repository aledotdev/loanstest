import mock
from django.test import TestCase
from loans.forms import LoanRequestForm
# from loans.models import LoanRequest


class LoanRequestTestCase(TestCase):

    def _get_valid_form(self):
        return LoanRequestForm(dict(
            name='Alejandro',
            last_name='Devalis',
            dni="31302928",
            email='aledev@gmail.com',
            amount='200',
            gender='M',
        ))

    def test_loan_request_form(self):
        loan_form = self._get_valid_form()
        loan_form.is_valid()
        self.assertTrue(loan_form.is_valid())

        loan = loan_form.save()

        self.assertEqual(loan.name, 'Alejandro')
        self.assertEqual(loan.last_name, 'Devalis')
        self.assertEqual(loan.dni, 31302928)
        self.assertEqual(loan.email, 'aledev@gmail.com')
        self.assertEqual(loan.amount, 200)
        self.assertEqual(loan.gender, 'M')

    def test_loan_request_form_errors(self):
        loan_form = LoanRequestForm()
        self.assertFalse(loan_form.is_valid())

        loan_form = LoanRequestForm(dict(
            name='Alejandro',
            last_name='Devalis',
            dni="abc",
            email='aledev',
            amount='hola lala',
            gender='X',
        ))
        errors_list = sorted(loan_form.errors.keys())
        self.assertListEqual(errors_list, ['amount', 'dni', 'email', 'gender'])

    @mock.patch('requests.get')
    def test_loan_request_form_is_approved(self, mock_get):
        loan = self._get_valid_form()
        loan.is_valid()

        mock_resp = mock.Mock()
        mock_resp.json = mock.Mock(return_value={'approved': True, 'error': False})
        mock_get.return_value = mock_resp
        self.assertTrue(loan.is_approved())

        mock_resp.json = mock.Mock(return_value={'approved': True, 'error': True})
        mock_get.return_value = mock_resp
        self.assertFalse(loan.is_approved())
