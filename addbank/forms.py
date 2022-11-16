from django import forms
from .models import BankDetail


class BankDetail(forms.ModelForm):
    class Meta:
        model=BankDetail
        fields=['bank', 'accountno', 'accountname']


#class BankDetail(forms.Form):
 #   bank=forms.CharField()
  #  accountno=forms.IntegerField()
   # accountname=forms.CharField()

    