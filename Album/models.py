from django.db import models
from musician.models import Musician
# Create your models here.

ratings_choice={'1':'*',
        '2':'**',
        '3':'***',
        '4':'****',
        '5':'*****',
        }
class AlbumModle(models.Model):
    name = models.CharField(max_length=60)
    musician  = models.ForeignKey(Musician, on_delete=models.CASCADE)
    release_date = models.DateField()
    rating = models.CharField(max_length=1,choices=ratings_choice)

    def __str__(self):
        return self.name
    

# class MusicianAlbums(models.Model):
#     musician = models.ForeignKey(Musician, on_delete=models.CASCADE)
#     album = models.ForeignKey(AlbumModle, on_delete=models.CASCADE)

#     @property
#     def musician_name(self):
#         return f'{self.musician.First_name} {self.musician.Last_name}'

#     @property
#     def musician_email(self):
#         return self.musician.Email

#     @property
#     def album_rating(self):
#         return self.album.rating

#     @property
#     def instrument_type(self):
#         return self.musician.instrument

#     @property
#     def release_date(self):
#         return self.album.release_date

#     def __str__(self):
#         return f'{self.musician_name} - {self.album.name}'