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
    rate = 0
    comments = Comment.objects.filter(card=post).order_by("-date_posted")
    if request.method == "POST":
        govno = json.loads(request.body)
        rate = govno[0]
        content = govno[1]
        user_count = govno[2]
        comment = Comment.objects.create(card=post, author=user, caption=content, rate= rate)
        post.rate = (post.rate * user_count + rate)/(user_count + 1)
        post.save()
    context = {
        'title': 'Оставить отзыв',
        'comments': comments,
        'object': post,
        "rates": rate,
    }

    return render(request, 'rating_app/rating_app.html', context=context)