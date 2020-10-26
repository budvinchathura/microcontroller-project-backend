import pprint
from flask import Blueprint, render_template, request, Response
from capparselib.parsers import CAPParser
from app.services import insert_records
SUBMIT_BP = Blueprint('SUBMIT_BP', __name__)


@SUBMIT_BP.route('/', methods=['POST'])
def submit():
    # print(request.data.decode("utf-8") )
    xml_output = ''
    status_code = 0
    try:
        alert_list = CAPParser(request.data.decode("utf-8") ).as_dict()
    except Exception:
        xml_output = '<?xml version="1.0" encoding="UTF-8"?><root> \
        <status>400</status><message>XML parsing failed</message></root>'
        status_code = 400
    else:    
        pp = pprint.PrettyPrinter(indent=2)
        pp.pprint(alert_list)
        insert_status = False;
        try:
            insert_status = insert_records(alert_list);
        except Exception:
            xml_output = '<?xml version="1.0" encoding="UTF-8"?><root> \
            <status>500</status><message>Server Error, Please Try Again</message></root>'
            status_code = 500
        else:            
            if insert_status:
                xml_output = '<?xml version="1.0" encoding="UTF-8"?><root> \
                <status>200</status><message>success</message></root>'
                status_code = 200
            else:        
                xml_output = '<?xml version="1.0" encoding="UTF-8"?><root> \
                <status>500</status><message>Database Error, Please Try Again</message></root>'
                status_code = 500

    return Response(xml_output, mimetype='text/xml', status=status_code)