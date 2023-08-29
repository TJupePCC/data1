from flask import redirect, jsonify, render_template, request
import pandas as pd
from app.models import db, Fooditems
from flask import Blueprint

routes_bp = Blueprint(
    'routes_bp', __name__,
    template_folder='templates',
    static_folder='static'
)


@routes_bp.route('/api/fooditems')
def get_fooditems():
    df = pd.read_csv('fastfood.csv', usecols=["restaurant", "item", "calories"])
    json_data = df.values.tolist()  # Convert DataFrame to list of lists
    print(jsonify(json_data))
    return jsonify(json_data)


@routes_bp.route('/')
def home():
    return render_template('table.html')


@routes_bp.route('/import')
def import_csv():
    title = 'Import Datasets'
    return render_template('import.html', title=title)


@routes_bp.route('/import/upload_file', methods=['POST'])
def upload_file():
    # get the uploaded file
    uploaded_file = request.files['file']
    # if not empty
    if uploaded_file.filename != '':
        # set the file path
        # file_path = os.path.join(config.UPLOAD_FOLDER, uploaded_file.filename)
        # save the file
        uploaded_file.save(uploaded_file.filename)
        parse_csv(uploaded_file.filename)
    return redirect('/import')


def parse_csv(file_path):
    # Use Pandas to parse the CSV file
    csv_data = pd.read_csv(file_path)
    # Loop through the rows and create a Student object for each row
    for i, row in csv_data.iterrows():
        fooditem = Fooditems(
            restaurant=row['restaurant'],
            item=row['item'],
            calories=row['calories']
        )
        # Insert each grade into db
        db.session.add(fooditem)
    db.session.commit()
