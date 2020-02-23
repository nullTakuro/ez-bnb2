from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from login.models import profile

# DB models
# After each edit run this = python manage.py makemigrations
# and then this = python manage.py migrate

class property(models.Model):
    profile = models.ForeignKey(profile, on_delete = models.CASCADE)
    assigned_name = models.CharField(max_length = 30)      # As the value for this data is to be assigned below as the default return value for when a search query is run pertaining to this data its value cannot be null so a defualt value must be assigned!
    address = models.TextField(max_length = 60)
    town = models.TextField(max_length = 60)
    postcode = models.TextField(max_length = 20)
    county = models.TextField(max_length = 30)
    value = models.DecimalField(max_digits = 65, decimal_places = 2)

    def get_absolute_url(self):
        return reverse('propertyView', kwargs = {'pk' : self.pk})       # When a property is added using the form this will redirect the user to the view PropertyView which will display the details that the user just added

    def __str__(self):
        return self.assigned_name        # Returns the specific value as the value of the assigned_name

    class Meta:
        verbose_name = 'Propery'        # If this isn’t given, Django will use verbose_name + "s".
        verbose_name_plural = 'Properties'      # Overrides djangos built in plurisation which sets the verbose name as verbose_name + "s".

class contract(models.Model):
    property = models.ForeignKey(property, on_delete = models.CASCADE)
    start_date = models.DateField(auto_now = False, auto_now_add = False)        # A date and time, represented in Python by a datetime.datetime instance
    duration = models.DurationField()       # A field for storing periods of time - modeled in Python by timedelta. When used on PostgreSQL, the data type used is an interval and on Oracle the data type is INTERVAL DAY(9) TO SECOND(6).
    end_date = models.DateField(auto_now = False, auto_now_add = False)        # A date and time, represented in Python by a datetime.datetime instance
    creation_datetime = models.DateTimeField(auto_now = False, auto_now_add = True)     # Automatically set the field to now when the object is first created. Useful for creation of timestamps. Note that the current date is always used; it’s not just a default value that you can override. So even if you set a value for this field when creating the object, it will be ignored.
    last_modififed = models.DateTimeField(auto_now=True, auto_now_add=False)        # Automatically set the field to now every time the object is saved. Useful for “last-modified” timestamps. Note that the current date is always used; it’s not just a default value that you can override.
    rent = models.DecimalField(max_digits = 65, decimal_places = 2)
    rent_due_day = models.IntegerField(default = 1, validators = [MaxValueValidator(31), MinValueValidator(1)])
    auto_renew = models.BooleanField(default = False)

    def get_absolute_url(self):
        return reverse('ContractView', kwargs = {'pk' : self.pk})

    def __str__(self):
        return self.pk

class tenant(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female')
    )
    contract = models.ForeignKey(contract, on_delete = models.CASCADE)
    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length = 30)
    gender = models.CharField(max_length = 1, choices = GENDER_CHOICES)
    fiscal_ID = models.IntegerField(max_length = 20)

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)      # Returns the specific value as the value of the first_name last_name

class document(models.Model):
    tenant = models.ForeignKey(tenant, on_delete = models.CASCADE)
    number = models.CharField(max_length = 100)
    start_date = models.DateField(auto_now = False, auto_now_add = False)
    exp_date = models.DateField(auto_now = False, auto_now_add = False)
    valid = models.BinaryField(default = False)
    validation_date = models.DateField(auto_now = False, auto_now_add = False)
    validation_user = models.ForeignKey(profile, on_delete = models.CASCADE)

    def __str__(self):
        return self.number      # Returns the specific value as the value of number

class tax_payment(models.Model):
    contract = models.ForeignKey(contract, on_delete = models.CASCADE)
    profile = models.ForeignKey(profile, on_delete = models.CASCADE)
    year = models.IntegerField(max_length = 4)
    paid = models.BooleanField(default = False)
    next_due_date = models.DateField()
    amount = models.DecimalField(max_digits = 65, decimal_places = 2)

    def __str__(self):
        return self.year      # Returns the specific value as the value of the year

class rent_payment(models.Model):
    contract = models.ForeignKey(contract, on_delete = models.CASCADE)
    date = models.DateTimeField()
    amount = models.DecimalField(max_digits = 65, decimal_places = 2)
