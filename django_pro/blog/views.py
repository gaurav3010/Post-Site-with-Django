from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView

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

class PostDetailView(DetailView):
	model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
	model = Post
	fields = ['title', 'content']

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)
	
	
def about(request):
	return render(request, 'blog/about.html')
