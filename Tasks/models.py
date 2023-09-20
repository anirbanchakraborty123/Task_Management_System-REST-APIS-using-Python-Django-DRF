from django.db import models

# Create your models here.


class Task(models.Model):
    """
    This model is for creating new tasks and tracking the tasks progress.
    """
    title = models.CharField(max_length=255,blank=True,null=True)
    description = models.TextField(max_length=500,blank=True,null=True)
    status = models.CharField(choices=[("created","created"),("started","started"),("in_progress","in_progress"),("completed","completed")],default="created",max_length=20)  # You can use choices for predefined statuses
    due_date = models.DateField()
    
    def __str__(self) -> str:
        return self.title 
    class Meta:
        """ By default order the tasks by id """
        ordering = ['-id']
