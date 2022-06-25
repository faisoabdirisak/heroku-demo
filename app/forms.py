
from django.forms import ModelForm
from .models import  Review
from django import forms


class ReviewForm(ModelForm):
    class Meta:
        model=Review
        fields =['review', 'rating']

        labels={
            'body':'add a comment with your vote'
        }    

    def __init__(self, *args, **kwargs):
        super(ReviewForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
                field.widget.attrs.update({'class':''})        
       