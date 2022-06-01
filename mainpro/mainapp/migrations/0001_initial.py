# Generated by Django 3.2.6 on 2022-03-14 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PatientRegistration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uhid', models.CharField(max_length=50, unique=True)),
                ('registration_date_and_time', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(max_length=50)),
                ('first_name', models.CharField(max_length=100)),
                ('middle_name', models.CharField(blank=True, max_length=100, null=True)),
                ('last_name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('dob', models.DateField()),
                ('gender', models.CharField(max_length=50)),
                ('blood_group', models.CharField(blank=True, max_length=50, null=True)),
                ('marital_status', models.CharField(blank=True, max_length=50, null=True)),
                ('father_or_husband_name', models.CharField(max_length=100)),
                ('mother_name', models.CharField(blank=True, max_length=100, null=True)),
                ('mobile_num', models.CharField(max_length=10)),
                ('address', models.CharField(max_length=300)),
                ('referred_by', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('pin_code', models.CharField(max_length=8)),
                ('aadhar_card', models.CharField(blank=True, editable=False, max_length=100, null=True)),
                ('pan_card', models.CharField(blank=True, editable=False, max_length=100, null=True)),
                ('emergency_contact_num', models.CharField(blank=True, max_length=100, null=True)),
                ('alternate_contact_number', models.CharField(blank=True, max_length=100, null=True)),
                ('nationality', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('staff_member', models.CharField(blank=True, max_length=100, null=True)),
                ('relationship', models.CharField(blank=True, max_length=100, null=True)),
                ('allow_photo_at_nursing_station', models.BooleanField(blank=True, editable=False, max_length=100, null=True)),
                ('notable', models.BooleanField(blank=True, editable=False, max_length=100, null=True)),
                ('in_cash', models.BooleanField(blank=True, max_length=100, null=True)),
                ('is_senior_citizen', models.BooleanField(blank=True, max_length=100, null=True)),
                ('billing_group', models.CharField(max_length=100)),
                ('corporate_name', models.CharField(blank=True, max_length=100, null=True)),
                ('cardholder_name', models.CharField(blank=True, max_length=100, null=True)),
                ('card_number', models.CharField(blank=True, max_length=100, null=True)),
                ('relation', models.CharField(blank=True, max_length=100, null=True)),
                ('valid_upto', models.DateTimeField(auto_now=True, null=True)),
                ('sum_insured_amount', models.IntegerField(blank=True, null=True)),
                ('is_inactive', models.BooleanField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Visit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uhid', models.CharField(max_length=50, unique=True)),
                ('visit_date_and_time', models.DateTimeField()),
                ('visit_id', models.CharField(max_length=50)),
                ('visit_type', models.CharField(max_length=100)),
                ('description', models.CharField(blank=True, max_length=100, null=True)),
                ('visit_department_id', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='VitalSign',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sys_bp', models.CharField(max_length=100)),
                ('dia_bp', models.CharField(max_length=100)),
                ('temp', models.CharField(max_length=100)),
                ('weight', models.IntegerField()),
                ('height', models.IntegerField()),
                ('bmi', models.CharField(max_length=100)),
                ('resp_rate', models.CharField(blank=True, max_length=100, null=True)),
                ('heart_rate', models.CharField(blank=True, max_length=100, null=True)),
                ('urine_output', models.CharField(blank=True, max_length=100, null=True)),
                ('blood_sugar_f', models.CharField(blank=True, max_length=100, null=True)),
                ('blood_sugar_r', models.CharField(blank=True, max_length=100, null=True)),
                ('spo2', models.CharField(blank=True, max_length=100, null=True)),
                ('avpu', models.CharField(blank=True, max_length=100, null=True)),
                ('trauma', models.CharField(blank=True, max_length=100, null=True)),
                ('mobility', models.CharField(blank=True, max_length=100, null=True)),
                ('oxygen_supplementation', models.CharField(blank=True, max_length=100, null=True)),
                ('comments', models.TextField(blank=True, null=True)),
                ('visit_id', models.ForeignKey(on_delete=models.SET(1), to='mainapp.visit')),
            ],
        ),
        migrations.CreateModel(
            name='VisitHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('visit_date', models.CharField(blank=True, max_length=100, null=True)),
                ('doctor_name', models.CharField(blank=True, max_length=100, null=True)),
                ('visit_summary', models.CharField(blank=True, max_length=500, null=True)),
                ('prescription', models.CharField(blank=True, max_length=500, null=True)),
                ('discharge_summary', models.CharField(blank=True, max_length=500, null=True)),
                ('test_reports', models.CharField(blank=True, max_length=500, null=True)),
                ('visit_id', models.ForeignKey(on_delete=models.SET(0), to='mainapp.visit')),
            ],
        ),
        migrations.CreateModel(
            name='PresentingComplaints',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('presenting_complaints', models.CharField(blank=True, max_length=500, null=True)),
                ('initial_complaints', models.CharField(blank=True, max_length=500, null=True)),
                ('visit_id', models.ForeignKey(on_delete=models.SET(0), to='mainapp.visit')),
            ],
        ),
        migrations.CreateModel(
            name='Prescription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medicine_name', models.CharField(max_length=100)),
                ('dossage', models.CharField(max_length=100)),
                ('frequency', models.CharField(max_length=100)),
                ('no_of_days', models.CharField(max_length=100)),
                ('food_relation', models.CharField(max_length=100)),
                ('route', models.CharField(max_length=100)),
                ('instruction', models.CharField(max_length=100)),
                ('visit_id', models.ForeignKey(on_delete=models.SET(1), to='mainapp.visit')),
            ],
        ),
        migrations.CreateModel(
            name='NursingAssessment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nurse_form_id', models.CharField(blank=True, max_length=100, null=True)),
                ('nurse_form', models.CharField(blank=True, max_length=100, null=True)),
                ('form_details', models.CharField(blank=True, max_length=100, null=True)),
                ('visit_id', models.ForeignKey(on_delete=models.SET(0), to='mainapp.visit')),
            ],
        ),
        migrations.CreateModel(
            name='MedicalCertificate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('template', models.CharField(max_length=500)),
                ('visit_id', models.ForeignKey(on_delete=models.SET(0), to='mainapp.visit')),
            ],
        ),
        migrations.CreateModel(
            name='Diagnosis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attendance', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=100)),
                ('category', models.CharField(max_length=100)),
                ('diagnosis', models.CharField(max_length=100)),
                ('d_grg_code', models.CharField(blank=True, max_length=100, null=True)),
                ('icd_10', models.CharField(max_length=100)),
                ('status_of_diagnosis', models.CharField(blank=True, max_length=100, null=True)),
                ('adverse_effect', models.CharField(blank=True, max_length=100, null=True)),
                ('visit_id', models.ForeignKey(on_delete=models.SET(1), to='mainapp.visit')),
            ],
        ),
        migrations.CreateModel(
            name='CurrentMedication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medicine', models.CharField(max_length=100)),
                ('dossage', models.CharField(max_length=100)),
                ('frequency', models.CharField(max_length=100)),
                ('food_relation', models.CharField(max_length=100)),
                ('route', models.CharField(max_length=100)),
                ('prescribe_date', models.CharField(max_length=100)),
                ('end_date', models.CharField(max_length=100)),
                ('visit_date', models.CharField(max_length=100)),
                ('visit_id', models.ForeignKey(on_delete=models.SET(0), to='mainapp.visit')),
            ],
        ),
        migrations.CreateModel(
            name='Allergy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('allergy_type', models.CharField(blank=True, max_length=100, null=True)),
                ('allergen', models.CharField(blank=True, max_length=100, null=True)),
                ('reactive', models.CharField(blank=True, max_length=100, null=True)),
                ('immunizations', models.CharField(blank=True, max_length=100, null=True)),
                ('immunization_date', models.CharField(blank=True, max_length=100, null=True)),
                ('visit_id', models.ForeignKey(on_delete=models.SET(0), to='mainapp.visit')),
            ],
        ),
        migrations.CreateModel(
            name='Advice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pt_advice', models.CharField(max_length=100)),
                ('pt_advice_action', models.BooleanField(default=False)),
                ('visit_id', models.ForeignKey(on_delete=models.SET(1), to='mainapp.visit')),
            ],
        ),
    ]