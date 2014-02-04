from django.db import models

# Create your models here.

class User(models.Model):
    PHONE_PROVIDERS = (
        ('@sms.3rivers.net', '3 River Wireless'), ('@paging.acswireless.com', 'ACS Wireless'),
        ('@message.alltel.com', 'Alltel'), ('@txt.att.net', 'AT&T'), ('@txt.bellmobility.ca', 'Bell Canada'),
        ('@txt.bellmobility.ca', 'Bell Mobility'), ('@blueskyfrog.com', 'Blue Sky Frog'),
        ('@sms.bluecell.com', 'Bluegrass Cellular'), ('@myboostmobile.com', 'Boost Mobile'),
        ('@bplmobile.com', 'BPL Mobile'), ('@cwwsms.com', 'Carolina West Wireless'),
        ('@mobile.celloneusa.com', 'Cellular One'), ('@csouth1.com', 'Cellular South'),
        ('@cwemail.com', 'Centennial Wireless'), ('@messaging.centurytel.net', 'CenturyTel'),
        ('@msg.clearnet.com', 'Clearnet'), ('@comcastpcs.textmsg.com', 'Comcast'),
        ('@corrwireless.net', 'Corr Wireless Communications'), ('@mobile.dobson.net', 'Dobson'),
        ('@sms.edgewireless.com', 'Edge Wireless'), ('@fido.ca', 'Fido'), ('@sms.goldentele.com', 'Golden Telecom'),
        ('@messaging.sprintpcs.com', 'Helio'), ('@text.houstoncellular.net', 'Houston Cellular'),
        ('@ideacellular.net', 'Idea Cellular'), ('@ivctext.com', 'Illinois Valley Cellular'),
        ('@inlandlink.com', 'Inland Cellular Telephone'), ('@pagemci.com', 'MCI'), ('@mymetropcs.com', 'Metro PCS'),
        ('@fido.ca', 'Microcell'), ('@clearlydigital.com', 'Midwest Wireless'), ('@mobilecomm.net', 'Mobilcomm'),
        ('@text.mtsmobility.com', 'MTS'), ('domain', 'name'), ('@messaging.nextel.com', 'Nextel'),
        ('@onlinebeep.net', 'OnlineBeep'), ('@pcsone.net', 'PCS One'), ('@txt.bell.ca', 'President\'s Choice'),
        ('@sms.pscel.com', 'Public Service Cellular'), ('@qwestmp.com', 'Qwest'),
        ('@pcs.rogers.com', 'Rogers AT&T Wireless'), ('@pcs.rogers.com', 'Rogers Canada'),
        ('@txt.bell.ca', 'Solo Mobile'), ('@email.swbw.com', 'Southwestern Bell'),
        ('@messaging.sprintpcs.com', 'Sprint'),
        ('@tms.suncom.com', 'Sumcom'), ('@mobile.surewest.com', 'Surewest Communicaitons'),
        ('@tmomail.net', 'T-Mobile'),
        ('@msg.telus.com', 'Telus'), ('@txt.att.net', 'Tracfone'), ('@tms.suncom.com', 'Triton'),
        ('@utext.com', 'Unicel'),
        ('@email.uscc.net', 'US Cellular'), ('@uswestdatamail.com', 'US West'), ('@vtext.com', 'Verizon'),
        ('@vmobl.com', 'Virgin Mobile'), ('@vmobile.ca', 'Virgin Mobile Canada'),
        ('@sms.wcc.net', 'West Central Wireless'), ('@cellularonewest.com', 'Western Wireless'),
    )

    email = models.EmailField(primary_key=True, unique=True, max_length=254)
    pwd = models.CharField(max_length=254)
    phone_num = models.CharField(max_length=10)
    service_domain = models.CharField(max_length=32, choices=PHONE_PROVIDERS)


class Bill(models.Model):
    DATE_RANGE = (
        (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10'),
        (11, '11'), (12, '12'), (13, '13'), (14, '14'), (15, '15'), (16, '16'), (17, '17'), (18, '18'), (19, '19'),
        (20, '20'), (21, '21'), (22, '22'), (23, '23'), (24, '24'), (25, '25'), (26, '26'), (27, '28'), (28, '28'),
        (29, '29'), (30, '30'), (31, '31'),
    )

    payer_email = models.ForeignKey(User, null=False)
    pay_id = models.CharField(max_length=254, primary_key=True, null=False)
    payee_name = models.CharField(max_length=60, null=False)
    pay_amt = models.DecimalField(max_digits=11, decimal_places=2, null=False)
    pay_acct = models.CharField(max_length=64, null=False)
    pay_due_date = models.PositiveSmallIntegerField(null=False, choices=DATE_RANGE)


class Reminder(models.Model):
    sequence_num = models.CharField(max_length=64, null=False)
    reminder_id = models.ForeignKey(Bill, null=False)
    file_date = models.DateField(auto_now=False, auto_now_add=True, null=False)
    confirmed = models.BooleanField(null=False, default=False)
    confirm_date = models.DateField(auto_now_add=False, auto_now=False, null=True)
    psbm = models.DateField(auto_now=False, auto_now_add=False, null=False)
    last_notified = models.DateField(auto_now=True, auto_now_add=False, null=True)