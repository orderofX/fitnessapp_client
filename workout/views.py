from django.http import HttpResponse
from django.views import generic
from django.utils import timezone

from .models import Workout, Set, Rep

# def index(request):
#     return HttpResponse("Hello, world. You're at the workout index.")

class IndexView(generic.ListView):
    template_name = 'workout/index.html'
    context_object_name = 'workout_list'

    def get_queryset(self):
        """Return the last five posted workouts (not including those set to
        be published in the future). """
        return Workout.objects.order_by('-post_date')[:5]

class DetailView(generic.DetailView):
    template_name = 'workout/detail.html'
    context_object_name = 'workout'
    model = Set

    def get_queryset(self):
        """
        Return three reps which represents the set.
        """
        return Set.objects.all()

def health(request):
    return HttpResponse()