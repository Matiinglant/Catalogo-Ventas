from django import forms

from .models import Producto


class Formulario_alta_producto(forms.ModelForm):
	

	class Meta:
		model = Producto
		fields = '__all__'

class EditPostForm(forms.ModelForm):
    class Meta:
        model = Producto

        fields = [
            'descripcion',
            'imagen',
			'precio',
			'stock',
        ]