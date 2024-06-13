from django.db import models


class User(models.Model):
    gender = models.CharField(max_length=30)
    role = models.CharField(max_length=30)
    salary = models.IntegerField(default=0)
    years_exp = models.IntegerField(default=0)
    company_size = models.IntegerField(default=0)
    industry = models.CharField(max_length=30)
    age = models.IntegerField(default=0)
    email = models.CharField(max_length=30)
    education_level = models.CharField(max_length=30, default="null")

    def __str__(self):
        return f"{self.gender} - {self.role} - {self.salary}"

    def get_user_info(self):
        return {
            "gender": self.gender,
            "role": self.role,
            "salary": self.salary,
            "years_exp": self.years_exp,
            "company_size": self.company_size,
            "industry": self.industry,
            "email": self.email,
            "education_level": self.education_level
        }