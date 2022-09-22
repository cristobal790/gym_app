from django import forms
from .models import Machine


class BaseMachineForm(forms.ModelForm):
    class Meta:
        model = Machine
        fields = (
            'name',
            'type',
            'muscle',
            'brand',
        )

        widgets = {
            'name': forms.TextInput(
                attrs={
                    'id': 'id_name',
                    'class': 'form-control',
                }
            ),
            'type': forms.Select(
                attrs={
                    'id': 'id_type',
                    'class': 'form-control',
                }
            ),
            'muscle': forms.CheckboxSelectMultiple(
                attrs={
                    'id': 'id_muscle',
                    'class': 'form-control',
                }
            ),
            'brand': forms.Select(
                attrs={
                    'id': 'id_brand',
                    'class': 'form-control',
                }
            ),
        }


class AddMachineForm(BaseMachineForm):
    pass


class EditMachineForm(BaseMachineForm):
    pass
