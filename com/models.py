from django.db import models


class report(models.Model):
    rname = models.CharField(max_length=100)
    rnum = models.CharField(max_length=100)
    radd = models.CharField(max_length=200)

    vname = models.CharField(max_length=100)
    vnum = models.CharField(max_length=100)
    vadd = models.CharField(max_length=200)

    date = models.CharField(max_length=100)
    time = models.CharField(max_length=100)
    location = models.CharField(max_length=200)

    desc = models.CharField(max_length=200)

    def __str__(self):
        return self.rname + ' ' + self.rnum + ' ' + self.radd + ' ' + self.vname + ' ' + self.vnum + ' ' + self.vadd + ' ' + self.date + ' ' + self.time + ' ' + self.location + ' ' + self.desc
