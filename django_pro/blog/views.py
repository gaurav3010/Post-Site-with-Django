from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User

# posts = [
# 	{
# 		'author':'Gaurav',
# 		'title':'First',
# 		'date_posted':'30th october',
# 		'content':'This is first post'
# 	},
# 	{
# 		'author':'Doli',
# 		'title':'Second',
# 		'date_posted':'31th october',
# 		'content':'This is second post'
# 	}
# ]

def home(request):
	context = {
		'posts':Post.objects.all(),
	}
	return render(request, 'blog/home.html', context)

class PostListView(ListView):
	model = Post
	template_name = 'blog/home.html'
	context_object_name = 'posts' 
	ordering = ['-date_posted']
	paginate_by = 5

class UserPostListView(ListView):
	model = User
	template_name = 'blog/user_posts.html'
	context_object_name = 'posts' 
	ordering = ['-date_posted']
	paginate_by = 5
	ordering = ['-date_posted']

	def get_queryset(self):
		user = get_object_or_404(User, username=self.kwargs.get('username'))
		return Post.objects.filter(author=user)

class PostDetailView(DetailView):
	model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
	model = Post
	fields = ['title', 'content']

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Post
	fields = ['title', 'content']

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		return False
	
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Post
	success_url = '/'

	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		return False

def about(request):
	return render(request, 'blog/about.html')
