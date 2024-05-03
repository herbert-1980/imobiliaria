from django import forms
from .models import Cliente, Imovel, Registro

## Cadastra Cliente          
class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'
        
    def __init__(self, *args, **kwargs): # Adiciona 
        super().__init__(*args, **kwargs)  
        for field_name, field in self.fields.items():   
              field.widget.attrs['class'] = 'form-control'
              
class MultiploFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True

class MultiploFileField(forms.FileField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("widget", MultiploFileInput())
        super().__init__(*args, **kwargs)

    def clean(self, data, initial=None):
        single_file_clean = super().clean
        if isinstance(data, (list, tuple)):
            result = [single_file_clean(d, initial) for d in data]
        else:
            result = single_file_clean(data, initial)
        return result

## Cadastra um Imovel
class ImovelForm(forms.ModelForm):
    imovel = MultiploFileField()
    class Meta:
        model = Imovel
        fields = '__all__'
        exclude = ('alugado',)
        
    def __init__(self, *args, **kwargs): # Adiciona 
        super().__init__(*args, **kwargs)  
        for field_name, field in self.fields.items():   
            if field.widget.__class__ in [forms.CheckboxInput, forms.RadioSelect]:
                field.widget.attrs['class'] = 'form-check-input'
            else:
                field.widget.attrs['class'] = 'form-control'

## Registrar Locação do Imóvel
class RegistroLocacaoForm(forms.ModelForm):
    data_inicio = forms.DateTimeField(widget=forms.DateInput(format='%d-%m-%Y', attrs={'type': 'date'}))
    data_final = forms.DateTimeField(widget=forms.DateInput(format='%d-%m-%Y', attrs={'type': 'date'}))

    class Meta:
        model = Registro
        fields = '__all__'
        exclude = ('imovel', 'criacao',)
        
    def __init__(self, *args, **kwargs): # Adiciona 
        super().__init__(*args, **kwargs)  
        for field_name, field in self.fields.items():   
            field.widget.attrs['class'] = 'form-control'
