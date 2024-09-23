from django import forms
from .models import CustomOrder

class CustomOrderForm(forms.ModelForm):

    class Meta:
        model = CustomOrder
        exclude = ['order_number', 'tax', 'order_total']
        fields = [
            'quantity',
            'stuff',
            'order_number',
            'first_name',
            'last_name',
            'phone',
            'email',
            'address_line_1',
            'address_line_2',
            'country',
            'state',
            'city',
            'order_note',
            'status',
            'ip',
            'is_ordered',
            'sizes_s',
            'sizes_m',
            'sizes_l',
            'sizes_xl',
            'sizes_xxl',
            'sizes_xxxl',
        ]
        widgets = {
            'order_number': forms.HiddenInput(),
            'status': forms.HiddenInput(),
            'ip': forms.HiddenInput(),
            'is_ordered': forms.HiddenInput(),
            'order_note': forms.Textarea(attrs={'rows': 4,'required':True, 'placeholder': 'Order Note', 'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(CustomOrderForm, self).__init__(*args, **kwargs)
        # No need to make 'tax' or 'order_total' read-only here
