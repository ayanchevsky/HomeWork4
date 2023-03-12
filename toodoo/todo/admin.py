from django.contrib import admin
from django import forms
from .models import Todo


class TodoAdminForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = "__all__"

    def clean_completed(self):
        if self.cleaned_data["completed"] and self.cleaned_data['completed_date'] is None:
            raise forms.ValidationError("Отсутствует дата завершения задачи!")
        elif not self.cleaned_data["completed"] and self.cleaned_data['completed_date']:
            raise forms.ValidationError("У незавершенной задачи есть дата завершения!")
        return self.cleaned_data["completed"]


class TodoAdmin(admin.ModelAdmin):
    form = TodoAdminForm
    readonly_fields = ('created_date', )
    list_display = ['title', 'created_date', 'completed', 'completed_date', ]
    search_fields = ('title', )


# Register your models here.
admin.site.register(Todo, TodoAdmin)
