from django import forms
from freedombooks_core.models import BookModel, TagsModel
from django.core.validators import MinLengthValidator
from django.core.exceptions import ValidationError

class AddPostBook(forms.ModelForm):
    #tag = forms.ModelChoiceField(queryset=TagsModel.objects.all(), empty_label='Tag not choiced', label='Tag')
    class Meta:
        model = BookModel
        fields = '__all__'

        widgets = {
            'title':forms.TextInput(attrs={'class':'form-input'}),
            'content':forms.Textarea(attrs={'cols':50, 'rows':5})
        }
        labels = {'slug':'URL'}
    def clean_data(self):
        title = self.cleaned_data['title']
        if len(title) > 128:
            raise ValidationError('Title is too long')
        else:
            return title
        
    def clean_data_text(self, id=None):
        if id is not None:
            text_hook = id
            return text_hook
        else:
            return


class UploadClassForm(forms.Form):
    file = forms.FileField(label='File')
