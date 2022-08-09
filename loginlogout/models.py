from django.db import models


class User(models.Model):
    username = models.CharField(max_length=255, null=False)
    email = models.EmailField(max_length=255, null=False)
    password = models.CharField(max_length=50)
    ifLogged = models.BooleanField(default=False)
    token = models.CharField(max_length=500, null=True, default="")

    def __str__(self):
        return "{} -{}".format(self.username, self.email)



class UserData(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.FileField(blank=True, upload_to='farmer_data')
    language_code = models.CharField(max_length=50, blank=True, null=True)
