from django.db import models
instruments=(
    ('guitar', 'Guitar'),
    ('drum', 'Drum'),
    ('amplifier', 'Amplifier'),
)
class Musician(models.Model):
    First_name = models.CharField(max_length=100)
    Last_name = models.CharField(max_length=100)
    Email = models.EmailField()
    Phone_number = models.CharField(max_length=12)
    instrument = models.CharField(max_length=30,choices = instruments)

    def __str__(self):
        return f'{self.First_name} {self.Last_name}'
    










# class MusicianAlbums(models.Model):
#     album = models.ForeignKey(AlbumModle, on_delete=models.CASCADE)
    

#     @property
#     def musician_name(self):
#         return f'{self.AlbumModle.musician.First_name} {self.AlbumModle.musician.Last_name}'

#     @property
#     def musician_email(self):
#         return self.AlbumModle.musician.Email

#     @property
#     def album_rating(self):
#         return self.album.rating

#     @property
#     def instrument_type(self):
#         return self.AlbumModle.musician.instrument

#     @property
#     def release_date(self):
#         return self.album.release_date

#     def __str__(self):
#         return f'{self.musician_name} - {self.album.title}'