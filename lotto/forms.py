from django import forms
from .models import GuessNumbers
# Django���� �����ϴ� ModelForm�� Ȱ���� form ����
class PostForm(forms.ModelForm):
 # Form�� ���� �޾Ƶ鿩���� �����Ͱ� ��õǾ� �ִ� ��Ÿ ������ (DB ���̺��� ����)
    class Meta:
        model = GuessNumbers
        fields = ('name', 'text',) # ����ڷκ��� form ���� �Է¹��� ������