from django.db import models


class Element(models.TextChoices):
    PYRO = 'P', 'Pyro'
    HYDRO = 'H', 'Hydro'
    ELECTRO = 'E', 'Electro'
    GEO = 'G', 'Geo'
    CRYO = 'C', 'Cryo'
    DENDRO = 'D', 'Dendro'
    LUNAR = 'L', 'Lunar'
    STELLAR = 'S', 'Stellar'


class Gender(models.TextChoices):
    MALE = 'M', 'Male'
    FEMALE = 'F', 'Female'
    OTHER = 'O', 'Other'


class WeaponType(models.TextChoices):
    SWORD = 'SW', 'Sword'
    CLAYMORE = 'CL', 'Claymore'
    POLEARM = 'PL', 'Polearm'
    BOW = 'BW', 'Bow'
    CATALYST = 'CT', 'Catalyst'


class Region(models.TextChoices):
    MONDSTADT = 'MO', 'Mondstadt'
    LIYUE = 'LI', 'Liyue'
    INAZUMA = 'IN', 'Inazuma'
    SUMERU = 'SU', 'Sumeru'
    FONTAINE = 'FO', 'Fontaine'
    NATLAN = 'NA', 'Natlan'
    NOD_KRAI = 'NK', 'Nod Krai'
    SNEZHNAYA = 'SN', 'Snezhnaya'


class CharInfo(models.Model):

    name = models.CharField(max_length=100)

    element = models.CharField(
        max_length=1,
        choices=Element.choices
    )

    gender = models.CharField(
        max_length=1,
        choices=Gender.choices
    )

    weapon_type = models.CharField(
        max_length=2,
        choices=WeaponType.choices
    )

    region = models.CharField(
        max_length=2,
        choices=Region.choices
    )

    dob = models.DateField(
        blank=True,
        null=True
    )

    image = models.ImageField(
        upload_to='characters/'
    )

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = 'Character'
        verbose_name_plural = 'Characters'