from django.db import models

# Create your models here.

from django.db import models

from django.contrib.auth.models import User

from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.postgres.fields import ArrayField

# uuid library:

import uuid

from multiselectfield import MultiSelectField

class CustomMultiSelectField(MultiSelectField):
    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 255  # Set the maximum length
        super().__init__(*args, **kwargs)


CATEGORIES = (
    ('0', 'Full Stack Development'),
    ('1', 'Web Development'), 
    ('2', 'Mobile Development'), 
    ('3', 'Desktop Development'), 
    ('4', 'Machine Learning'), 
    ('5', 'Data Science'), 
    ('6', 'Artificial Intelligence'), 
    ('7', 'Cloud Computing'), 
    ('8', 'DevOps'), 
    ('9', 'Cyber Security'), 
    ('10', 'Game Development'), 
    ('11', 'Robotics'), 
    ('12', 'Internet of Things'), 
    ('13', 'Blockchain'), 
    ('14', 'Augmented Reality'), 
    ('15', 'Virtual Reality'), 
    ('16', 'Mixed Reality'), 
    ('17', 'Quantum Computing'), 
    ('18', 'Big Data'), 
    ('19', 'Other')
)

TAGS = (
    ('0', 'C'),
    ('1', 'Python'),
    ('2', 'Java'),
    ('3', 'C++'),
    ('4', 'C#'),
    ('5', 'JavaScript'),
    ('6', 'PHP'),
    ('7', 'Swift'),
    ('8', 'Kotlin'),
    ('9', 'Dart'),
    ('10', 'Ruby'),
    ('11', 'Go'),
    ('12', 'R'),
    ('13', 'Scala'),
    ('14', 'Rust'),
    ('15', 'TypeScript'),
    ('16', 'SQL'),
    ('17', 'HTML'),
    ('18', 'CSS'),
    ('19', 'React'),
    ('20', 'Tailwind CSS'),
    ('21', 'MongoDB'),
    ('22', 'Artificial Intelligence'),
    ('23', 'Machine Learning'),
    ('24', 'Deep Learning'),
    ('25', 'Data Science'),
    ('26', 'Big Data'),
    ('27', 'Cloud Computing'),
    ('28', 'DevOps'),
    ('29', 'Blockchain'),
    ('30', 'Internet of Things (IoT)'),
    ('31', 'Virtual Reality (VR)'),
    ('32', 'Augmented Reality (AR)'),
    ('33', 'Cybersecurity'),
    ('34', 'Responsive Web Design'),
    ('35', 'Progressive Web Apps (PWA)'),
    ('36', 'Microservices'),
    ('37', 'Serverless Architecture'),
    ('38', 'Containerization'),
    ('39', 'Git'),
    ('40', 'Jenkins'),
    ('41', 'Docker'),
    ('42', 'Kubernetes'),
    ('43', 'Amazon Web Services (AWS)'),
    ('44', 'Microsoft Azure'),
    ('45', 'Google Cloud Platform (GCP)'),
    ('46', 'WordPress'),
    ('47', 'Drupal'),
    ('48', 'Joomla'),
    ('49', 'Magento'),
    ('50', 'Salesforce'),
    ('51', 'Shopify'),
    ('52', 'WooCommerce'),
    ('53', 'Squarespace'),
    ('54', 'Wix'),
    ('55', 'Weebly'),
    ('56', 'Blogger'),
    ('57', 'Ghost'),
    ('58', 'Medium'),
    ('59', 'Tumblr')
)


FRAMEWORKS = (
    ('1', 'Django'),
    ('2', 'Flask'),
    ('3', 'React'),
    ('4', 'Angular'),
    ('5', 'Vue'),
    ('6', 'Laravel'),
    ('7', 'Spring'),
    ('8', 'Express'),
    ('9', 'Django Rest Framework'),
    ('10', 'Flutter'),
    ('11', 'React Native'),
    ('12', 'Ionic'),
    ('13', 'Xamarin'),
    ('14', 'Electron'),
    ('15', 'HUGO'),
    ('16', 'Gatsby'),
    ('17', 'Next.js'),
    ('18', 'Nuxt.js'),
    ('19', 'Jekyll'),
    ('20', 'Ruby on Rails'),
    ('21', 'ASP.NET'),
    ('22', 'ASP.NET Core'),
    ('23', 'Spring Boot'),
    ('24', 'Express.js'),
    ('25', 'Vue.js'),
    ('26', 'AngularJS'),
    ('27', 'Ember.js'),
    ('28', 'MeteorJS'),
    ('29', 'CakePHP'),
    ('30', 'CodeIgniter'),
    ('31', 'Zend Framework'),
    ('32', 'Yii'),
    ('33', 'Symfony'),
    ('34', 'Phalcon'),
    ('35', 'Vite.js'),
    ('36', 'Svelte'),
    ('37', 'Quasar'),
    ('38', 'Tailwind CSS'),
    ('39', 'Bootstrap'),
    ('40', 'Materialize'),
    ('41', 'Bulma'),
    ('42', 'Foundation'),
    ('43', 'Semantic UI'),
    ('44', 'UIKit'),
    ('45', 'Ant Design'),
    ('46', 'Chakra UI'),
    ('47', 'Tailwind UI'),
    ('48', 'PrimeReact'),
)


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

    frameworks = CustomMultiSelectField(choices=FRAMEWORKS, blank=True, null=True)
    

    categories = CustomMultiSelectField(choices=CATEGORIES, blank=True, null=True)

    tags = CustomMultiSelectField(choices=TAGS, blank=True, null=True)

  

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    content = RichTextUploadingField(verbose_name="Compose Content", blank=True, null=True)

    summary = models.TextField(verbose_name='Post Summary', blank=True, null=True)

    class Meta:
        unique_together = ("title", "content" )
        verbose_name_plural = "Posts"

    def __str__(self):
        return self.title


class Image(models.Model):
    # auto generated id
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    project = models.ForeignKey("Project", on_delete=models.CASCADE, related_name='project_image')
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Images"
    
    def __str__(self):
        return self.image

class Project(models.Model):
    
    # auto generated id
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name='project_user')

    title = models.TextField(max_length=200, unique=True)
    objective = models.TextField()

    # Project thumbnail:
    thumbnail = models.ImageField(upload_to='images/', blank=True, null=True)


    frameworks = CustomMultiSelectField(choices=FRAMEWORKS, blank=True, null=True)
    

    categories = CustomMultiSelectField(choices=CATEGORIES, blank=True, null=True)

    tags = CustomMultiSelectField(choices=TAGS, blank=True, null=True)

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