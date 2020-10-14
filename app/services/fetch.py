from app.services.db import fetch_all_records
from datetime import datetime


def fetch():
    all_records = fetch_all_records()
    for record in all_records:
        record['recorded'] = datetime.fromisoformat(record['recorded']).strftime("%Y-%m-%d %H:%M:%S")
        record['received'] = datetime.fromisoformat(record['received']).strftime("%Y-%m-%d %H:%M:%S")
        del record['_id']
    latest_record = all_records[0]
    all_records = all_records[1:]
    return {'latest_record': latest_record, 'all_records': all_records}
