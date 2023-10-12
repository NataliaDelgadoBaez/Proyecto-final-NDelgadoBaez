from django import forms
 
class Discoformulario(forms.Form):
    nombre= forms.CharField()
    autor= forms.CharField()
    año = forms.IntegerField()
    
class BuscaDiscoform(forms.Form):
    nombre= forms.CharField()
    
    

