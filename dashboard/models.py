from django.db import models
from django.utils import timezone
# Create your models here.

    
class Myuser(models.Model):
    no = models.CharField(db_column='NO', max_length=5, blank=True, null=True)  # Field name made lowercase.
    order_id = models.CharField(db_column='ORDER_ID', max_length=9, blank=True, null=True)  # Field name made lowercase.
    regional = models.TextField(db_column='REGIONAL', blank=True, null=True)  # Field name made lowercase.
    witel = models.CharField(db_column='WITEL', max_length=6, blank=True, null=True)  # Field name made lowercase.
    sto = models.CharField(db_column='STO', max_length=3, blank=True, null=True)  # Field name made lowercase.
    unit = models.CharField(db_column='UNIT', max_length=4, blank=True, null=True)  # Field name made lowercase.
    jenispsb = models.CharField(db_column='JENISPSB', max_length=8, blank=True, null=True)  # Field name made lowercase.
    type_trans = models.CharField(db_column='TYPE_TRANS', max_length=10, blank=True, null=True)  # Field name made lowercase.
    type_layanan = models.CharField(db_column='TYPE_LAYANAN', max_length=12, blank=True, null=True)  # Field name made lowercase.
    type_channel = models.CharField(db_column='TYPE_CHANNEL', max_length=18, blank=True, null=True)  # Field name made lowercase.
    group_channel = models.CharField(db_column='GROUP_CHANNEL', max_length=13, blank=True, null=True)  # Field name made lowercase.
    flag_deposit = models.CharField(db_column='FLAG_DEPOSIT', max_length=13, blank=True, null=True)  # Field name made lowercase.
    status_resume = models.CharField(db_column='STATUS_RESUME', max_length=29, blank=True, null=True)  # Field name made lowercase.
    status_message = models.CharField(db_column='STATUS_MESSAGE', max_length=194, blank=True, null=True)  # Field name made lowercase.
    provider = models.CharField(db_column='PROVIDER', max_length=29, blank=True, null=True)  # Field name made lowercase.
    order_date = models.CharField(max_length=16)
    last_updated_date = models.CharField(max_length=17, blank=True, null=True)
    device_id = models.CharField(db_column='DEVICE_ID', max_length=19, blank=True, null=True)  # Field name made lowercase.
    hide = models.CharField(db_column='HIDE', max_length=4, blank=True, null=True)  # Field name made lowercase.
    package_name = models.CharField(db_column='PACKAGE_NAME', max_length=1800, blank=True, null=True)  # Field name made lowercase.
    loc_id = models.CharField(db_column='LOC_ID', max_length=32, blank=True, null=True)  # Field name made lowercase.
    ncli = models.CharField(db_column='NCLI', max_length=8, blank=True, null=True)  # Field name made lowercase.
    pots = models.CharField(db_column='POTS', max_length=10, blank=True, null=True)  # Field name made lowercase.
    speedy = models.CharField(db_column='SPEEDY', max_length=11, blank=True, null=True)  # Field name made lowercase.
    customer_name = models.CharField(db_column='CUSTOMER_NAME', max_length=14, blank=True, null=True)  # Field name made lowercase.
    contact_hp = models.CharField(db_column='CONTACT_HP', max_length=13, blank=True, null=True)  # Field name made lowercase.
    ins_address = models.CharField(db_column='INS_ADDRESS', max_length=100, blank=True, null=True)  # Field name made lowercase.
    gps_longitude = models.CharField(db_column='GPS_LONGITUDE', max_length=13, blank=True, null=True)  # Field name made lowercase.
    gps_latitude = models.CharField(db_column='GPS_LATITUDE', max_length=12, blank=True, null=True)  # Field name made lowercase.
    kcontact = models.CharField(db_column='KCONTACT', max_length=66, blank=True, null=True)  # Field name made lowercase.
    umur = models.CharField(db_column='UMUR', max_length=4, blank=True, null=True)  # Field name made lowercase.
    status_task = models.CharField(db_column='STATUS_TASK', max_length=11, blank=True, null=True)  # Field name made lowercase.
    schedule_labor = models.CharField(db_column='SCHEDULE_LABOR', max_length=16, blank=True, null=True)  # Field name made lowercase.
    act_start = models.CharField(db_column='ACT_START', max_length=16, blank=True, null=True)  # Field name made lowercase.
    amcrew = models.CharField(db_column='AMCREW', max_length=12, blank=True, null=True)  # Field name made lowercase.
    teknisi = models.CharField(db_column='TEKNISI', max_length=42, blank=True, null=True)  # Field name made lowercase.
    product = models.CharField(db_column='PRODUCT', max_length=8, blank=True, null=True)  # Field name made lowercase.
    engineer_memo = models.CharField(db_column='ENGINEER MEMO', max_length=158, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    kendala = models.CharField(db_column='KENDALA', max_length=17, blank=True, null=True)  # Field name made lowercase.
    sub_kendala = models.CharField(db_column='SUB KENDALA', max_length=14, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    description = models.CharField(db_column='DESCRIPTION', max_length=69, blank=True, null=True)  # Field name made lowercase.
    id = models.IntegerField(primary_key=True, blank=True, null=False)
    class Meta:
        managed = False
        db_table = 'kolom_data_hsi'

    def __str__(self):
        return self.nama