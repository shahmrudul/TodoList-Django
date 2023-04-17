from django.shortcuts import render,redirect
from django.views.generic import CreateView,ListView,UpdateView,DeleteView
from django.urls import reverse_lazy
from .models import Todolist
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
# Create your views here.
def todolist(request):
   return render(request,'todo_list.html')
class TaskCreate(LoginRequiredMixin,CreateView):
    template_name='taskform.html'
    model=Todolist
    fields=['title','description','complete']
    success_url = reverse_lazy('todolist')
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

# class ShowTask(ListView,LoginRequiredMixin):
 
#  template_name='todo_list.html'
#  model=Todolist
#  context_object_name='todo_lists'
#  def get_queryset(self):
#     queryset = super().get_queryset()
#     print(queryset)
#     return queryset.filter(user=self.request.user)
@method_decorator(never_cache, name='get')
class ShowTask(LoginRequiredMixin,ListView):
    template_name='todo_list.html'
    model=Todolist
    context_object_name='todolists'
    def get_queryset(self):
        queryset = super().get_queryset()
        print(queryset)
        return queryset.filter(user=self.request.user)
    
class TaskUpdate(LoginRequiredMixin,UpdateView):
    template_name='taskform.html'
    model=Todolist
    fields=['title','description','complete']
    success_url=reverse_lazy('todo_list')
  
class TaskDelete(DeleteView):
    template_name='confirm_delete.html'
    model=Todolist
    fields='__all__'
    success_url=reverse_lazy('todo_list')
 