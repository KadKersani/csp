from django.db import models

# Create your models here.


# class Utilisateur(models.Model):
# 	id = models.AutoField(primary_key=True)
# 	nom = models.CharField(max_length=200, null=True)
# 	user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
# 	tel = models.CharField(max_length=200, null=True)
# 	email = models.CharField(max_length=200, null=True)
# 	date_created = models.DateTimeField(auto_now_add=True, null=True, verbose_name = 'Date de création')
# 	profile_img = models.ImageField(null = True, blank = True )
# 	etiquette = models.CharField(max_length=200, null=True, blank = True)

# 	def __str__(self):
# 		return self.nom


# class Projet(models.Model):
# 	id = models.AutoField(primary_key=True)
# 	utilisateur = models.ForeignKey(Utilisateur, null=True, on_delete= models.SET_NULL)
# 	date_created = models.DateTimeField(auto_now_add=True, null=True, verbose_name = 'Date de création')
# 	objectif = models.CharField(max_length=200, null=True, blank=True, verbose_name = 'Objectif')
# 	avancement = models.CharField(max_length=200, null=True, choices=STATUS, verbose_name = 'Avancement')
# 	typeLieu = models.CharField(max_length=200, null=True, choices=TYPELIEU)
# 	adresse = models.CharField(max_length=200, null=True, verbose_name = 'Adresse')
# 	description = models.CharField(max_length=200, null=True, blank=True, verbose_name = 'Description')
# 	def __str__(self):
# 		return str(self.id)



class City(models.Model):
  title = models.CharField(max_length=200)
  priority = models.IntegerField(default=-1, blank=True, null=True)
  visited = models.BooleanField(default=False, blank=True, null=True)
      
  def __str__(self):
    return self.title


