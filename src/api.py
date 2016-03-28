import requests


DOMAIN = 'https://data.seattle.gov'
PATH = '/resource/ih58-ykqj.json'
PARAMS = {
        u'rms_cdw_id': '', 
        u'general_offense_number': '',
        u'offense_code': '',
        u'offense_code_extension': '', 
        u'offense_type': '', 
        u'summary_offense_code': '',
        u'summarized_offense_description': '', 
        u'date_reported': '',
        u'occurred_date_ordate_range_start': '', 
        u'occurred_date_range_end': '',
        u'hundred_block_location': '', 
        u'district_sector': '', 
        u'zone_beat': '',
        u'census_tract_2000': '', 
        u'longitude': '', 
        u'latitude': '', 
        u'location': '', 
        u'month': '',
        u'year': '',
    
}

def call_api(requests):


