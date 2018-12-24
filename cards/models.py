from django.db import models
from django.utils.translation import ugettext_lazy as _


class Edition(models.Model):
    name = models.CharField(_('name'), max_length=30)
    empire_valid = models.DateField(_('empire valid'))
    release_date = models.DateField(_('release date'))
    image = models.URLField(_('image'))
    slug = models.SlugField(_('slug'))

    def __str__(self):
        return self.name

class Race(models.Model):
    name = models.CharField(_('name'), max_length=30)
    slug = models.SlugField(_('slug'))

    def __str__(self):
        return self.name

class Rarity(models.Model):
    name = models.CharField(_('name'), max_length=30)
    slug = models.SlugField(_('slug'))

    def __str__(self):
        return self.name

class Kind(models.Model):
    name = models.CharField(_('name'), max_length=30)
    slug = models.SlugField(_('slug'))

    def __str__(self):
        return self.name

class Keyword(models.Model):
    name = models.CharField(_('name'), max_length=30)
    slug = models.SlugField(_('slug'))
    definition = models.TextField(_('definition'))

    def __str__(self):
        return self.name

class Illustrator(models.Model):
    name = models.CharField(_('name'), max_length=30)
    slug = models.SlugField(_('slug'))

    def __str__(self):
        return self.name

class Card(models.Model):
    name = models.CharField(_('name'), max_length=120)
    ability = models.TextField(_('ability'))
    cost = models.IntegerField(_('cost'))
    damage = models.IntegerField(_('damage'))
    edid = models.IntegerField(_('edition id'))
    slug = models.SlugField(_('slug'))
    flavour = models.TextField(_('flavour'))
    ability = models.TextField(_('ability'))
    ability_html = models.TextField(_('ability html'))
    kind = models.ForeignKey(
        Kind, on_delete=models.PROTECT, related_name='cards'
    )
    rarity = models.ForeignKey(
        Rarity, on_delete=models.PROTECT, related_name='cards'
    )
    illustrator = models.ForeignKey(
        Illustrator, on_delete=models.PROTECT, related_name='cards'
    )
    edition = models.ForeignKey(
        Edition, on_delete=models.PROTECT, related_name='cards'
    )
    keywords = models.ManyToManyField(
        Keyword, related_name='cards'
    )

    def __str__(self):
        return self.name
