from django import forms
from .models import Myuser

class UserForm(forms.ModelForm):
    class Meta:
        model = Myuser
        fields = ['no', 'order_id','regional','witel','sto','unit','jenispsb','type_trans',
                  'type_layanan','type_channel','group_channel','flag_deposit','status_resume',
                  'status_message','provider','order_date','last_updated_date','device_id','hide',
                  'package_name','loc_id','ncli','pots','speedy','customer_name','contact_hp',
                  'ins_address','gps_longitude','gps_latitude','kcontact','umur','status_task',
                  'schedule_labor','act_start','amcrew','teknisi','product','engineer_memo','kendala',
                  'sub_kendala','description', 'id']
        