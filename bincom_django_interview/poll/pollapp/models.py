from django.db import models


class agentname(models.Model):
    name_id=                 models.PositiveIntegerField()
    firstname =               models.CharField(max_length=255)
    lastname =                models.CharField(max_length=255)
    email =                   models.EmailField(max_length=255)
    phone =                   models.CharField(max_length=13)  
    pollingunit_uniqueid =    models.PositiveIntegerField()

    def __str__(self):
        return self.firstname

    class Meta:
        db_table = "agentname"
  
  
class announced_lga_results(models.Model):
    result_id           = models.PositiveIntegerField()
    lga_name            = models.CharField(max_length=50)
    party_abbreviation  = models.CharField(max_length=4)
    party_score         = models.PositiveIntegerField()
    entered_by_user     = models.CharField(max_length=50)
    date_entered        = models.DateTimeField()
    user_ip_address     = models.CharField(max_length=50)

    def __str__(self):
        return self.lga_name

    class Meta:
        db_table = "announced_lga_results"
    
    
class announced_pu_results(models.Model):
    result_id               = models.PositiveIntegerField()
    polling_unit_uniqueid   = models.CharField(max_length=50)
    party_abbreviation      = models.CharField(max_length=4)
    party_score             = models.PositiveIntegerField()
    entered_by_user         = models.CharField(max_length=50)
    date_entered            = models.DateTimeField()
    user_ip_address         = models.CharField(max_length=50)

    def __str__(self):
        return self. party_abbreviation

    class Meta:
        db_table = "announced_pu_results"
      

class announced_state_results(models.Model):
    result_id          = models.PositiveIntegerField()
    state_name         = models.CharField(max_length=50)
    party_abbreviation = models.CharField(max_length=4)
    party_score        = models.PositiveIntegerField()
    entered_by_user    = models.CharField(max_length=50)
    date_entered       = models.DateTimeField()
    user_ip_address    = models.CharField(max_length=50)

    def __str__(self):
        return self.state_name

    class Meta:
        db_table = "announced_state_results"
  

class announced_ward_results(models.Model):
    result_id           = models.PositiveIntegerField()
    ward_name           = models.CharField(max_length=50)
    party_abbreviation  = models.CharField(max_length=4)
    party_score         = models.PositiveIntegerField()
    entered_by_user      = models.CharField(max_length=50)
    date_entered       = models.DateTimeField()
    user_ip_address    = models.CharField(max_length=50)

    def __str__(self):
        return self.ward_name

    class Meta:
        db_table = "announced_ward_results"
  
  
class lga(models.Model):
    uniqueid              = models.PositiveIntegerField()
    lga_id                = models.PositiveIntegerField()
    lga_name              = models.CharField(max_length=50)
    state_id              = models.PositiveIntegerField()
    lga_description       = models.TextField()
    entered_by_user      = models.CharField(max_length=50)
    date_entered       = models.DateTimeField()
    user_ip_address    = models.CharField(max_length=50)

    def __str__(self):
        return self.lga_name

    class Meta:
        db_table = "lga"
  

class party(models.Model):
    pid       = models.PositiveIntegerField()
    partyid       = models.CharField(max_length=50)
    partyname       = models.CharField(max_length=11)

    def __str__(self):
        return self.partyname

    class Meta:
        db_table = "party"
    

class polling_unit(models.Model):
    uniqueid                        = models.PositiveIntegerField(null=True, blank=True)
    polling_unit_id                        = models.PositiveIntegerField(null=True, blank=True)
    ward_id                        = models.PositiveIntegerField(null=True, blank=True)
    lga_id                        = models.PositiveIntegerField(null=True, blank=True)
    uniquewardid                        = models.PositiveIntegerField(null=True, blank=True)
    polling_unit_number           = models.CharField(max_length=50, null=True, blank=True)
    polling_unit_name              = models.CharField(max_length=50, null=True, blank=True)
    polling_unit_description      = models.TextField(null=True, blank=True)
    lat                        = models.CharField(max_length=255, null=True, blank=True)
    long                        = models.CharField(max_length=255, null=True, blank=True)
    entered_by_user             = models.CharField(max_length=50, null=True, blank=True)
    date_entered                = models.DateTimeField(null=True, blank=True)
    user_ip_address             = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return f"{self.polling_unit_id}"

    class Meta:
        db_table = "polling_unit"
    
    
class states(models.Model):
    state_id    = models.PositiveIntegerField()
    state_name  = models.CharField(max_length=50)

    def __str__(self):
        return self.state_name

    class Meta:
        db_table = "states"
    

class ward(models.Model):
    uniqueid         = models.PositiveIntegerField()
    ward_id         = models.PositiveIntegerField()
    ward_name         = models.CharField(max_length=50)
    lga_id         = models.PositiveIntegerField()
    ward_description    = models.TextField()
    entered_by_user         = models.CharField(max_length=50)
    date_entered          = models.DateTimeField()
    user_ip_address         = models.CharField(max_length=50)

    def __str__(self):
        return self.ward_name

    class Meta:
        db_table = "ward"
