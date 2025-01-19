from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from .models import Post
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .forms import UserProfileForm, ProfileForm, SignUpForm
from .models import Profile
from django.contrib.auth import login

# Vista para listar los posts
class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'

# Vista para ver el detalle de un post
class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'

# Vista para crear un nuevo post
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'blog/post_form.html'
    fields = ['title', 'content', 'image']

# Vista para editar un post
class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    template_name = 'blog/post_form.html'
    fields = ['title', 'content', 'image']

    def get_queryset(self):
        # Filtrar posts por el usuario actual
        return Post.objects.filter(author=self.request.user)

# Vista para eliminar un post
class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy('post_list')

    def get_queryset(self):
        # Filtrar posts por el usuario actual
        return Post.objects.filter(author=self.request.user)

# Vista basada en clases para el perfil
class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'blog/profile.html'
    def get_context_data(self, **kwargs):
        # El contexto incluirá los datos del usuario logueado
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user  # Pasamos el usuario al template
        return context
    
@login_required
def profile_view(request):
    user = request.user
    profile = user.profile  # Obtiene el perfil relacionado al usuario
    return render(request, 'profile.html', {'user': user, 'profile': profile})

@login_required
def update_profile(request):
    profile = request.user.profile
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')  # Redirige al perfil actualizado
    else:
        form = ProfileForm(instance=profile)
    
    return render(request, 'update_profile.html', {'form': form})

@login_required
def edit_profile(request):
    user = request.user  # Obtener el usuario actual
    profile, created = Profile.objects.get_or_create(user=user)  # Obtener el perfil o crear uno nuevo
    
    if request.method == 'POST':
        user_form = UserProfileForm(request.POST, instance=user)  # Formulario para editar el usuario
        profile_form = ProfileForm(request.POST, request.FILES, instance=profile)  # Formulario para editar el perfil
        
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()  # Guardar los cambios del usuario
            profile_form.save()  # Guardar los cambios del perfil
            return redirect('profile')  # Redirigir a la página del perfil
    else:
        user_form = UserProfileForm(instance=user)  # Mostrar los datos actuales
        profile_form = ProfileForm(instance=profile)
    
    return render(request, 'edit_profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })

def home_view(request):
    return render(request, 'blog/home.html', {'mensaje': 'Bienvenido!'})

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Inicia sesión automáticamente después del registro
            return redirect('home')  # Cambia por la URL de inicio
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})

def about_us_view(request):
    return render(request, 'blog/about_us.html')

def temas_view(request):
    return render(request, 'blog/temas.html')