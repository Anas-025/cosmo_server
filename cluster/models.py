from django.db import models


class User(models.Model):
    username = models.CharField(max_length=200)
    ip = models.CharField(max_length=200)

class Cluster(models.Model):
    name = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='clusters', null=True)

class Data(models.Model):
    value = models.CharField(max_length=200)

    def __str__(self):
        return self.value

class Comet(models.Model):
    type_of_comet = models.CharField(max_length=200, default="line")
    cluster = models.ForeignKey(Cluster, on_delete=models.CASCADE, related_name='comets', null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comets', null=True)
    x = models.IntegerField(default=0)
    y = models.IntegerField(default=0)
    w = models.IntegerField(default=1)
    h = models.IntegerField(default=1)
    data = models.ManyToManyField(Data)
    label = models.CharField(max_length=200, null=True)
