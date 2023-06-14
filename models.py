# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class KolomDataDatin(models.Model):
    no = models.CharField(db_column='NO', max_length=3)  # Field name made lowercase.
    wfm_orderid = models.CharField(db_column='WFM_ORDERID', max_length=43, blank=True, null=True)  # Field name made lowercase.
    wonum = models.CharField(db_column='WONUM', max_length=9, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='DESCRIPTION', max_length=33, blank=True, null=True)  # Field name made lowercase.
    wfm_status = models.CharField(db_column='WFM_STATUS', max_length=10, blank=True, null=True)  # Field name made lowercase.
    ownergroup = models.CharField(db_column='OWNERGROUP', max_length=23, blank=True, null=True)  # Field name made lowercase.
    schedstart = models.CharField(db_column='SCHEDSTART', max_length=19, blank=True, null=True)  # Field name made lowercase.
    ncx_orderid = models.CharField(db_column='NCX_ORDERID', max_length=13, blank=True, null=True)  # Field name made lowercase.
    oh_status = models.CharField(db_column='OH_STATUS', max_length=11, blank=True, null=True)  # Field name made lowercase.
    mile = models.CharField(db_column='MILE', max_length=24, blank=True, null=True)  # Field name made lowercase.
    ncx_status = models.CharField(db_column='NCX_STATUS', max_length=24, blank=True, null=True)  # Field name made lowercase.
    productname = models.CharField(db_column='PRODUCTNAME', max_length=17, blank=True, null=True)  # Field name made lowercase.
    order_type = models.CharField(db_column='ORDER_TYPE', max_length=11, blank=True, null=True)  # Field name made lowercase.
    bandwidth = models.CharField(db_column='BANDWIDTH', max_length=9, blank=True, null=True)  # Field name made lowercase.
    order_date = models.CharField(db_column='ORDER_DATE', max_length=19, blank=True, null=True)  # Field name made lowercase.
    date_provcomp = models.CharField(db_column='DATE_PROVCOMP', max_length=19)  # Field name made lowercase.
    date_billcomp = models.CharField(db_column='DATE_BILLCOMP', max_length=19)  # Field name made lowercase.
    customer_name = models.CharField(db_column='CUSTOMER_NAME', max_length=26, blank=True, null=True)  # Field name made lowercase.
    segment = models.CharField(db_column='SEGMENT', max_length=9, blank=True, null=True)  # Field name made lowercase.
    service_region = models.CharField(db_column='SERVICE_REGION', max_length=14, blank=True, null=True)  # Field name made lowercase.
    service_witel = models.CharField(db_column='SERVICE_WITEL', max_length=13, blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='ADDRESS', max_length=110, blank=True, null=True)  # Field name made lowercase.
    total_scaling = models.CharField(db_column='TOTAL_SCALING', max_length=13, blank=True, null=True)  # Field name made lowercase.
    nama_am = models.CharField(db_column='NAMA_AM', max_length=30, blank=True, null=True)  # Field name made lowercase.
    ticket_fo = models.CharField(db_column='TICKET_FO', max_length=324, blank=True, null=True)  # Field name made lowercase.
    tgl_create_ticket_fo = models.CharField(db_column='TGL_CREATE_TICKET_FO', max_length=20, blank=True, null=True)  # Field name made lowercase.
    durasi_fo = models.CharField(db_column='DURASI_FO', max_length=11, blank=True, null=True)  # Field name made lowercase.
    status_tl = models.CharField(db_column='STATUS_TL', max_length=10, blank=True, null=True)  # Field name made lowercase.
    keterangan_tl = models.CharField(db_column='KETERANGAN_TL', max_length=248, blank=True, null=True)  # Field name made lowercase.
    user_tl = models.CharField(db_column='USER_TL', max_length=14, blank=True, null=True)  # Field name made lowercase.
    tgl_tl = models.CharField(db_column='TGL_TL', max_length=6, blank=True, null=True)  # Field name made lowercase.
    worklog_create_by = models.CharField(db_column='WORKLOG_CREATE_BY', max_length=17, blank=True, null=True)  # Field name made lowercase.
    log_description = models.CharField(db_column='LOG_DESCRIPTION', max_length=15, blank=True, null=True)  # Field name made lowercase.
    log_detail_description = models.CharField(db_column='LOG_DETAIL_DESCRIPTION', max_length=22, blank=True, null=True)  # Field name made lowercase.
    sid = models.CharField(db_column='SID', max_length=21, blank=True, null=True)  # Field name made lowercase.
    notel = models.CharField(db_column='NOTEL', max_length=5, blank=True, null=True)  # Field name made lowercase.
    tti_kontak_berlangganan = models.CharField(db_column='TTI_KONTAK_BERLANGGANAN', max_length=23, blank=True, null=True)  # Field name made lowercase.
    target_nas = models.CharField(db_column='TARGET_NAS', max_length=10, blank=True, null=True)  # Field name made lowercase.
    target_treg = models.CharField(db_column='TARGET_TREG', max_length=11, blank=True, null=True)  # Field name made lowercase.
    target_witel = models.CharField(db_column='TARGET_WITEL', max_length=12, blank=True, null=True)  # Field name made lowercase.
    target_dso = models.CharField(db_column='TARGET_DSO', max_length=10, blank=True, null=True)  # Field name made lowercase.
    target_dit = models.CharField(db_column='TARGET_DIT', max_length=10, blank=True, null=True)  # Field name made lowercase.
    target_dss = models.CharField(db_column='TARGET_DSS', max_length=10, blank=True, null=True)  # Field name made lowercase.
    sto = models.CharField(db_column='STO', max_length=3, blank=True, null=True)  # Field name made lowercase.
    agreement_name = models.CharField(db_column='AGREEMENT NAME', max_length=47, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'kolom_data_datin'


class KolomDataHsi(models.Model):
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
    id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kolom_data_hsi'
