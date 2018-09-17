from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

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
	
def about(request):
	return render(request, 'blog/about.html')
