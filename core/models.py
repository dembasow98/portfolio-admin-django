from django.db import models

# Create your models here.

from django.db import models

from django.contrib.auth.models import User

from ckeditor_uploader.fields import RichTextUploadingField


# uuid library:
import uuid

# Use the django-countries
from django_countries.fields import CountryField

#Use the django-phone-field
from phonenumber_field.modelfields import PhoneNumberField



STATUS = (
    ('draft', 'Draft'),
    ('published', 'Published'),
    ('archived', 'Archived'),
    ('pending', 'Pending'),
    ('deleted', 'Deleted')
)


class Social(models.Model):

    # auto generated id
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='social_user')

    name = models.TextField()
    link = models.TextField()
    logo = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        unique_together = ("name", "link")

#class Image(models.Model):

class Image(models.Model):
    # auto generated id
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='image_user')

    image = models.ImageField(upload_to='images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Images"
    
    def __str__(self):
        return "Image"


class TrustBrand(models.Model):
    # auto generated id
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='trust_brand_user')

    image = models.ImageField(upload_to='images/', blank=True, null=True)
    name = models.TextField()
    link = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Trust Brands"
    
    def __str__(self):
        return self.name


class ContactInfo(models.Model):
    # auto generated id
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='contact_user')

    address = models.TextField()
    email = models.EmailField()
    #phone = PhoneNumberField(blank=True)
    map_location = models.TextField()


    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Contact Informations"
    
    def __str__(self):
        return "Contact"

    
class ContactMessage(models.Model):
    # auto generated id 
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='contact_message_user')

    full_name = models.TextField()
    email = models.EmailField()
    subject = models.TextField()
    message = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Contact Messages"
    
    def __str__(self):
        return "Contact Message"


class Client(models.Model):
    # auto generated id
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='client_user')

    profile = models.ImageField(upload_to='images/', blank=True, null=True)

    name = models.TextField()
    surname = models.TextField()
    job = models.TextField()
    # Nationality stores 3 datas country code, name, and flag
    nationality = CountryField(
        blank_label="select country",
        countries_flag_url="//flags.example.com/{code}.png",
        blank=True,
    )

    feedback = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Clients"
    
    def __str__(self):
        return self.name


class ExtraInfo(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='extra_info_user')

    years_of_experience = models.IntegerField(blank=True, null=True)
    
    github_stars = models.TextField(null=True)

    projects_completed = models.TextField(null=True)

    positive_feedback = models.TextField(null=True)

    happy_clients = models.TextField(null=True)

    cups_of_coffee = models.TextField(null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Extra Info"

    def __str__(self):
        return self.years_of_experience

class Skill(models.Model):
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='skill_user')

    name = models.TextField()

    description = models.TextField()

    link = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Skills"

    def __str__(self): 
        return self.name



class About(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='about_user')

    profile_picture = models.ImageField(upload_to='images/', blank=True, null=True)

    images = models.ManyToManyField(Image, blank=True, related_name='about_images')

    about = models.TextField()

    skills = models.ManyToManyField(Skill, related_name='about_skills')

    cv = models.FileField(upload_to='files/', blank=True, null=True)

    # Extra info
    extra_info = models.ManyToManyField(ExtraInfo, related_name='about_extra_info')

    # Trust Brands
    trust_brands = models.ManyToManyField(TrustBrand, related_name='about_trust_brands')

    # Clients
    clients = models.ManyToManyField(Client, related_name='about_clients')

    # Contact Info
    contact = models.ManyToManyField(ContactInfo, related_name='about_contact_info')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "About"
    

    def __str__(self): 
        return self.about
    
    

    

class Category(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name='category_user')

    name = models.TextField()
    description = models.TextField()
    link = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

class Tag(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name='tag_user')

    name = models.TextField()
    description = models.TextField()
    link = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Tags"

    def __str__(self):
        return self.name
    
class Technology(models.Model):
    # auto generated id
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name='technology_user')

    name = models.TextField(max_length=200, unique=True)

    description = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name_plural = "Technologies"

    def __str__(self):
        return self.name


class Post (models.Model):
    
    # auto generated id
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post_user')

    title = models.TextField()
    
    status = models.CharField(
        max_length=10,
        choices=STATUS,
        default='draft'
    )
    

    thumbnail = models.ImageField(upload_to='images/', blank=True, null=True)

    technologies = models.ManyToManyField(Technology, blank=True, related_name='post_technologies')
    
    categories = models.ManyToManyField(Category, blank=True, related_name='post_categories')

    tags = models.ManyToManyField(Tag, blank=True, related_name='post_tags')

  

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    content = RichTextUploadingField(verbose_name="Compose Content", blank=True, null=True)

    summary = models.TextField(verbose_name='Post Summary', blank=True, null=True)

    class Meta:
        unique_together = ("title", "content" )
        verbose_name_plural = "Posts"

    def __str__(self):
        return self.title



class Project(models.Model):
    
    # auto generated id
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name='project_user')

    title = models.TextField(max_length=200, unique=True)

    objective = models.TextField()

    # Project thumbnail:
    thumbnail = models.ImageField(upload_to='images/', blank=True, null=True)


    technologies = models.ManyToManyField(Technology, blank=True, related_name='project_technologies')
    
    categories = models.ManyToManyField(Category, blank=True, related_name='project_categories')

    tags = models.ManyToManyField(Tag, blank=True, related_name='project_tags')


    # Project Images:
    images = models.ManyToManyField(Image, blank=True, related_name='project_images')

    # Project Status:
    status = models.CharField(
        max_length=10,
        choices=STATUS,
        default='draft'
    )

    #Project Live Link:
    live_link = models.TextField(blank=True, null=True)
    source_link = models.TextField(blank=True, null=True)
    
   

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        unique_together = ("title", "objective" )
        verbose_name_plural = "Projects"

    def __str__(self):
        return self.title