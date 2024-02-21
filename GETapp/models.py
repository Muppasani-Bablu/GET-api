from django.db import models

# Create your models here.
class Model (models.Model):
    # id=models.AutoField(primary_key=True)
    # salary=models.BigIntegerField()
    
    student=models.CharField(max_length=150)
    sno=models.AutoField (primary_key=True)
    classroom=models.IntegerField()
    def __str__(self):
        return self.student
    class Meta:
        db_table="helo"
        managed=False