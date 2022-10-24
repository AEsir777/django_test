from django.core.exceptions import ValidationError
from django import forms
from .models import App2

class FileForm(forms.ModelForm):
    class Meta:
        model = App2
        fields = ('fileName', 'description')
        # constrol the front end
        widgets = {
            'fileName': forms.TextInput(attrs={'class': 'name'}), 
            'description': forms.Textarea(attrs={'class': 'des'})
        }
        labels = {
            'description': 'Enter the description'
        }

    # validation: cannot submit file with no Django in fileName
    def clean_fileName(self):
        name = self.cleaned_data['fileName']
        if 'Django' not in name:
            raise ValidationError('Only accept file name that contains Django')
        return name