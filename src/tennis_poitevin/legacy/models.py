from django.db import models
from django.utils import timezone


class User(models.Model):
    email = models.EmailField(max_length=180, unique=True)
    roles = models.JSONField(default=list)
    password = models.CharField(max_length=255)
    is_verified = models.BooleanField(default=False)
    nom = models.CharField(max_length=255)
    prenom = models.CharField(max_length=255)

    class Meta:
        db_table = "user"
        ordering = ["nom", "prenom"]

    def __str__(self):
        return f"{self.prenom} {self.nom}".strip()


class Categorie(models.Model):
    nom = models.CharField(max_length=255)
    slug = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ["nom"]

    def __str__(self):
        return self.nom


class Tag(models.Model):
    nom = models.CharField(max_length=100, unique=True)
    slug = models.CharField(max_length=100)
    couleur = models.CharField(max_length=7, blank=True, null=True)

    class Meta:
        ordering = ["nom"]

    def __str__(self):
        return self.nom


class Page(models.Model):
    titre = models.CharField(max_length=255)
    slug = models.CharField(max_length=255)
    est_publie = models.BooleanField(default=False)
    date_modification = models.DateTimeField(default=timezone.now)
    contenu = models.TextField(blank=True, null=True)
    categorie = models.ForeignKey(Categorie, on_delete=models.SET_NULL, null=True, blank=True, related_name="pages")
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name="pages")
    is_draft = models.BooleanField(default=True)
    tags = models.ManyToManyField(Tag, related_name="pages", blank=True, db_table="page_tag")
    sur_accueil = models.BooleanField(default=False)

    class Meta:
        ordering = ["-date_modification"]
        indexes = [models.Index(fields=["is_draft", "est_publie"])]

    def __str__(self):
        return self.titre


class Competition(models.Model):
    TYPE_CHAMPIONNAT = "championnat"
    TYPE_TOURNOI = "tournoi"
    nom = models.CharField(max_length=255)
    type = models.CharField(max_length=50, default=TYPE_CHAMPIONNAT)
    categorie = models.CharField(max_length=100, blank=True, null=True)
    division = models.CharField(max_length=50, blank=True, null=True)
    poule = models.CharField(max_length=50, blank=True, null=True)
    annee = models.IntegerField(default=timezone.now().year)
    date_debut = models.DateField(blank=True, null=True)
    date_fin = models.DateField(blank=True, null=True)
    sexe = models.CharField(max_length=20, blank=True, null=True)
    est_actif = models.BooleanField(default=True, null=True)
    classement_final = models.CharField(max_length=50, blank=True, null=True)
    nb_equipes = models.IntegerField(default=0)
    sur_accueil = models.BooleanField(default=False)

    class Meta:
        ordering = ["-annee", "nom"]
        indexes = [models.Index(fields=["annee", "est_actif"])]

    def __str__(self):
        return f"{self.nom} {self.annee}"


class Equipe(models.Model):
    nom = models.CharField(max_length=255)
    ville = models.CharField(max_length=100, blank=True, null=True)
    est_club = models.BooleanField(default=False, null=True)
    competitions = models.ManyToManyField(Competition, related_name="equipes", blank=True)

    class Meta:
        ordering = ["nom"]

    def __str__(self):
        return self.nom


class MatchTennis(models.Model):
    RESULTAT_VICTOIRE = "V"
    RESULTAT_DEFAITE = "D"
    RESULTAT_NUL = "N"
    equipe_domicile = models.ForeignKey(Equipe, on_delete=models.SET_NULL, null=True, blank=True, related_name="matchs_domicile")
    equipe_exterieur = models.ForeignKey(Equipe, on_delete=models.SET_NULL, null=True, blank=True, related_name="matchs_exterieur")
    equipe_domicile_club_id = models.IntegerField(blank=True, null=True)
    equipe_exterieur_club_id = models.IntegerField(blank=True, null=True)
    date_match = models.DateField()
    score_domicile = models.CharField(max_length=50, blank=True, null=True)
    score_exterieur = models.CharField(max_length=50, blank=True, null=True)
    resultat = models.CharField(max_length=10, blank=True, null=True)
    est_domicile = models.BooleanField(default=True, null=True)
    lieu = models.CharField(max_length=255, blank=True, null=True)
    commentaire = models.TextField(blank=True, null=True)
    competition = models.ForeignKey(Competition, on_delete=models.CASCADE, null=True, blank=True, related_name="matchs")
    forfait = models.BooleanField(default=False, null=True)

    class Meta:
        ordering = ["date_match"]
        indexes = [models.Index(fields=["date_match"])]


class Joueur(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    classement = models.CharField(max_length=20, blank=True, null=True)
    categorie = models.CharField(max_length=20, blank=True, null=True)
    sexe = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        ordering = ["nom", "prenom"]

    def __str__(self):
        return f"{self.prenom} {self.nom}"


class Palmares(models.Model):
    TYPE_VAINQUEUR = "Vainqueur"
    TYPE_FINALISTE = "Finaliste"
    TYPE_DEMI_FINALISTE = "Demi-finaliste"
    TYPE_QUART_FINALISTE = "Quart de finaliste"
    NIVEAU_DEPARTEMENTAL = "Départemental"
    NIVEAU_REGIONAL = "Régional"
    NIVEAU_NATIONAL = "National"
    NIVEAU_INTERNATIONAL = "International"
    joueur = models.ForeignKey(Joueur, on_delete=models.CASCADE, related_name="palmares")
    annee = models.IntegerField()
    competition = models.CharField(max_length=255)
    resultat = models.CharField(max_length=100, default=TYPE_VAINQUEUR)
    categorie = models.CharField(max_length=100, blank=True, null=True)
    niveau = models.CharField(max_length=50, default=NIVEAU_DEPARTEMENTAL, blank=True, null=True)
    epreuve = models.CharField(max_length=50, blank=True, null=True)
    est_actif = models.BooleanField(default=True, null=True)

    class Meta:
        ordering = ["-annee", "competition"]


class CouleurSite(models.Model):
    nom = models.CharField(max_length=255)
    couleur_primaire = models.CharField(max_length=7)
    couleur_secondaire = models.CharField(max_length=7)
    couleur_action = models.CharField(max_length=7)
    couleur_texte = models.CharField(max_length=7, blank=True, null=True)
    couleur_texte_navbar = models.CharField(max_length=7, blank=True, null=True)
    couleur_texte_bouton = models.CharField(max_length=7, blank=True, null=True)
    couleur_hero = models.CharField(max_length=7, blank=True, null=True)
    couleur_texte_hero = models.CharField(max_length=7, blank=True, null=True)
    couleur_presentation = models.CharField(max_length=7, blank=True, null=True)
    couleur_texte_presentation = models.CharField(max_length=7, blank=True, null=True)
    couleur_slider = models.CharField(max_length=7, blank=True, null=True)
    couleur_texte_slider = models.CharField(max_length=7, blank=True, null=True)
    couleur_partenaire = models.CharField(max_length=7, blank=True, null=True)
    couleur_card = models.CharField(max_length=7, blank=True, null=True)
    couleur_texte_card = models.CharField(max_length=7, blank=True, null=True)
    image_par_defaut = models.CharField(max_length=512, blank=True, null=True)


class CoursFormation(models.Model):
    nom = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    position = models.IntegerField(default=0)
    est_actif = models.BooleanField(default=True, null=True)

    class Meta:
        ordering = ["position"]


class TarifFormation(models.Model):
    intitule = models.CharField(max_length=255)
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    unite = models.CharField(max_length=50, default="an", blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    position = models.IntegerField(default=0)
    cours_formation = models.ForeignKey(CoursFormation, on_delete=models.CASCADE, related_name="tarifs")

    class Meta:
        ordering = ["position"]


class Domaine(models.Model):
    nom = models.CharField(max_length=255)
    ordre = models.IntegerField(blank=True, null=True)

    class Meta:
        ordering = ["ordre", "nom"]


class Partenaire(models.Model):
    nom = models.CharField(max_length=255, unique=True)
    logo = models.CharField(max_length=255, blank=True, null=True)
    domaine = models.ForeignKey(Domaine, on_delete=models.SET_NULL, null=True, blank=True, related_name="partenaires")
    lien = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        ordering = ["nom"]


class Enseignant(models.Model):
    nom = models.CharField(max_length=255)
    prenom = models.CharField(max_length=255)
    diplome = models.CharField(max_length=255)
    fonction = models.CharField(max_length=255, blank=True, null=True)
    photo = models.CharField(max_length=255, blank=True, null=True)
    biographie = models.TextField(blank=True, null=True)
    est_actif = models.BooleanField(default=True, null=True)
    cours_particuliers = models.BooleanField(default=False, null=True)

    class Meta:
        ordering = ["nom", "prenom"]


class MembreManagement(models.Model):
    nom = models.CharField(max_length=255)
    prenom = models.CharField(max_length=255)
    fonction = models.CharField(max_length=255)
    photo = models.CharField(max_length=255, blank=True, null=True)
    biographie = models.TextField(blank=True, null=True)
    email = models.EmailField(max_length=255, blank=True, null=True)
    telephone = models.CharField(max_length=50, blank=True, null=True)
    est_actif = models.BooleanField(default=True, null=True)

    class Meta:
        ordering = ["nom", "prenom"]


class DocumentAdministratif(models.Model):
    titre = models.CharField(max_length=255)
    fichier = models.CharField(max_length=255)
    categorie = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    date_ajout = models.DateTimeField(default=timezone.now)
    est_actif = models.BooleanField(default=True, null=True)


class HistoireClub(models.Model):
    annee = models.IntegerField()
    titre = models.CharField(max_length=255)
    description = models.TextField()
    image = models.CharField(max_length=255, blank=True, null=True)
    est_actif = models.BooleanField(default=True, null=True)
    page = models.ForeignKey(Page, on_delete=models.SET_NULL, null=True, blank=True, related_name="histoires")

    class Meta:
        ordering = ["annee"]


class Media(models.Model):
    nom = models.CharField(max_length=255)
    fichier = models.CharField(max_length=255)
    type_mime = models.CharField(max_length=100, blank=True, null=True)
    taille = models.IntegerField(blank=True, null=True)
    largeur = models.IntegerField(blank=True, null=True)
    hauteur = models.IntegerField(blank=True, null=True)
    alt = models.CharField(max_length=255, blank=True, null=True)
    date_creation = models.DateTimeField(default=timezone.now)
    date_modification = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = "media"
        ordering = ["-date_creation"]


class SectionAccueil(models.Model):
    TYPE_HERO = "hero"
    TYPE_PRESENTATION = "presentation"
    TYPE_CUSTOM = "custom"
    TYPE_SLIDER = "slider"
    TYPE_PARTENAIRE = "partenaire"
    TYPE_MATCH = "match"
    titre = models.CharField(max_length=255)
    contenu = models.TextField(blank=True, null=True)
    image = models.CharField(max_length=255, blank=True, null=True)
    position = models.IntegerField(default=0)
    est_actif = models.BooleanField(default=True, null=True)
    type = models.CharField(max_length=50, default="texte")
    slider_mode = models.CharField(max_length=20, blank=True, null=True)
    slider_images = models.JSONField(blank=True, null=True)
    slider_categorie = models.ForeignKey(Categorie, on_delete=models.SET_NULL, null=True, blank=True, related_name="sections_slider")
    slider_bouton_texte = models.CharField(max_length=255, blank=True, null=True)
    slider_bouton_url = models.CharField(max_length=255, blank=True, null=True)
    slider_nb_cards = models.SmallIntegerField(default=3, blank=True, null=True)
    slider_show_arrows = models.BooleanField(default=False, blank=True, null=True)
    partenaire_images = models.JSONField(blank=True, null=True)

    class Meta:
        ordering = ["position"]


class Navbar(models.Model):
    nom = models.CharField(max_length=255)
    est_active = models.BooleanField(default=False, null=True)
    logo = models.CharField(max_length=255, blank=True, null=True)


class NavbarItem(models.Model):
    titre = models.CharField(max_length=255)
    type = models.CharField(max_length=255, default="lien")
    route = models.CharField(max_length=255, blank=True, null=True)
    page = models.ForeignKey(Page, on_delete=models.SET_NULL, null=True, blank=True, related_name="navbar_items")
    url_externe = models.CharField(max_length=500, blank=True, null=True)
    navbar = models.ForeignKey(Navbar, on_delete=models.CASCADE, related_name="items")
    parent = models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True, related_name="enfants")
    ordre = models.IntegerField(blank=True, null=True)

    class Meta:
        ordering = ["ordre"]


class Footer(models.Model):
    nom = models.CharField(max_length=255)
    est_actif = models.BooleanField(default=False)
    copyright = models.CharField(max_length=255, blank=True, null=True)


class FooterRow(models.Model):
    background_color = models.CharField(max_length=50, blank=True, null=True)
    footer = models.ForeignKey(Footer, on_delete=models.CASCADE, related_name="rows")
    ordre = models.IntegerField(blank=True, null=True)

    class Meta:
        ordering = ["ordre"]


class FooterColumn(models.Model):
    titre = models.CharField(max_length=255, blank=True, null=True)
    ordre = models.IntegerField(default=0)
    row = models.ForeignKey(FooterRow, on_delete=models.CASCADE, related_name="columns")

    class Meta:
        ordering = ["ordre"]


class FooterItem(models.Model):
    TYPE_TEXT = "text"
    TYPE_LINK = "link"
    TYPE_SOCIAL = "social"
    type = models.CharField(max_length=50, default=TYPE_TEXT)
    contenu = models.CharField(max_length=255)
    url = models.CharField(max_length=500, blank=True, null=True)
    page = models.ForeignKey(Page, on_delete=models.SET_NULL, null=True, blank=True, related_name="footer_items")
    route = models.CharField(max_length=255, blank=True, null=True)
    icone = models.CharField(max_length=50, blank=True, null=True)
    ordre = models.IntegerField(default=0)
    column = models.ForeignKey(FooterColumn, on_delete=models.CASCADE, related_name="items")

    class Meta:
        ordering = ["ordre"]


class Open86Config(models.Model):
    est_actif = models.BooleanField(default=False)
    titre = models.CharField(max_length=255, default="Open Masculin 86", blank=True, null=True)
    sous_titre = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    banniere = models.CharField(max_length=500, blank=True, null=True)
    logo = models.CharField(max_length=500, blank=True, null=True)
    date_debut = models.DateTimeField(blank=True, null=True)
    date_fin = models.DateTimeField(blank=True, null=True)


class Open86CouleurSite(models.Model):
    nom = models.CharField(max_length=255)
    couleur_primaire = models.CharField(max_length=7)
    couleur_secondaire = models.CharField(max_length=7)
    couleur_action = models.CharField(max_length=7)
    couleur_texte = models.CharField(max_length=7, blank=True, null=True)
    couleur_texte_navbar = models.CharField(max_length=7, blank=True, null=True)
    couleur_texte_bouton = models.CharField(max_length=7, blank=True, null=True)
    couleur_hero = models.CharField(max_length=7, blank=True, null=True)
    couleur_texte_hero = models.CharField(max_length=7, blank=True, null=True)
    couleur_presentation = models.CharField(max_length=7, blank=True, null=True)
    couleur_texte_presentation = models.CharField(max_length=7, blank=True, null=True)
    couleur_contenu = models.CharField(max_length=7, blank=True, null=True)
    couleur_texte_contenu = models.CharField(max_length=7, blank=True, null=True)
    couleur_partenaire = models.CharField(max_length=7, blank=True, null=True)
    couleur_card = models.CharField(max_length=7, blank=True, null=True)
    couleur_texte_card = models.CharField(max_length=7, blank=True, null=True)


class Open86Domaine(models.Model):
    nom = models.CharField(max_length=255)
    ordre = models.IntegerField(default=0, blank=True, null=True)

    class Meta:
        ordering = ["ordre", "nom"]


class Open86Partenaire(models.Model):
    nom = models.CharField(max_length=255)
    logo = models.CharField(max_length=255, blank=True, null=True)
    domaine = models.ForeignKey(Open86Domaine, on_delete=models.SET_NULL, null=True, blank=True, related_name="partenaires")
    lien = models.CharField(max_length=255, blank=True, null=True)


class Open86Edito(models.Model):
    nom = models.CharField(max_length=255)
    prenom = models.CharField(max_length=255)
    fonction = models.CharField(max_length=255)
    photo = models.CharField(max_length=255, blank=True, null=True)
    contenu = models.TextField(blank=True, null=True)
    ordre = models.IntegerField(default=0, blank=True, null=True)
    est_actif = models.BooleanField(default=True, null=True)

    class Meta:
        ordering = ["ordre"]


class Open86SectionAccueil(models.Model):
    titre = models.CharField(max_length=255)
    type = models.CharField(max_length=100, default="texte")
    contenu = models.TextField(blank=True, null=True)
    image = models.CharField(max_length=500, blank=True, null=True)
    lien_bouton = models.CharField(max_length=500, blank=True, null=True)
    texte_bouton = models.CharField(max_length=100, blank=True, null=True)
    ordre = models.IntegerField(default=0)
    est_actif = models.BooleanField(default=True)
    couleur_fond = models.CharField(max_length=50, blank=True, null=True)
    couleur_texte = models.CharField(max_length=50, blank=True, null=True)
    options = models.JSONField(blank=True, null=True)
    partenaire_images = models.JSONField(blank=True, null=True)

    class Meta:
        ordering = ["ordre"]


class Open86Navbar(models.Model):
    nom = models.CharField(max_length=255)
    est_actif = models.BooleanField(default=False)
    logo = models.CharField(max_length=500, blank=True, null=True)
    couleur_fond = models.CharField(max_length=50, blank=True, null=True)
    couleur_texte = models.CharField(max_length=50, blank=True, null=True)


class Open86NavbarItem(models.Model):
    label = models.CharField(max_length=255)
    url = models.CharField(max_length=500, blank=True, null=True)
    ordre = models.IntegerField(default=0)
    type = models.CharField(max_length=50, default="link", blank=True, null=True)
    icone = models.CharField(max_length=100, blank=True, null=True)
    est_actif = models.BooleanField(default=True)
    navbar = models.ForeignKey(Open86Navbar, on_delete=models.CASCADE, related_name="items")
    parent = models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True, related_name="children")

    class Meta:
        ordering = ["ordre"]


class Open86Footer(models.Model):
    nom = models.CharField(max_length=255)
    est_actif = models.BooleanField(default=False)
    couleur_fond = models.CharField(max_length=50, blank=True, null=True)
    couleur_texte = models.CharField(max_length=50, blank=True, null=True)
    copyright = models.TextField(blank=True, null=True)


class Open86FooterRow(models.Model):
    ordre = models.IntegerField(default=0)
    couleur_fond = models.CharField(max_length=50, blank=True, null=True)
    footer = models.ForeignKey(Open86Footer, on_delete=models.CASCADE, related_name="rows")

    class Meta:
        ordering = ["ordre"]


class Open86FooterColumn(models.Model):
    titre = models.CharField(max_length=255, blank=True, null=True)
    ordre = models.IntegerField(default=0)
    largeur = models.IntegerField(default=3)
    row = models.ForeignKey(Open86FooterRow, on_delete=models.CASCADE, related_name="columns")

    class Meta:
        ordering = ["ordre"]


class Open86FooterItem(models.Model):
    label = models.CharField(max_length=255)
    url = models.CharField(max_length=500, blank=True, null=True)
    ordre = models.IntegerField(default=0)
    type = models.CharField(max_length=50, default="link")
    icone = models.CharField(max_length=100, blank=True, null=True)
    est_actif = models.BooleanField(default=True)
    column = models.ForeignKey(Open86FooterColumn, on_delete=models.CASCADE, related_name="items", db_column="column_id")

    class Meta:
        ordering = ["ordre"]
