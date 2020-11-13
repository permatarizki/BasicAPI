from django.db import models

# Create your models here.

class Makanan(models.Model):
    nama_makanan = models.CharField(max_length=100)
    kategori_list = (
        ("Makanan Barat", "Makanan Barat"),
        ("Makanan Asia", "Makanan Asia"),
        ("Makanan Indonesia", "Makanan Indonesia"),
        ("Makanan Korea", "Makanan Korea"),
    )
    kategori = models.CharField(max_length=40, choices= kategori_list)
    gambar = models.ImageField()

    def __str__(self):
        return '{} | {}'.format(self.nama_makanan, self.kategori)

class Bahan(models.Model):
    makanan = models.ForeignKey(Makanan, on_delete=models.CASCADE)
    nama_bahan = models.CharField(max_length= 100)
    qty = models.IntegerField()
    satuan_list = (
        ("gr", "gr"),
        ("buah", "buah"),
        ("ml", "ml"),
    )
    satuan = models.CharField(max_length= 10, choices = satuan_list)

    def __str__(self):
        return '{} | {}'.format(self.nama_bahan, self.makanan)