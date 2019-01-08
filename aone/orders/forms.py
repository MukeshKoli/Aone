from django import forms
from .models import Orders
from products.models import Products


class OrderForm(forms.ModelForm):

    class Meta:
        model = Orders
        fields = ('compName', 'itemName', 'itemQuantity',)


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['itemName'].queryset = Products.objects.none()

        if 'compName' in self.data:
            try:
                compName_id = int(self.data.get('compName'))

                self.fields['itemName'].queryset = Products.objects.filter(compName_id=compName_id).order_by('compName')
            except(ValueError, TypeError):
                pass

        elif self.instance.pk:
            print(str(self.instance.pk)) # This is to check.
            self.fields['itemName'].queryset = self.instance.compName.prodName_set.order_by('compName')
