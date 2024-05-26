from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator

class News(models.Model):
    name=models.CharField(max_length=100,null=True,blank=True)
    email=models.EmailField(max_length=100,unique=True)
    rating=models.FloatField(validators=[MinValueValidator(0),MaxValueValidator(5)],default=0)
    image=models.ImageField(upload_to='images/',null=True,blank=True)
    date=models.DateTimeField(auto_now_add=True)
    
    # @classmethod
    # def binary_search(cls, target_value):
    #     # Retrieve all objects sorted by field_name
    #     queryset = cls.objects.order_by('field_name')
        
    #     low = 0
    #     high = queryset.count() - 1

    #     while low <= high:
    #         mid = (low + high) // 2
    #         mid_value = queryset[mid].field_name
    #         if mid_value == target_value:
    #             return queryset[mid]  # Found the record
    #         elif mid_value < target_value:
    #             low = mid + 1
    #         else:
    #             high = mid - 1

    #     return None
    
    def __str__(self):
        return str(self.name)
    

class Address(models.Model):
    news=models.ForeignKey(News,on_delete=models.CASCADE)
    title=models.CharField(max_length=100,null=True,blank=True)
    address=models.TextField(null=True,blank=True)
    date=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.title)
    
