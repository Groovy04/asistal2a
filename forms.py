
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, SelectField, TextAreaField, ValidationError, PasswordField
from wtforms.validators import DataRequired, Email, InputRequired, Optional
from wtforms.fields.core import DateField, RadioField


#FORMS HERE
#FORMS TO BE INCLUDED - USERS, SALESMTPLANNED, SALESMTACTUAL, CUSTOMERS, ... OTHERS?
#////////////////////////////////////////////////////////////
class Login(FlaskForm):
    email = StringField("Lütfen e-mail adresinizi giriniz", validators=[DataRequired(), Email()]) #Check if true
    password = PasswordField("Lütfen şifrenizi giriniz", validators=[DataRequired()])
    submit = SubmitField("Sisteme Giriş")


class SalesMTPlanned(FlaskForm): #Will be transformed to a form structure.. check also integer vaidations..
    month_planned = SelectField(label='Ay', choices=[("Oca", "Oca"), 
                    ("Şub", "Şub"), ("Mar", "Mar"), ("Nis", "Nis"), ("May", "May"), ("Haz", "Haz")
                    , ("Tem", "Tem"), ("Agu", "Agu"), ("Eyl", "Eyl"), ("Eki", "Eki"), ("Kas", "Kas")
                    , ("Ara", "Ara") ], validators=[InputRequired()])
    year_planned = IntegerField("Yıl", validators=[InputRequired()]) #Is integer?1
    #period_planned = StringField("Enter the relevant period please", validators=[DataRequired()])
    tot_vol_planned = IntegerField("Toplam Planlanan Satış Hacmi - MT", validators=[InputRequired()]) #Is integer?
    tot_mf_planned = IntegerField("Toplam Planlanan Satış Hacmi MF Fazı - MT", validators=[InputRequired()])
    tot_anodize_planned = IntegerField("Toplam Planlanan Satış Hacmi Anodize Fazı - MT", validators=[InputRequired()])
    tot_powder_coat_planned = IntegerField("Toplam Planlanan Satış Hacmi Powder Coating Fazı - MT", validators=[InputRequired()])
    tot_wood_finish_planned = IntegerField("Toplam Planlanan Satış Hacmi Wood Finish Fazı - MT", validators=[InputRequired()])
    tot_crimping_planned = IntegerField("Toplam Planlanan Satış Hacmi Crimping Fazı - MT", validators=[InputRequired()])
    tot_EUR_planned = IntegerField("EURO Bazlı Planlanan Toplam Satış Tutarı", validators=[InputRequired()])
    new_customers_planned = IntegerField("Planlanan Toplam Yeni Müşteri Sayısı", validators=[InputRequired()])
    submit = SubmitField("Bilgileri Kaydet")
    

#////////////////////////////////////////////////////////////
#NEW FORM
class SalesMTActual(FlaskForm): #Will be transformed to a form structure.. check also integer vaidations..
    month_actual = SelectField(label='Month', choices=[("Oca", "Oca"), 
                    ("Şub", "Şub"), ("Mar", "Mar"), ("Nis", "Nis"), ("May", "May"), ("Haz", "Haz")
                    , ("Tem", "Tem"), ("Agu", "Agu"), ("Eyl", "Eyl"), ("Eki", "Eki"), ("Kas", "Kas")
                    , ("Ara", "Ara") ], validators=[InputRequired()])
    year_actual = IntegerField("Yıl", validators=[InputRequired()]) #Is integer?1
    #period_actual = StringField("Enter the relevant period please", validators=[DataRequired()])
    tot_vol_actual = IntegerField("Toplam Gerçekleşen Satış Hacmi - MT", validators=[InputRequired()]) #Is integer?
    tot_mf_actual = IntegerField("Toplam Gerçekleşen Satış Hacmi MF Fazı - MT", validators=[InputRequired()])
    tot_anodize_actual = IntegerField("Toplam Gerçekleşen Satış Hacmi Anodize Fazı - MT", validators=[InputRequired()])
    tot_powder_coat_actual = IntegerField("Toplam Gerçekleşen Satış Hacmi Powder Coating Fazı - MT", validators=[InputRequired()])
    tot_wood_finish_actual = IntegerField("Toplam Gerçekleşen Satış Hacmi Wood Finish Fazı - MT", validators=[InputRequired()])
    tot_crimping_actual = IntegerField("Toplam Gerçekleşen Satış Hacmi Crimping Fazı - MT", validators=[InputRequired()])
    tot_EUR_actual = IntegerField("EURO Bazlı Gerçekleşen Toplam Satış Tutarı", validators=[InputRequired()])
    new_customers_actual = IntegerField("Gerçekleşen Toplam Yeni Müşteri Sayısı", validators=[InputRequired()])
    submit = SubmitField("Bilgileri Kaydet")



#//////////////////////////////////////////////////////////// customer1 form

StringField("Enter your email please..", validators=[DataRequired(), Email()])
IntegerField("Total Volume in MT in MF phase", validators=[InputRequired()])
SelectField(label='Month', choices=[("Jan", "Jan"), 
                    ("Feb", "Feb"), ("Mar", "Mar"), ("Apr", "Apr"), ("May", "May"), ("Jun", "Jun")
                    , ("Jul", "Jul"), ("Aug", "Aug"), ("Sep", "Sep"), ("Oct", "Oct"), ("Nov", "Nov")
                    , ("Dec", "Dec") ], validators=[InputRequired()])
new_date = DateField('DatePicker Test - New', format='%Y-%m-%d')


#Alttakini sileceğiz
def my_length_check(FlaskForm, field):
    if len(field.data) == 0:
        raise ValidationError('This field must be filled in')

"""class MyForm(Form):
    name = StringField('Name', [InputRequired(), my_length_check])"""

class Customer1(FlaskForm):
    
    company_name = StringField("Şirket İsmi", validators=[DataRequired()])
    
    staff1_name = StringField("Müşteri Personeli -1 Adı Soyadı", validators=[DataRequired()])
    staff1_birthdate = DateField('Müşteri Personeli -1 Doğumgünü', format='%Y-%m-%d', validators=[Optional()]) #!!! Optional validator boş bırakabilmemize olanak veriyor.
    staff1_personal_notes = TextAreaField("Müşteri Personeli -1 Kişisel Notlar ve Bilgiler")
    staff1_email = StringField("Müşteri Personeli -1 E-mail", validators=[DataRequired(), Email()])
    
    staff2_name = StringField("Müşteri Personeli -2 Adı Soyadı")
    staff2_birthdate = DateField('Müşteri Personeli -2 Doğumgünü', format='%Y-%m-%d', validators=[Optional()])
    staff2_personal_notes = TextAreaField("Müşteri Personeli -2 Kişisel Notlar ve Bilgiler")
    staff2_email = StringField("Müşteri Personeli -2 E-mail")

    staff3_name = StringField("Müşteri Personeli -3 Adı Soyadı")
    staff3_birthdate = DateField('Müşteri Personeli -3 Doğumgünü', format='%Y-%m-%d', validators=[Optional()])
    staff3_personal_notes = TextAreaField("Müşteri Personeli -3 Kişisel Notlar ve Bilgiler")
    staff3_email = StringField("Müşteri Personeli -3 E-mail")
        
    customer_tel1 = StringField("Müşteri Telefonu -1")
    customer_tel2 = StringField("Müşteri Telefonu -2") 
    customer_tel3 = StringField("Müşteri Telefonu -3")
    customer_website = StringField("Customer Website")
    customer_type = SelectField(label='Müşteri Türü', choices=[("Actual/Aktif", "Actual/Aktif"), ("Prospect/Muhtemel", "Prospect/Muhtemel"), ("Suspect/Potansiyel", "Suspect/Potansiyel")])
    customer_notes = TextAreaField("Müşteri Hakkında Notlar")
    local_international  = SelectField(label='Yerel - Uluslararası Müşteri', choices=[("Yerel", "Yerel"), ("Uluslararası", "Uluslararası"), 
                                    ("Hem Uluslararası hem Yerel", "Hem Uluslararası hem Yerel")])
    customer_country = SelectField(label='Müşteri Ülkesi', choices=[("Türkiye", "Türkiye"),
                                    ("Almanya", "Almanya"), ("Amerika", "Amerika"),
                                     ("Azerbaycan", "Azerbaycan"),
                                     ("Belçika", "Belçika"),("Benin", "Benin"),
                                     ("Bosna Hersek", "Bosna Hersek"),
                                     ("Bulgaristan", "Bulgaristan"),("Çekya", "Çekya"),("Ermenistan", "Ermenistan"),("Fas", "Fas"),("Gürcistan", "Gürcistan"),("Hırvatistan", "Hırvatistan"),("Hollanda", "Hollanda"), ("İngiltere", "İngiltere"), ("Irak", "Irak"), ("İran", "İran"), ("İsrail", "İsrail"),("İsveç", "İsveç"), ("İtalya", "İtalya"),("Gana", "Gana"), ("Kanada", "Kanada"),("Karadağ", "Karadağ"), ("Katar", "Katar"), ("Kazakistan", "Kazakistan"),  ("Kıbrıs", "Kıbrıs"), ("Kosova", "Kosova"), ("Lübnan", "Lübnan"),("Kuveyt", "Kuveyt"), ("Libya", "Libya"), ("Macaristan", "Macaristan"), ("Makedonya", "Makedonya"), ("Malta", "Malta"), ("Moldova", "Moldova"),("Özbekistan", "Özbekistan"), ("Panama", "Panama"), ("Polonya", "Polonya"),("Romanya", "Romanya"),("Sırbistan", "Sırbistan"), ("Slovakya", "Slovakya"),("Slovenya", "Slovenya"),("Tunus", "Tunus"),("Ukrayna", "Ukrayna"), ("Yunanistan", "Yunanistan"), ("Diğer", "Diğer")])
                                    
    customer_address = StringField("Müşteri Adresi")
    last_offer_date = DateField('Müşteriye Son Gönderilen Teklif Tarihi', format='%Y-%m-%d', validators=[Optional()])
    last_offer_result = SelectField(label='Gönderilen Son Teklifin Sonucu', choices=[("Kabul Edildi", "Kabul Edildi"), ("Red Edildi", "Red Edildi"), 
                                    ("Beklemede", "Beklemede")])
    rejection_reason = StringField("Red Sebebi - Eğer Red Edildi İSe")
    customer_source = SelectField(label='Müşteri Bize Nasıl Ulaşmış?', choices=[("Info e-mail/Web Sitesi", "Info e-mail/Web Sitesi"), 
                    ("Referans", "Referans"), ("Ticari Fuar", "Ticari Fuar"), ("Sosyal Medya", "Sosyal Medya"), 
                    ("Diğer", "Diğer")])
    reference_name = StringField("Referans Adı - Var İse")
    competitor_name = StringField("Müşterinin İş Yaptığı Diğer Rakipler - Var İse")
    competitor_conditions = StringField("Rakiplerin Satış Koşulları - Var İse")
    gender = SelectField(label='Gender of staff 1', choices=[("Bay", "Bay"), ("Bayan", "Bayan"), 
                                    ("Belirtilmemiş", "Belirtilmemiş")])
    prefix = SelectField(label='Müşteri Personeli -1 Ön Ek', choices=[("Mr.", "Mr."), ("Mrs.", "Mrs."), 
                                    ("Ms.", "Ms."), ("Belirtilmemiş", "Belirtilmemiş")])
    language1  = StringField("Şirkette Konuşulan Dil - 1")
    language2  = StringField("Şirkette Konuşulan Dil  - 2")
    language3  = StringField("Şirkette Konuşulan Dil  - 3")
    language4  = StringField("Şirkette Konuşulan Dil  - 4")
    
    submit = SubmitField("Müşteri Bilgilerini Kaydet")

    
    #Custom validation does not work??? Check this out
    def validate_companyname(self, company_name):
        if len(company_name.data)==0:
            raise ValidationError('Bu alan doldurulmalıdır!!!')
#//////////////////////////////////////////////////////////// end of customer1 form

#//////////////////////////////////////////////////////////// beginning of customer1 search form

class Customer1_Search_Form(FlaskForm):    
    search_company_name = StringField("Lütfen aradığınız müşterinin(firma adı) adını giriniz. Firma adının bir kısmını da girebilirsiniz. ", validators=[DataRequired()])      
    submit = SubmitField("Müşteri Ara")


#//////////////////////////////////////////////////////////// end of customer1 search form

#////////////////////////////////////////////////////////////

"""#////////////////First example
class MyForm(FlaskForm):
    name = StringField('Name', [InputRequired()])
    def validate_name(form, field):
        if len(field.data) > 50:
            raise ValidationError('Name must be less than 50 characters')
#////////////////Second example
def my_length_check(form, field):
    if len(field.data) > 50:
        raise ValidationError('Field must be less than 50 characters')
class MyForm(Form):
    name = StringField('Name', [InputRequired(), my_length_check])"""


#////////////////////////////////////////////////////////////END-OF FORMS