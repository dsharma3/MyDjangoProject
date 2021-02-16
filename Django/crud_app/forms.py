from django import forms
from crud_app.models import EmployeeModel
GENDER = ['M','F']

class EmployeeForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(EmployeeForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
                    visible.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = EmployeeModel
        fields = "__all__"
 