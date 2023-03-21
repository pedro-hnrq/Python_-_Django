from django import forms

class Cliente(forms.Form):
    nome = forms.CharField(max_length=20, required=False)
    idade = forms.IntegerField()
    data = forms.DateField()
    email = forms.EmailField()

    def __init__(self,  *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields['nome'].widget.attrs['class'] = 'form-control'
        self.fields['nome'].widget.attrs['placeholder'] = 'Digite seu nome...'

        self.fields['idade'].widget.attrs['class'] = 'form-control'
        self.fields['idade'].widget.attrs['placeholder'] = 'Digite sua idade...'

        self.fields['data'].widget.attrs['class'] = 'form-control'

        self.fields['email'].widget.attrs['class'] = 'form-control'

