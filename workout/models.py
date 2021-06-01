import datetime
from django.db import models

class Rep(models.Model):
    exercise_name = models.CharField(max_length=60)
    weight = models.PositiveIntegerField(default=5)

    def __str__(self):
        return f"{self.exercise_name} {self.weight}lb"

class Set(models.Model):
    reps = models.ManyToManyField(Rep, blank=True)

    def __str__(self):
        return f"Reps: {self.reps}"

class Workout(models.Model):
    post_date = models.DateTimeField('data posted')
    # 3 instance of rep group - one object
    # should this be one???
    set = models.ManyToManyField(Set, blank=True)

    def __str__(self):
        return f"{self.post_date}"
