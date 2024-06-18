import json

from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

from map.models import Cardss
from .forms import CommentForm
from .models import Comment


def post_detailview(request, slug, *args, **kwargs):
    user = request.user
    post = Cardss.objects.get(slug=slug)
    cf = CommentForm(data=request.POST or None)
    comments = Comment.objects.filter(card=post).order_by("-date_posted")
    if cf.is_valid():
        content = request.POST.get('content')
        comment = Comment.objects.create(card=post, author=user, caption=content)
        # Дополнительная логика по обновлению данных, если необходимо
    context = {
        'title': 'Оставить отзыв',
        'comments': comments,
        'object': post,
        'comment_form': cf,
    }

    return render(request, 'rating_app/rating_app.html', context=context)