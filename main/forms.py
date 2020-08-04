from django.forms import ModelForm, CharField
from django.forms.widgets import TextInput
from froala_editor.widgets import FroalaEditor
from main.models import Category, Article


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
        widgets = {
            'color': TextInput(attrs={'type': 'color'}),
        }


class ArticleForm(ModelForm):
    content = CharField(widget=FroalaEditor)
    
    class Meta:
        model = Article
        fields = '__all__'
