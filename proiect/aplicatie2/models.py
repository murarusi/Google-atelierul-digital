from django.db import models
company_type = (("SRL", "S.R.L"), ("SA", "S.A"))


class Companies(models.Model):
    name = models.CharField(max_length=100)
    website = models.CharField(max_length=50)
    company_type = models.CharField(max_length=10, choices=company_type)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name}-{self.website}-{self.company_type}"