# gallery/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Photo
from .forms import PhotoForms
from django.contrib import messages
from django.utils.translation import gettext as _
from django.core.paginator import Paginator


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


def list_post_view(request):
    query = request.GET.get('search', '')
    posts = Photo.objects.filter(title__icontains=query) if query else Photo.objects.all()

    paginator = Paginator(posts, 2)  #Ici Django divise les photos en plusieurs pages, chaque page contenant 3 posts

    page_number = request.GET.get('page')  #Récupération du numero de page à partir de la requete GET
    page_obj = paginator.get_page(page_number)  #OBTENTION DES POSTS de la page spécifique. C'est l'objet page_obj qui contient le attributs has_next, has_previous et paginator_range

    context = {
        'posts': page_obj,
        'query': query
    }
    return render(request, 'gallery/list_posts.html', context)


def edit_post_view(request, post_id):
    photo = get_object_or_404(Photo, id=post_id)
    form = PhotoForms(request.POST or None, request.FILES or None, instance=photo)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, "Modifications reussies!")
            return redirect('gallery:list_posts')
        else:
            messages.error(request, "Échec de la mise à jour. Veuillez vérifier les informations fournies.")

    context = {
        'form': form,
        'photo': photo,
    }
    return render(request, 'gallery/update_photo.html', context)


def delete_post_view(request, post_id):
    post = get_object_or_404(Photo, id=post_id)

    post.delete()
    messages.success(request, "post supprimé avec succès !")
    return redirect('gallery:list_posts')  #dans redirect, tu mets le name de la page qui est dans l'url
