from django.db import models

CATEGORY = (
    ("dokument", "Dokument"), ("länk", "Länk")
)
class Document(models.Model):
    """
    Model to upload document links to document page
    """
    category = models.TextField(choices=CATEGORY, default="none",
        help_text="Välj om du vill lägga upp ett dokument eller en länk.")
    name = models.CharField(max_length=200, blank=False, 
        help_text="Skriv vad det är för dokumentet eller länk.")
    url = models.TextField(max_length=1000, blank=False,
        help_text="Klistra in URL/länken till dokumentet eller önskad länk.")
    

    def __str__(self):
        return self.name