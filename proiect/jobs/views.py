from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
# Create your views here.
from django.urls import reverse
from django.views.generic import ListView, CreateView, UpdateView

from jobs.models import Jobs


class JobsView(LoginRequiredMixin, ListView):
    model = Jobs
    template_name = "jobs/jobs_index.html"
    paginate_by = 5


class CreateJobsView(LoginRequiredMixin, CreateView):
    model = Jobs
    fields = ['type', 'title', "url", "description", "how_to_apply"]
    template_name = 'jobs/jobs_form.html'

    def get_success_url(self):
        return reverse('jobs:lista_joburi')


class UpdateJobsView(LoginRequiredMixin, UpdateView):
    model = Jobs
    fields = ['type', 'title', "url", "description", "how_to_apply", "active"]
    template_name = 'jobs/jobs_form.html'

    def get_success_url(self):
        return reverse('jobs:lista_joburi')


@login_required
def delete_jobs(request, pk):
    Jobs.objects.filter(id=pk).update(active=0)
    return redirect("jobs:lista_joburi")


@login_required
def activate_jobs(request, pk):
    Jobs.objects.filter(id=pk).update(active=1)
    return redirect("jobs:lista_joburi")
