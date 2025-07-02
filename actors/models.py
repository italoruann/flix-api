from django.db import models

NATIONALITY_CHOICES = (
    ('AFG', 'Afghanistan'),
    ('DEU', 'Germany'),
    ('ARG', 'Argentina'),
    ('AUS', 'Australia'),
    ('AUT', 'Austria'),
    ('BEL', 'Belgium'),
    ('BOL', 'Bolivia'),
    ('BRA', 'Brazil'),
    ('CAN', 'Canada'),
    ('CHL', 'Chile'),
    ('CHN', 'China'),
    ('COL', 'Colombia'),
    ('KOR', 'South Korea'),
    ('CUB', 'Cuba'),
    ('DNK', 'Denmark'),
    ('EGY', 'Egypt'),
    ('ARE', 'United Arab Emirates'),
    ('ESP', 'Spain'),
    ('USA', 'United States'),
    ('PHL', 'Philippines'),
    ('FIN', 'Finland'),
    ('FRA', 'France'),
    ('GRC', 'Greece'),
    ('NLD', 'Netherlands'),
    ('HKG', 'Hong Kong'),
    ('HUN', 'Hungary'),
    ('IND', 'India'),
    ('IDN', 'Indonesia'),
    ('IRN', 'Iran'),
    ('IRQ', 'Iraq'),
    ('IRL', 'Ireland'),
    ('ISL', 'Iceland'),
    ('ISR', 'Israel'),
    ('ITA', 'Italy'),
    ('JPN', 'Japan'),
    ('LBN', 'Lebanon'),
    ('MEX', 'Mexico'),
    ('MAR', 'Morocco'),
    ('NGA', 'Nigeria'),
    ('NOR', 'Norway'),
    ('NZL', 'New Zealand'),
    ('PAK', 'Pakistan'),
    ('PER', 'Peru'),
    ('POL', 'Poland'),
    ('PRT', 'Portugal'),
    ('GBR', 'United Kingdom'),
    ('CZE', 'Czech Republic'),
    ('RUS', 'Russia'),
    ('SWE', 'Sweden'),
    ('THA', 'Thailand'),
    ('TUR', 'Turkey'),
)


class Actor(models.Model):
    name = models.CharField(max_length=200)
    birthday = models.DateField(null=True, blank=True)
    nationatily = models.CharField(
        max_length=3, 
        choices=NATIONALITY_CHOICES, 
        default='ESTADOS UNIDOS', 
        blank=True,
        null=True
    )
    
    def __str__(self):
        return self.name