from .models import Task
from django.forms import ModelForm, TextInput

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ["prod", "name", "price", "time"]
        widgets ={
            "prod": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название товара'
            }),
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Имя сотрудника'
            }),
            "price": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Цена'
            }),
            "time": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Время продажи'
            }),
        }