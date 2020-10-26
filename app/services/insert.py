from app.services.db import insert_records_to_db
import datetime

sorted_keys = ['humidity', 'light', 'pressure', 'recorded', 'temperature']

def insert_records(cap_object):
    formatted_records = []
    for alert in cap_object:
        for info in alert['cap_info']:
            record = {}
            parameters = info['cap_parameter']
            for p in parameters:
                record[str(p['valueName'])] = p['value']
            if not(sorted(record.keys()) == sorted_keys):
                return False
            
            record['humidity'] = float(record['humidity'])
            record['light'] = float(record['light'])
            record['pressure'] = float(record['pressure'])
            record['temperature'] = float(record['temperature'])

            record['recorded'] = str(record['recorded'])

            record['received'] = datetime.datetime.now().astimezone().replace(microsecond=0).isoformat()
            formatted_records.append(record)
    return insert_records_to_db(formatted_records)
    
