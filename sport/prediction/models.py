from django.db import models
from sklearn.tree import DecisionTreeClassifier
import joblib

# Create your models here.
GENDER = (
    (0,'Female'),
    (1,'Male'),
)
class Data(models.Model):
    name = models.CharField(max_length=100,null=True)
    age = models.PositiveIntegerField(null=True)
    height = models.PositiveIntegerField(null=True)
    sex = models.IntegerField(choices=GENDER)
    prediction = models.CharField(max_length=100, blank=True)
    date = models.DateField(auto_now_add=True)
    
    
    def save(self,*args,**kwargs):
        ml_model = joblib.load('ml_model/ml_sport_model.joblib')
        self.prediction = ml_model.predict([[self.age,self.height,self.sex]])
        return super().save(*args,**kwargs)
    
    class Meta:
        ordering = ['-date']
        
    def __str__(self):
        return self.name