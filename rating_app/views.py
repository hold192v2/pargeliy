from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render

from map.models import Cardss
from .forms import CommentForm
from .models import Comment


def post_detailview(request, id, *args, **kwargs):
    user = request.user
    post = Cardss.objects.get(id=id)
    cf = CommentForm(data=request.POST or None)
    comments = Comment.objects.filter().order_by("-pk")
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