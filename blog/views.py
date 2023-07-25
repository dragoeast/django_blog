from django.shortcuts import render

posts = [
    {
        'author': 'Chris Markella',
        'title': 'Blog Post 1',
        'content': 'First Post Content',
        'date_posted': 'July 23, 2023',
    },
    {
        'author': 'Mark Markella',
        'title': 'Blog Post 2',
        'content': 'Second Post Content',
        'date_posted': 'July 24, 2023',
    },
    {
        'author': 'Krisztian Markella',
        'title': 'Blog Post 3',
        'content': 'Third Post Content',
        'date_posted': 'July 25, 2023',
    },
    
]

def home(request):
    context = {
        'posts': posts,
    }
    return render(request=request, template_name='blog/home.html', context=context)

def about(request):
    return render(request=request, template_name='blog/about.html')
