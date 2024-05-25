from django import forms
from .models import Usuario
from .models import Solicitacao          

# Log in prefeitura

class RegistroForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['register_prefeitura', 'coluna_1234']
        widgets = {
            'coluna_1234': forms.PasswordInput(),
        }

# Formulário munícipe

class SolicitacaoForm(forms.ModelForm):
    mensagem = forms.CharField(widget=forms.Textarea(attrs={'maxlength': '50'}))

    class Meta:
        model = Solicitacao
        fields = ['nome', 'endereco', 'email', 'mensagem', 'imagem', 'tipo_solicitacao', 'prioridade']        