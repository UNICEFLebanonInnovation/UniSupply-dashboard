import os
import datetime

from flask import Flask, redirect

from mongoengine import *

import flask_admin as admin
from flask_admin import BaseView, expose
from flask_admin.contrib.mongoengine.filters import FilterEqual
from flask_mongoengine import MongoEngine
from flask_admin.form import rules
from flask_admin.contrib.mongoengine import ModelView, EmbeddedForm

# Create application
app = Flask(__name__)

# Create dummy secrey key so we can use sessions
app.config['SECRET_KEY'] = '133456790'
app.config['MONGODB_SETTINGS'] = {
    'db': 'winter',
    'host': os.environ.get('MONGODB_URI', 'mongodb://localhost:27017/winter'),
}

# Create models
db = MongoEngine()
db.init_app(app)


# Define mongoengine documents
# class KoboData(DynamicEmbeddedDocument):
#
#     safe_water = BooleanField(db_field='Safe Water')
#     hands_washed = BooleanField(db_field='Hands Washed')
#     clean_latrines = BooleanField(db_field='Clean Latrines')
#     disease_prevention = BooleanField(db_field='Disease Prevention')
#     diseases = StringField(db_field='Diseases')
#
#     household_data = DictField(db_field='Metadata_section/household_data')


class SubmissionDetailsMixin(object):

    _id = StringField()
    p_code = StringField()
    p_code_name = StringField()
    district = StringField()
    cadastral = StringField()
    governorate = StringField()
    site_type = StringField(db_field='site-type')
    type = StringField()
    assistance_type = StringField()
    phone_number = StringField()
    phone_owner = StringField()
    latitude = StringField()
    longitude = StringField()
    first_name = StringField()
    middle_name = StringField()
    family_name = StringField()
    mothers_name = StringField()
    relationship_type = StringField()
    family_count = StringField()
    disabilities = StringField()
    official_id = StringField()
    gender = StringField()
    dob = StringField()
    marital_status = StringField()
    creation_date = StringField()
    completion_date = StringField()
    partner_name = StringField()
    moving_location = StringField()
    new_district = StringField()
    new_cadastral = StringField()
    _0_to_3_months = StringField()
    _3_to_12_months = StringField()
    _1_year_old = StringField()
    _2_years_old = StringField()
    _3_years_old = StringField()
    _4_years_old = StringField()
    _5_years_old = StringField()
    _6_years_old = StringField()
    _7_years_old = StringField()
    _8_years_old = StringField()
    _9_years_old = StringField()
    _10_years_old = StringField()
    _11_years_old = StringField()
    _12_years_old = StringField()
    _13_years_old = StringField()
    _14_years_old = StringField()
    male = StringField()
    female = StringField()
    _3_months_kit = StringField()
    _12_months_kit = StringField()
    _2_years_kit = StringField()
    _3_years_kit = StringField()
    _5_years_kit = StringField()
    _7_years_kit = StringField()
    _9_years_kit = StringField()
    _12_years_kit = StringField()
    _14_years_kit = StringField()
    _3_months_kit_completed = StringField()
    _12_months_kit_completed = StringField()
    _2_years_kit_completed = StringField()
    _3_years_kit_completed = StringField()
    _5_years_kit_completed = StringField()
    _7_years_kit_completed = StringField()
    _9_years_kit_completed = StringField()
    _12_years_kit_completed = StringField()
    _14_years_kit_completed = StringField()


class Visits(SubmissionDetailsMixin, DynamicEmbeddedDocument):
    pass


class Submissions(SubmissionDetailsMixin, DynamicDocument):

    visits = ListField(EmbeddedDocumentField(Visits))


# Customized admin views
class SubmissionView(ModelView):
    can_create = False
    can_delete = False
    can_export = True
    can_edit = False
    can_view_details = True
    page_size = 50

    column_list = (
        # 'p_code_internal_code',
        # 'p_code_name',
        # 'date',
        # 'visit',
        # 'by',
        # 'partner',
        # 'governorate',
        # 'total_tents',
        # 'individuals',
        # 'min_sample_tents',
        # 'free_of_open_defecation',
        # 'clean_environment',
        # 'no_solid_waste',
        # 'site_score',
        # 'safe_water',
        # 'hands_washed',
        # 'clean_latrines',
        # 'locked_latrines',
        # 'lighted_latrines',
        # 'diseases',
        # 'disease_prevention',
        # 'household_score',
        # 'total_score',
        # 'gbv_number',
        # 'gbv_number_female',
        # 'gbv_number_male',
        # 'gbv_number_female_negative',
        # 'gbv_number_male_negative',
        # 'gbv_score_percentage',
        # 'gbv_score_percentage_female',
        # 'gbv_score_percentage_male',
        # 'report',
    )

    column_filters = (
        '_id',
        'p_code',
        'p_code_name',
        'district',
        'cadastral',
        'site_type',
        'type',
        'phone_number',
        'phone_owner',
        'latitude',
        'longitude',
        'first_name',
        'middle_name',
        'family_name',
        'mothers_name',
        'relationship_type',
        'family_count',
        'disabilities',
        'official_id',
        'gender',
        'dob',
        'marital_status',
        'creation_date',
        'completion_date',
        'partner_name',
        'moving_location',
        'new_district',
        'new_cadastral',
        '_0_to_3_months',
        '_3_to_12_months',
        '_1_year_old',
        '_2_years_old',
        '_3_years_old',
        '_4_years_old',
        '_5_years_old',
        '_6_years_old',
        '_7_years_old',
        '_8_years_old',
        '_9_years_old',
        '_10_years_old',
        '_11_years_old',
        '_12_years_old',
        '_13_years_old',
        '_14_years_old',
        'male',
        'female',
        '_3_months_kit',
        '_12_months_kit',
        '_2_years_kit',
        '_3_years_kit',
        '_5_years_kit',
        '_7_years_kit',
        '_9_years_kit',
        '_12_years_kit',
        '_14_years_kit',
        '_3_months_kit_completed',
        '_12_months_kit_completed',
        '_2_years_kit_completed',
        '_3_years_kit_completed',
        '_5_years_kit_completed',
        '_7_years_kit_completed',
        '_9_years_kit_completed',
        '_12_years_kit_completed',
        '_14_years_kit_completed',
    )

    # column_searchable_list = (
    #     'p_code_internal_code',
    #     'p_code_name',
    #     'date',
    #     'visit',
    #     'by',
    #     'partner',
    #     'governorate',
    # )

    # form_subdocuments = {
    #     'visits': {
    #         'form_subdocuments': {
    #             None: {
    #                 # Add <hr> at the end of the form
    #                 'form_columns': (
    #                     'date',
    #                     'visit',
    #                     'partner',
    #                     'governorate',
    #                     'by',
    #                     'individuals',
    #                     'total_tents',
    #                     'min_sample_tents',
    #                     'actual_tents_sampled',
    #                     'free_of_open_defecation',
    #                     'clean_environment',
    #                     'no_solid_waste',
    #                     'safe_water',
    #                     'hands_washed',
    #                     'clean_latrines',
    #                     'locked_latrines',
    #                     'lighted_latrines',
    #                     'disease_prevention',
    #                     'total_score',
    #                     'diseases',
    #                     #'raw_data',
    #                     #rules.HTML('<hr>')
    #                 ),
    #                 'form_widget_args': {
    #                     'total_score': {
    #                         'style': 'color: red'
    #                     }
    #                 }
    #             }
    #         }
    #     }
    # }


# Create admin
admin = admin.Admin(app, 'UniSupply dashboard')

# Add views
admin.add_view(SubmissionView(Submissions))


# Flask views
@app.route('/')
def index():
    return redirect('/admin')


if __name__ == '__main__':
    # Start app
    app.run(debug=True, use_reloader=True)