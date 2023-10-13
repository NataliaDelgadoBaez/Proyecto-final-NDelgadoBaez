from django import forms
 
class Crearalbumform(forms.Form):
    album= forms.CharField()
    artista= forms.CharField()
    año = forms.IntegerField()
    precio = forms.IntegerField()
    
class Buscaralbumform(forms.Form):
    album= forms.CharField()
    artista= forms.CharField()
    
    
class Mostraralbumform(forms.Form):
    nombre= forms.CharField()
    artista= forms.CharField()
    
    
    

