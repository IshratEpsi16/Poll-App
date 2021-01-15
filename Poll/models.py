from django.db import models

# Create your models here.


class db(models.Model):
    poll_que = models.TextField()
    poll_option1 = models.CharField(max_length=30)
    poll_option2 = models.CharField(max_length=30)
    poll_option3 = models.CharField(max_length=30)
    poll_option4 = models.CharField(max_length=30)
    # here poll_option1_count default=0 because when we started the poll no one is voted
    poll_option1_count = models.IntegerField(default=0)
    poll_option2_count = models.IntegerField(default=0)
    poll_option3_count = models.IntegerField(default=0)
    poll_option4_count = models.IntegerField(default=0)

    def total(self):
        return self.poll_option1_count + self.poll_option2_count + self.poll_option3_count + self.poll_option4_count
