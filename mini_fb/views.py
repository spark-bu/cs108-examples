from django.shortcuts import render
from.models import Profile, StatusMessage
from django.views.generic import ListView, DetailView, UpdateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import redirect
from django.urls import reverse


from .forms import CreateProfileForm,UpdateProfileForm, CreateStatusMessageForm

# Create your views here.
class ShowAllProfilesView(ListView):
    model = Profile
    template_name = 'mini_fb/show_all_profiles.html'
    context_object_name = 'all_profile_list'

class ShowProfilePageView(DetailView):
    model = Profile
    template_name = 'mini_fb/show_profile_page.html'
    context_object_name ='profile'

    def get_context_data(self, **kwargs):

        '''Return the context data (a dictionary) to be used in the template.'''

        # obtain the default context data (a dictionary) from the superclass; 
        # this will include the Profile record for this page view
        context = super(ShowProfilePageView, self).get_context_data(**kwargs)
        # create a new CreateStatusMessageForm, and add it into the context dictionary
        form = CreateStatusMessageForm()
        context['create_status_form'] = form
        # return this context dictionary
        return context

class CreateProfileView(CreateView):
    '''A view to create a new quote and save it to the database.'''
    form_class = CreateProfileForm
    template_name = "mini_fb/create_profile_form.html"

class DeleteStatusMessageView(DeleteView):
    template_name = "mini_fb/delete_status_form.html"
    queryset = Profile.objects.all()
    def get_context_data(self, **kwargs):
        context = super(ShowProfilePageView, self).get_context_data(**kwargs)
        st_msg = StatusMessage.objects.get(pk=self.kwargs['status_pk'])
        # return this context dictionary
        return context
    def get_object(self):
        profile_pk = self.kwargs['profile_pk']
        status_pk = self.kwargs['status_pk']
        st_msg = StatusMessage.objects.get(pk=self.kwargs['status_pk'])
        return st_msg

class ShowNewsFeedView(DetailView):
    model = Profile
    template_name = 'mini_fb/show_news_feed.html'


class UpdateProfileView(UpdateView):
    '''A view to create a new quote and save it to the database.'''
    form_class = UpdateProfileForm
    template_name = "mini_fb/update_profile_form.html"
    queryset = Profile.objects.all()

def create_status_message(request, pk):
    '''
    Process a form submission to post a new status message.
    '''
    # find the profile that matches the `pk` in the URL
    profile = Profile.objects.get(pk=pk)

    # if and only if we are processing a POST request, try to read the data
    if request.method == 'POST':

        # read the data from this form submission
        message = request.POST['message']
        form = CreateStatusMessageForm(request.POST or None, request.FILES or None)
        
        # save the new status message object to the database
        if message:
            sm = StatusMessage()
            sm.profile = profile
            sm.message = message
            image = form.save(commit=False)
            image.profile = profile
            image.save()
    # redirect the user to the show_profile_page view
    return redirect(reverse('profile', kwargs={'pk': pk}))

