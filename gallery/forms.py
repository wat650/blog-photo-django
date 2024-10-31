# gallery/forms.py
from django import forms
from .models import Photo

class PhotoForms(forms.ModelForm):
    title = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',  # Classe Bootstrap pour les champs de texte
            'placeholder': 'Entrez le titre de la photo',
            # 'style': 'max-width: 500px;'
        })
    )
    description = forms.CharField(
        widget=forms.Textarea(attrs={
            "class": "form-control",  # Classe Bootstrap pour le champ de texte
            "rows": 5,
            "placeholder": "Description détaillée de la photo",
            # 'style': 'max-width: 500px;'
        })
    )
    image = forms.ImageField(
        widget=forms.ClearableFileInput(attrs={
            'class': 'form-control',  # Classe Bootstrap pour les fichiers
            'accept': 'image/*',
            # 'style': 'max-width: 500px;'
        })
    )

    class Meta:
        model = Photo
        fields = ['title', 'description', 'image']

    def clean_image(self):
        image = self.cleaned_data.get('image')
        if image and image.size > 500 * 1024: #500 ko
            raise forms.ValidationError("La taille de l'image est trop grande, réduisez-là.")
        return image
