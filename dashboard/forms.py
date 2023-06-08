from django import forms
from django.forms import ModelForm

from shop.models import Product, Category


class AddProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['category', 'image', 'title','description', 'price']
        labels = {
            'category': 'Elige una categoria o subcategoria:',
            'image': 'Imagen:',
            'title': 'Nombre producto:',
            'description': 'Descripcion del producto:',
            'price': 'Precio:'
        }

    def __init__(self, *args, **kwargs):
        super(AddProductForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'


class AddCategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ['title', 'sub_category', 'is_sub']
        labels = {
            'title': 'Nombre categoria',
            'sub_category': 'Subcategoría de...',
            'is_sub': '¿Es subcategoría?'
        }

    def __init__(self, *args, **kwargs):
        super(AddCategoryForm, self).__init__(*args, **kwargs)
        self.fields['is_sub'].widget.attrs['class'] = 'form-check-input'
        self.fields['sub_category'].widget.attrs['class'] = 'form-control'
        self.fields['title'].widget.attrs['class'] = 'form-control'


class EditProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['category', 'image', 'title','description', 'price']
        labels = {
            'category': 'Elige una categoria o subcategoria:',
            'image': 'Imagen:',
            'title': 'Nombre producto:',
            'description': 'Descripcion del producto:',
            'price': 'Precio:'
        }

    def __init__(self, *args, **kwargs):
        super(EditProductForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'