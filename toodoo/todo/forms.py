from django.forms import ModelForm
from .models import Todo


class TodoForm(ModelForm):

    class Meta:
        model = Todo
        fields = ['title', 'description', ]

    # def clean_completed(self):
    #     data = self.cleaned_data['completed']
    #     print(data)
    #     return data
