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
        u'location': ''
}


def call_api():
    url = DOMAIN + PATH
    response = requests.get(url)
    response.raise_for_status()
    print(response.text)
    return response.text



def populate_json(json):
    data = call_api()
    json_file = json.loads(data)
    entry_collection = []
    for entry in json_file:
        entry = {
            u'rms_cdw_id': '',
            u'general_offense_number': '',
            u'offense_code': '',
            u'offense_code_extension': '',
            u'offense_type': '',
            u'summary_offense_code': '',
            u'summarized_offense_description': '',
            u'date_reported': '',
            u'occurred_date_or_date_range_start': '',
            u'occurred_date_range_end': '',
            u'hundred_block_location': '',
            u'district_sector': '',
            u'zone_beat': '',
            u'census_tract_2000': '',
            u'longitude': '',
            u'latitude': '',
            u'location': ''
        }
    entry_collection.append(entry)
    return entry_collection


def populate_db(entry):
    entries = Entry(**entry)
    DBSession.add(entry)


def import_entries():
    return populate_json()




if __name__ == '__main__':
    call_api()



