from django import forms
from .models import Bills
from orders.models import Orders
# from django_select2.forms import Select2MultipleWidget


class BillsForm(forms.ModelForm):

    class Meta:
        model = Bills
        fields = ('compName', 'createdBy', 'billAmount', 'billStatus')
        # widgets = {'orderId: OrderModelSelect2MultipleWidget'}

    # order = forms.ModelMultipleChoiceField(queryset=Orders.objects.all(), widget=Select2MultipleWidget)

