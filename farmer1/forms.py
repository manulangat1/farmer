from django import forms
from . models import Sell,Help
#create your form instances here.
class SellForm(forms.ModelForm):
    class Meta:
        model = Sell
        fields = ('text','name','slug','pic','price','available',)
class HelpForm(forms.ModelForm):
    class Meta:
        model = Help
        fields = ('text',)
