from flask import Blueprint, render_template
from app.services.fetch import fetch
HOME_BP = Blueprint('HOME_BP', __name__)


@HOME_BP.route('/', methods=['GET'])
def home():
    output_data = fetch()
    return render_template('home.html', name="John doe", output_data=output_data)