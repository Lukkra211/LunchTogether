from django.db import models


# Create your models here.


class User(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)

    def right_user(self, username, password):
        if username == self.username and self.password == password:
            return True
        return False

    def get_id(self):
        return self.id

    def is_registred(self, username):
        if username == self.username:
            return True
        return False