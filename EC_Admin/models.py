from django.db import models

# Create your models here.
class Voters(models.Model):
    voterid_no = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100)
    father_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=6)
    dateofbirth = models.DateField()
    address = models.CharField(max_length=1024)
    mobile_no = models.BigIntegerField()
    state = models.CharField(max_length=50)
    pincode = models.CharField(max_length=6)
    parliamentary = models.CharField(max_length=50)
    assembly = models.CharField(max_length=50)
    voter_image = models.ImageField(upload_to='VoterImage/')


class Candidates(models.Model):
    candidate_id = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100)
    father_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=6)
    dateofbirth = models.DateField()
    address = models.CharField(max_length=1024)
    mobile_no = models.BigIntegerField()
    state = models.CharField(max_length=50)
    pincode = models.CharField(max_length=6)
    constituency = models.CharField(max_length=50)
    parliamentary = models.CharField(max_length=50, blank=True, null=True)
    assembly = models.CharField(max_length=50, blank=True, null=True)
    candidate_image = models.ImageField(upload_to='CandidateImage/')
    candidate_party = models.CharField(max_length=50)
    party_image = models.ImageField(upload_to='PartyImage/')
    affidavit = models.FileField(upload_to='CandidateAffidavit/', null=True)


class Election(models.Model):
    election_id = models.CharField(max_length=50, unique=True)
    election_type = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    start_date = models.DateField()
    start_time = models.TimeField()
    end_date = models.DateField()
    end_time = models.TimeField()
    status = models.CharField(max_length=10)


class Votes(models.Model):
    election_id = models.CharField(max_length=50)
    candidate_id = models.CharField(max_length=50)
    candidate_name = models.CharField(max_length=100)
    candidate_party = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    constituency = models.CharField(max_length=50)
    online_votes = models.BigIntegerField(default=0)
    evm_votes = models.BigIntegerField(default=0)
    total_votes = models.BigIntegerField(default=0)


class EC_Admins(models.Model):
    ecadmin_id = models.CharField(max_length=50, unique=True)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    middlename = models.CharField(max_length=100)
    gender = models.CharField(max_length=6)
    dateofbirth = models.DateField()
    address = models.CharField(max_length=1024)
    pincode = models.CharField(max_length=6)
    mobile_no = models.BigIntegerField(unique=True)
    email = models.EmailField(max_length=254, unique=True)
    ecadmin_image = models.ImageField(upload_to='ECAdminImage/')


    def __str__(self):
        return self.ecadmin_id


class Reports(models.Model):
    election_id = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    constituency = models.CharField(max_length=50)
    electors_male = models.BigIntegerField(default=0)
    electors_female = models.BigIntegerField(default=0)
    electors_others = models.BigIntegerField(default=0)
    electors_total = models.BigIntegerField(default=0)
    voters_male = models.BigIntegerField(default=0)
    voters_female = models.BigIntegerField(default=0)
    voters_others = models.BigIntegerField(default=0)
    voters_total = models.BigIntegerField(default=0)
    poll_male = models.FloatField()
    poll_female = models.FloatField()
    poll_others = models.FloatField()
    poll_total = models.FloatField()