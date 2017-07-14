from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models import Post


def post_list(request):
	""" Shows all posts, and limits posts on 1 page."""
	post_list = Post.objects.all().order_by('-published_date')   # List of all posts, order by date
	paginator = Paginator(post_list, 4)
	page = request.GET.get('page')
	try:
		posts = paginator.page(page)
	except PageNotAnInteger:
		posts = paginator.page(1) # Calls page with index 1, if page not found calls except InvalidPage
	except EmptyPage:
		posts = paginator.page(paginator.num_pages) 		# Get number of all pages 
	vars = dict(posts=posts,)
	return render(request, 'blog/post_list.html', {'posts':posts})


def post_detail(request, pk):
	""" Shows single post. """
	post = get_object_or_404(Post, pk=pk)
	return render(request, 'blog/post_detail.html', {'post': post})
	


