from django.forms import ModelForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from . import models

class UserUpdateForm(ModelForm):
    class Meta:
        model = models.User
        fields = ('name',)

    """docstring for UserUpdateForm."""
    def __init__(self, *arg, **args):
        super().__init__(*arg, **args)
        self.helper = FormHelper()
        self.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Actualizar perfil'))
