from django import forms
from .models import Invoice


class InvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = ['name', 'invoice_number', 'phone_number', 'invoice_date',
                  'line_one', 'line_one_quantity', 'line_one_unit_price', 'line_one_total_price',
                  'line_two', 'line_two_quantity', 'line_two_unit_price', 'line_two_total_price',
                  'line_three', 'line_three_quantity', 'line_three_unit_price', 'line_three_total_price',
                  'line_four', 'line_four_quantity', 'line_four_unit_price', 'line_four_total_price',
                  'line_five', 'line_five_quantity', 'line_five_unit_price', 'line_five_total_price',
                  'line_six', 'line_six_quantity', 'line_six_unit_price', 'line_six_total_price',
                  'line_seven', 'line_seven_quantity', 'line_seven_unit_price', 'line_seven_total_price',
                  'line_eight', 'line_eight_quantity', 'line_eight_unit_price', 'line_eight_total_price',
                  'line_nine', 'line_nine_quantity', 'line_nine_unit_price', 'line_nine_total_price',
                  'line_ten', 'line_ten_quantity', 'line_ten_unit_price', 'line_ten_total_price',
                  'total', 'paid', 'invoice_type'
                  ]

    def clean_invoice_number(self):
        invoice_number = self.cleaned_data.get('invoice_number')
        if not invoice_number:
            raise forms.ValidationError('This field is required')
        if Invoice.objects.filter(invoice_number=invoice_number).exists():
            raise forms.ValidationError("email already exists in system. Please check the existing list.")
        return invoice_number

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if not name:
            raise forms.ValidationError('This field is required')
        return name

    def clean_line_one(self):
        line_one = self.cleaned_data.get('line_one')
        if not line_one:
            raise forms.ValidationError('This field is required')
        return line_one

    def clean_invoice_type(self):
        invoice_type = self.cleaned_data.get('invoice_type')
        if not invoice_type:
            raise forms.ValidationError('This field is required')
        return invoice_type

    # def clean_email(self):
    #     email = self.cleaned_data.get('email')
    #     email_match = MyObj.objects.filter(email=email).exclude(pk=self.instance.pk)
    #     if self.instance and self.instance.pk and not email_match:
    #         return email
    #     else:
    #         raise forms.ValidationError("email already exists in system. Please check the existing list.")


class InvoiceSearchForm(forms.ModelForm):
    generate_invoice = forms.BooleanField(required=False)

    class Meta:
        model = Invoice
        fields = ['invoice_number', 'name', 'invoice_date', 'generate_invoice']


class InvoiceUpdateForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = ['name', 'invoice_number', 'phone_number', 'invoice_date',
                  'line_one', 'line_one_quantity', 'line_one_unit_price', 'line_one_total_price',
                  'line_two', 'line_two_quantity', 'line_two_unit_price', 'line_two_total_price',
                  'line_three', 'line_three_quantity', 'line_three_unit_price', 'line_three_total_price',
                  'line_four', 'line_four_quantity', 'line_four_unit_price', 'line_four_total_price',
                  'line_five', 'line_five_quantity', 'line_five_unit_price', 'line_five_total_price',
                  'line_six', 'line_six_quantity', 'line_six_unit_price', 'line_six_total_price',
                  'line_seven', 'line_seven_quantity', 'line_seven_unit_price', 'line_seven_total_price',
                  'line_eight', 'line_eight_quantity', 'line_eight_unit_price', 'line_eight_total_price',
                  'line_nine', 'line_nine_quantity', 'line_nine_unit_price', 'line_nine_total_price',
                  'line_ten', 'line_ten_quantity', 'line_ten_unit_price', 'line_ten_total_price',
                  'total', 'paid', 'invoice_type'
                  ]
