from django.db import models


# Create your models here.


class GeneralModel(models.Model):
    name_surname = models.CharField(max_length=60, null=True, blank=True)
    profile_image = models.ImageField(upload_to='media/profile_photos', null=True, blank=True)
    location = models.CharField(max_length=80, null=True, blank=True)
    date_of_birth = models.DateField(auto_now=False, null=True, blank=True)
    mail = models.EmailField()
    phone_number = models.CharField(max_length=100)
    web_site = models.URLField(max_length=100, blank=True)
    position = models.CharField(max_length=100)
    description = models.TextField()
    comunity = models.FloatField(default=0.00, max_length=1.00)
    solving = models.FloatField(default=0.00, max_length=1.00)
    safety = models.FloatField(default=0.00, max_length=1.00)
    info = models.FloatField(default=0.00, max_length=1.00)
    file_cv = models.FileField()

    def __str__(self):
        return f'{self.name_surname}'


class SkillsModel(models.Model):
    skills_desc = models.TextField()
    experience = models.IntegerField()
    happy_client =models.IntegerField()
    follower_facebook = models.IntegerField()
    finished_project = models.IntegerField()

    def __str__(self):
        return f'Work experience {self.experience}'


class JobSkills(models.Model):
    skills_model = models.ForeignKey(SkillsModel,on_delete=models.CASCADE,null=True,blank=True)
    skills_name = models.CharField(max_length=120,null=True,blank=True)
    skills_interest = models.FloatField(default=0)
    js_interest = models.CharField(max_length=15)

    def __str__(self):
        return f'{self.skills_name}'


class ExperienceModel(models.Model):
    company_name = models.CharField(max_length=120)
    start_date = models.DateField(auto_now=False)
    end_date = models.DateField(default="Present")
    job_title = models.CharField(max_length=120)
    desrp = models.TextField()

    def __str__(self):
        return f'{self.company_name}'


class EducationModel(models.Model):
    edu_name = models.CharField(max_length=120)
    start_date = models.DateField(auto_now=False)
    end_date = models.DateField(default="Present")
    job_title = models.CharField(max_length=120)
    desrp = models.TextField()
    edu_logo = models.ImageField(upload_to='media/edo_logo', null=True,blank=True)

    def __str__(self):
        return f'{self.edu_name}'


class PortfolioModel(models.Model):
    project_name = models.CharField(max_length=120)
    project_image = models.ImageField(upload_to='media/project_images', null=True,blank=True)
    project_link = models.URLField()

    def __str__(self):
        return f'{self.project_name}'


class Test(models.Model):
    test = models.CharField(max_length=255)