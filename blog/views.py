from django.shortcuts import render, get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from hitcount.views import HitCountDetailView
from .models import Post, Category
from hitcount.models import HitCount
from hitcount.views import HitCountMixin
from django.core.paginator import Paginator
# Create your views here.
class PostListView(ListView):

    model = Post
    template_name = 'blog/blog.html'
    ordering = ['-created']
    
    paginate_by = 3

    def get_context_data(self, **kwargs):
        context = super(PostListView,self).get_context_data(**kwargs)
        context["categories"] = Category.objects.all() 
        return context
    

def category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    categories = Category.objects.all()
    category_list = category.get_posts.all()
    paginator = Paginator(category_list, 3) # Show 25 contacts per page

    page = request.GET.get('page')
    categori = paginator.get_page(page)

    return render(request, "blog/category.html", {'categori':categori, 'categories':categories})

class PostDetailView(DetailView):
    
    model = Post
    template_name = 'blog/post.html'

    def get_context_data(self, **kwargs):
        context = super(PostDetailView,self).get_context_data(**kwargs)
        post_sel = self.get_object()
        post_sel.views = post_sel.views + 1
        post_sel.save()
        context["categories"] = Category.objects.all() 
        context["visits"] = post_sel.views
        context["posts"]= Post.objects.all().order_by('-created')[:3]

        return context