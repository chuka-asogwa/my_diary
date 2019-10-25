from django.db import models
from django.contrib.auth.models import User

class Topic(models.Model):
    """ Topic for a diary Entry. """
    title = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User,on_delete=models.CASCADE)
    
    
    def __str__(self):
        """ Return a string representation of model. """
        return self.title
    
    
class Entry(models.Model):
    """ Class for entry detail of a single topic """
    topic = models.ForeignKey(Topic,on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = 'entries'
        
        
    def __str__(self):
        """ Return a string representation of the model """
        if len(self.text) > 50:
            return f"{self.text[:50]}..."
        else:
            return f"{self.text}"
        
