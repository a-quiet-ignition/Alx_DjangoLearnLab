from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView, ListView, DetailView, UpdateView, DeleteView
from .models import Post, Comment, Profile, Tag
from .forms import UserUpdateForm, ProfileUpdateForm, PostForm, CommentForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Q

# Create your views here.
class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = 'blog/register.html'
    success_url = reverse_lazy('login')
    
    
class ProfileView(TemplateView):
    template_name = 'blog/profile.html'
    

# Profile Management View
@login_required
def update_profile(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('profile')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)
    
    context = {
        'user_form': user_form,
        'profile_form': profile_form
    }
    
    return render(request, 'blog/update_profile.html', context)


# Post Model Views
class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    ordering = ['published_date']
    
class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = Comment.objects.filter(post=self.object)
        return context
    
class PostCreateView(CreateView):
    model = Post
    template_name = 'blog/post_form.html'
    fields = ['author', 'title', 'content', 'tags']
    success_url = reverse_lazy('post_list')
    
class PostUpdateView(UpdateView, UserPassesTestMixin, LoginRequiredMixin):
    model = Post
    template_name = 'blog/post_form.html'
    fields = ['title', 'content', 'tags']
    success_url = reverse_lazy('post_list')
    
    # Permission check for update
    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author
    
class PostDeleteView(DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy('post_list')
    
    # Permission check for deletion
    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author
    
class PostSearchView(ListView):
    model = Post
    template_name = 'blog/search_results.html'
    context_object_name = 'posts'
    paginate_by = 10
    
    def get_queryset(self):
        query = self.request.GET.get('q', '')
        
        if query:
            # Search in title, content, and tags
            posts = Post.objects.filter(
                Q(title__icontains=query) |
                Q(content__icontains=query) |
                Q(tags__name__icontains=query)
            ).distinct()
        else:
            posts = Post.objects.none()
        
        return posts
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('q', '')
        return context

   
# Comment Model Views

class CommentCreateView(LoginRequiredMixin, CreateView): 
    model = Comment
    fields = ['content']
    template_name = 'blog/comment_form.html'
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.post_id = self.kwargs['pk']  
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('post_detail', kwargs={'pk': self.kwargs['pk']})  

class CommentUpdateView(UpdateView, UserPassesTestMixin, LoginRequiredMixin):
    model = Comment
    fields = ['content']
    template_name = 'blog/comment_form.html'
    
    
    def get_success_url(self):
        return reverse_lazy('post_detail', kwargs={'pk': self.object.post.pk})
    
    # Permission check for update
    def test_func(self):
        comment = self.get_object()
        return self.request.user == comment.author
    
    
class CommentDeleteView(DeleteView, UserPassesTestMixin, LoginRequiredMixin):
    model = Comment
    template_name = 'blog/comment_confirm_delete.html'
    
    def get_success_url(self):
        return reverse_lazy('post_detail', kwargs={'pk': self.object.post.pk})
    
    # Permission check for deletion
    def test_func(self):
        comment = self.get_object()
        return self.request.user == comment.author


# class CommentListView(ListView):
#     model = Comment
#     template_name = 'blog/post_detail.html'
#     context_object_name = 'comments'

# class CommentCreateView(CreateView): 
#     model = Comment
#     form_class = CommentForm
#     template_name = 'blog/comment_form.html'
    
#     def form_valid(self, form):
#         form.instance.author = self.request.user
#         form.instance.post_id = self.kwargs['post_id']
#         return super().form_valid(form)
    
#     def get_success_url(self):
#         return reverse_lazy('post_detail', kwargs={'pk': self.kwargs['post_id']})
    
# class CommentUpdateView(UpdateView, UserPassesTestMixin, LoginRequiredMixin):
#     model = Comment
#     form_class = CommentForm
#     template_name = 'blog/comment_form.html'
    
#     def get_success_url(self):
#         return reverse_lazy('post_detail', kwargs={'pk': self.object.post.pk})
    
#     # Permission check for update
#     def test_func(self):
#         comment = self.get_object()
#         return self.request.user == comment.author
    
# class CommentDeleteView(DeleteView, UserPassesTestMixin, LoginRequiredMixin):
#     model = Comment
#     template_name = 'blog/post_detail.html'
    
#     def get_success_url(self):
#         return reverse_lazy('post_detail', kwargs={'pk': self.object.post.pk})
    
#     # Permission check for deletion
#     def test_func(self):
#         comment = self.get_object()
#         return self.request.user == comment.author
    
    