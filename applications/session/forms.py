from django import forms
from .models import Session, TimeSession


class BaseSessionForm(forms.ModelForm):
    class Meta:
        model = Session
        fields = (
            'machine',
        )

        widgets = {
            'machine': forms.Select(
                attrs={
                    'id': 'id_machine',
                    'class': 'form-control',
                }
            ),
        }


class AddSessionForm(BaseSessionForm):
    pass


class EditSessionForm(BaseSessionForm):
    pass


class AddTimeSessionForm(BaseSessionForm):
    class Meta(BaseSessionForm.Meta):
        model = TimeSession
        fields = BaseSessionForm.Meta.fields + (
            'time',
            'spending',
        )
        widgets = BaseSessionForm.Meta.widgets | {
            'time': forms.TimeInput(
                attrs={
                    'id': 'id_time',
                    'class': 'form-control',
                    'type': 'time',
                    'step': 1,
                    'max': '02:00:00',
                }
            ),
            'spending': forms.NumberInput(
                attrs={
                    'id': 'id_spending',
                    'class': 'form-control',
                }
            ),
        }


class EditTimeSessionForm(BaseSessionForm):
    pass
