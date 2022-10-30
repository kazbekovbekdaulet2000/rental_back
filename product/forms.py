from django import forms
from product.models.product import Product
from product.models.category import Category
from django.db.models import Q


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = "__all__"

    def __init__(self, *args, **kwargs):
      super(ProductForm, self).__init__(*args, **kwargs)


class CategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = "__all__"

    def __init__(self, *args, **kwargs):
      super(CategoryForm, self).__init__(*args, **kwargs)
      self.fields['parent_category'].queryset = Category.objects.filter(~Q(id=self.instance.id))