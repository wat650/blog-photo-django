# gallery/views.py
from django.shortcuts import render
from .models import Photo
from .forms import PhotoForms
from django.contrib import messages
from django.utils.translation import gettext as _

def created_photo_view(request):
    form = PhotoForms()
    
    # Vérifie si la requête est un POST avant de valider le formulaire
    if request.method == 'POST':
        form = PhotoForms(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, _("Création réussie !"))
            form = PhotoForms()  # Réinitialise le formulaire après l’enregistrement
        else:
            messages.error(request, _("Échec de création"))

    context = {
        'form': form,
    }
    return render(request, 'gallery/created_photo.html', context=context)
