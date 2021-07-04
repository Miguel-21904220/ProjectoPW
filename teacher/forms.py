from django import forms
from django.forms import ModelForm
from .models import Formulario, Quiz, Comment
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class QuizForm(ModelForm):
    class Meta:
        model = Quiz
        fields = '__all__'
        # inserção de classes CSS para formatação de cada campo do formulário
        widgets = {
            'answer1': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Answer here.'}),
            'answer2': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Answer here.'}),
            'answer3': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Answer here.'}),
            'answer4': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Answer here.'}),
            'answer5': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Answer here.'}),
            'answer6': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Answer here.'}),
            'answer7': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Answer here.'}),
            'answer8': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Answer here.'}),
            'answer9': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Answer here.'}),
            'answer10': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Answer here.'}),
        }

        # texto a exibir junto à janela de inserção
        labels = {
            'answer1': 'What is CSS ?',
            'answer2': 'What is the origin of CSS ?',
            'answer3': 'What are CSS frameworks?',
            'answer4': 'What is HTML?',
            'answer5': 'Do all HTML tags come in a pair?',
            'answer6': 'How do you insert a copyright symbol on a browser page?',
            'answer7': 'What is Inline style?',
            'answer8': 'Who maintains the CSS specifications?',
            'answer9': 'Is there any way to keep list elements straight in an HTML file?',
            'answer10': 'Are <br> tags the only way to separate sections of text?',
        }

class FormularioForm(ModelForm):
    
    class Meta:
        model = Formulario
        fields = '__all__'
    # inserção de classes CSS para formatação de cada campo do formulário
        widgets = {
            'primeiroNome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'O seu primeiro nome'}),
            'ultimoNome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'O seu ultimo nome'}),
            'idade': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'O seu email'}),
            'commentario': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'A sua mensagem'}),
        }


    # texto a exibir junto à janela de inserção
        labels = {
            'primeiroNome': 'Primeiro Nome',
            'ultimoNome': 'Ultimo Nome',
            'idade': 'Idade',
            'email': 'Email',
            'commentario': 'Mensagem',
        }
               
class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'
        # inserção de classes CSS para formatação de cada campo do formulário
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}),
            'comment': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}),
        }

        # texto a exibir junto à janela de inserção
        labels = {
            'name': 'Whats your name?',
            'comment': 'Your comment.',
        }

class UserRegistraitonForm(UserCreationForm):
    first_name = forms.CharField(max_length=101)
    last_name = forms.CharField(max_length=101)
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
        
