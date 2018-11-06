from django.shortcuts import render,render_to_response
from blog.models import BlogsPost,Comment
from django.http import Http404
from blog.forms import CommentForm


# Create your views here.
def get_blogs(request):
    blog_list = BlogsPost.objects.all().order_by('-created')
    return render_to_response('blog_list.html', {'blog_list':blog_list})


def get_details(request,blog_id):
    try:
        blog = BlogsPost.objects.get(id = blog_id)
    except blog.DoesNotExist:
        raise Http404
    if request.method == 'GET':
        form = CommentForm()
    else:
        form = CommentForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            cleaned_data['blog'] = blog
            Comment.objects.create(**cleaned_data)

    ctx = {
        'blog': blog,
        'comments': blog.comment_set.all().order_by('-created'),
        'form': form
    }
    return render(request,'blog_details.html',ctx)
