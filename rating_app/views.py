from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

from map.models import Cardss
from .forms import CommentForm
from .models import Comment

@login_required
def post_detailview(request, slug, *args, **kwargs):
    user = request.user
    post = Cardss.objects.get(slug=slug)
    cf = CommentForm(data=request.POST or None)
    comments = Comment.objects.filter(card=post).order_by("-slug")
    if request.method == 'POST':
        if cf.is_valid():
            content = request.POST.get('content')
            comment = Comment.objects.create( card= post, author=user, caption=content)
            comment.save()
            return redirect(post.get_absolute_url())
        else:
            cf = CommentForm()

    context = {
        'title': 'Оставить отзыв',
        'comments': comments,
        'object': post,
        'comment_form': cf
    }
    return render(request, 'rating_app/rating_app.html', context=context)