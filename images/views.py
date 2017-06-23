from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ImageCreateForm
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from .models import Image
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.contrib.auth.models import User
from action.utils import create_action
@login_required
def image_create(request):
    if request.method == 'POST':
        form = ImageCreateForm(data=request.POST,files=request.FILES)
        if form.is_valid():
            cd = form.cleaned_data
            new_item = form.save(commit=False)
            new_item.user = request.user
            new_item.save()
            create_action(request.user, 'uploaded an image', new_item)
            return HttpResponse('Image successfully added')
    else:
        form = ImageCreateForm(data=request.GET)
    return render(request,'images/image/create.html',{'section': 'images','form': form})

def image_detail(request, pk):
    image = get_object_or_404(Image, pk=pk)
    return render(request,'images/image/detail.html',{'section': 'images','image': image})

@login_required
@require_POST
def image_like(request):
    image_id = request.POST.get('id')
    action = request.POST.get('action')
    if image_id and action:
        try:
            image = Image.objects.get(id=image_id)
            if action == 'like':
                image.users_like.add(request.user)
                create_action(request.user, 'likes', image)
            else:
                image.users_like.remove(request.user)
            return JsonResponse({'status':'ok'})
        except:
            pass
    return JsonResponse({'status':'ko'})

@login_required
def image_list(request, pk):
    user = User.objects.get(id=pk) 
    images = Image.objects.filter(user = user)
    return render(request,'images/image/list.html',{'section': 'images', 'images': images})
