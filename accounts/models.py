# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.


from django.utils import timezone
import uuid
from django.db import models


class Educations(models.Model):
    educationid = models.UUIDField(primary_key=True)
    userid = models.ForeignKey('Users', models.DO_NOTHING, db_column='userid', blank=True, null=True)
    degree = models.CharField(max_length=100)
    institution = models.CharField(max_length=100)
    startyear = models.IntegerField(blank=True, null=True)
    endyear = models.IntegerField(blank=True, null=True)
    grade = models.CharField(max_length=20, blank=True, null=True)
    certificatefileid = models.ForeignKey('Files', models.DO_NOTHING, db_column='certificatefileid', blank=True, null=True)
    createdat = models.DateTimeField(blank=True, null=True)
    updatedat = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'educations'


class Feedback(models.Model):
    feedbackid = models.UUIDField(primary_key=True)
    meetingid = models.ForeignKey('Meetings', models.DO_NOTHING, db_column='meetingid', blank=True, null=True)
    rating = models.IntegerField(blank=True, null=True)
    comments = models.TextField(blank=True, null=True)
    createdat = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'feedback'


class Files(models.Model):
    fileid = models.UUIDField(primary_key=True)
    fileurl = models.TextField()
    purpose = models.CharField(max_length=50, blank=True, null=True)
    filetype = models.CharField(max_length=50, blank=True, null=True)
    uploadedby = models.ForeignKey('Users', models.DO_NOTHING, db_column='uploadedby', blank=True, null=True)
    uploadedat = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'files'


class Followrequests(models.Model):
    followrequestid = models.UUIDField(primary_key=True)
    menteeid = models.ForeignKey('Users', models.DO_NOTHING, db_column='menteeid', blank=True, null=True)
    mentorid = models.ForeignKey('Users', models.DO_NOTHING, db_column='mentorid', related_name='followrequests_mentorid_set', blank=True, null=True)
    status = models.CharField(max_length=10, blank=True, null=True)
    message = models.TextField(blank=True, null=True)
    createdat = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'followrequests'


class Learninggoals(models.Model):
    learninggoalid = models.UUIDField(primary_key=True)
    menteeid = models.ForeignKey('Users', models.DO_NOTHING, db_column='menteeid', blank=True, null=True)
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    targetdate = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=15, blank=True, null=True)
    createdat = models.DateTimeField(blank=True, null=True)
    updatedat = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'learninggoals'


class Meetingnotes(models.Model):
    meetingnoteid = models.UUIDField(primary_key=True)
    meetingid = models.ForeignKey('Meetings', models.DO_NOTHING, db_column='meetingid', blank=True, null=True)
    authorid = models.ForeignKey('Users', models.DO_NOTHING, db_column='authorid', blank=True, null=True)
    content = models.TextField()
    attachmentfileids = models.TextField(blank=True, null=True)  # This field type is a guess.
    createdat = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'meetingnotes'


class Meetings(models.Model):
    meetingid = models.UUIDField(primary_key=True)
    mentorid = models.ForeignKey('Users', models.DO_NOTHING, db_column='mentorid', blank=True, null=True)
    menteeid = models.ForeignKey('Users', models.DO_NOTHING, db_column='menteeid', related_name='meetings_menteeid_set', blank=True, null=True)
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    starttime = models.DateTimeField(blank=True, null=True)
    endtime = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=15, blank=True, null=True)
    meetinglink = models.TextField(blank=True, null=True)
    createdat = models.DateTimeField(blank=True, null=True)
    updatedat = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'meetings'


class Messages(models.Model):
    messageid = models.UUIDField(primary_key=True)
    senderid = models.ForeignKey('Users', models.DO_NOTHING, db_column='senderid', blank=True, null=True)
    receiverid = models.ForeignKey('Users', models.DO_NOTHING, db_column='receiverid', related_name='messages_receiverid_set', blank=True, null=True)
    content = models.TextField()
    isread = models.BooleanField(blank=True, null=True)
    sentat = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'messages'


class Profiles(models.Model):
    profileid = models.UUIDField(primary_key=True)
    userid = models.OneToOneField('Users', models.DO_NOTHING, db_column='userid', blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    mobile = models.CharField(max_length=20, blank=True, null=True)
    gender = models.CharField(max_length=10, blank=True, null=True)
    linkedinurl = models.TextField(blank=True, null=True)
    githuburl = models.TextField(blank=True, null=True)
    twitterurl = models.TextField(blank=True, null=True)
    instagramurl = models.TextField(blank=True, null=True)
    dob = models.DateField(blank=True, null=True)
    portfoliourl = models.TextField(blank=True, null=True)
    timezone = models.CharField(max_length=50, blank=True, null=True)
    profilepicfileid = models.ForeignKey(Files, models.DO_NOTHING, db_column='profilepicfileid', blank=True, null=True)
    createdat = models.DateTimeField(blank=True, null=True)
    updatedat = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'profiles'


class Specializations(models.Model):
    specializationid = models.UUIDField(primary_key=True)
    name = models.CharField(unique=True, max_length=50)
    category = models.CharField(max_length=50, blank=True, null=True)
    createdat = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'specializations'


class Users(models.Model):
    userid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.CharField(unique=True, max_length=100)
    passwordhash = models.TextField()
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    usertype = models.CharField(max_length=10)
    isverified = models.BooleanField(blank=True, null=True)
    isactive = models.BooleanField(default=True, blank=True, null=True)
    createdat = models.DateTimeField(default=timezone.now, null=True, blank=True)
    updatedat = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'


class Userspecializations(models.Model):
    userspecializationid = models.UUIDField(primary_key=True)
    userid = models.ForeignKey(Users, models.DO_NOTHING, db_column='userid', blank=True, null=True)
    specializationid = models.ForeignKey(Specializations, models.DO_NOTHING, db_column='specializationid', blank=True, null=True)
    proficiency = models.CharField(max_length=20, blank=True, null=True)
    role = models.CharField(max_length=10, blank=True, null=True)
    createdat = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'userspecializations'
        unique_together = (('userid', 'specializationid'),)
