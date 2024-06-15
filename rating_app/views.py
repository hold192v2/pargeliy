from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

from map.models import Cardss
from .forms import CommentForm
from .models import Comment


def post_detailview(request, slug, *args, **kwargs):
    user = request.user
    post = Cardss.objects.get(slug=slug)
    cf = CommentForm(data=request.POST or None)
    val = request.POST.get('val')
    comments = Comment.objects.filter(card=post).order_by("-date_posted")
    if request.method == 'POST':
        el_id = request.POST.get('el_id')
        val = request.POST.get('val')
        post.rate = val
        post.save()
        if cf.is_valid():
            content = request.POST.get('content')
            rating = request.POST.get('rating')
            comment = Comment.objects.create( card= post, author=user, caption=content, rate= rating)
            comment.save()
            return redirect(post.get_absolute_url())
        else:
            cf = CommentForm()

    context = {
        'title': 'Оставить отзыв',
        'comments': comments,
        'object': post,
        'comment_form': cf,
        'rate' : val
    }
    return render(request, 'rating_app/rating_app.html', context=context)