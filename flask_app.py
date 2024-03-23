from flask import Flask, render_template, request, redirect, url_for, jsonify
import os
app = Flask(__name__)

# Specify the upload folder
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Data for the dropdowns
categories = {'Raipur': ['Raipur', 'Tilda', 'Abhanpur', 'Arang', 'Nava Raipur'],
 'Balodabazar': ['Balodabazar',  'Bhatapara',  'Bilaigarh',  'Palari',  'Kasdol',  'Simga'],
 'Gariyaband': ['Gariyaband', 'Deobhog', 'Chhura', 'Rajim'],
 'Mahasamund': ['Mahasamund', 'Saraipali', 'Basna', 'Pithoura'],
 'Durg': ['Durg', 'Dhamdha', 'Patan'],
 'Bemetara': ['Bemetara', 'Navagarh', 'Berla', 'Saja'],
 'Balod': ['Balod', 'Gunderdehi', 'Gurur', 'Dondilohara', 'Dallirajahara'],
 'Raigarh': ['Raigarh', 'Saranggarh', 'Kharsia', 'Gharghoda', 'Dharamjaygarh'],
 'Jashpur': ['Kunkuri', 'Paththalgaon', 'Bagicha', 'Jashpur'],
 'Bilaspur': ['Bilaspur',  'Pendraroad',  'Kota',  'Bilha',  'Marwahi',  'Masturi',  'Takhatpur'],
 'Mungeli': ['Mungeli', 'Lormi', 'Pathariya'],
 'Janjgir-Champa': ['Janjgir',  'Sakti',  'Champa',  'Dabra',  'Pamgarh',  'Malkharauda',  'Navagarh',  'Jaijaipur',  'Akaltara'],
 'Rajnandgaon': ['Rajnandgaon',  'Khairagarh',  'Chhuikhadan',  'Dongargarh',  'Ambagarh-Chowki',  'Mohla',  'Dongargaon',  'Gandai',  'Chhuriya'],
 'Kawardha': ['Kabirdham', 'Pandariya', 'Bodla'],
 'Surguja': ['Ambikapur', 'Sitapur'],
 'Surajpur': ['Surajpur', 'Pratappur'],
 'Balrampur': ['Balrampur', 'Rajpur', 'Ramanujganj', 'Kusmi'],
 'Koriya': ['Baikunthpur', 'Manendragarh', 'Bharatpur'],
 'Korba': ['Korba', 'Katghora', 'Pali', 'Hardibazar'],
 'Dhamtari': ['Dhamtari', 'Kurud', 'Nagri'],
 'Bastar': ['Jagdalpur', 'Kondagaon', 'Keshkal', 'Narainpur'],
 'Kanker': ['Kanker', 'Bhanupratappur', 'Antagarh', 'Pakhanjur'],
 'Dantewada': ['Dantewada', 'Bijapur', 'Sukma', 'Konta']}

# Function to check if the uploaded file is allowed
def allowed_file(filename):
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('index.html',  categories=categories)
@app.route('/get_options/<category>')
def get_options(category):
    options = categories.get(category, [])
    return jsonify(options)
@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return redirect(request.url)
    
    images = request.files.getlist('file')
    district = request.form['district']
    tehsil = request.form['tehsil']
    for file in images:
        if file.filename == '':
            return redirect(request.url)
        path = os.path.join(app.config['UPLOAD_FOLDER'],district, tehsil)
        if not os.path.exists(path):
            os.makedirs(path)
        if file and allowed_file(file.filename):
            filename = file.filename
            file.save(os.path.join(path, filename))
    return render_template('success_upload.html')

if __name__ == '__main__':
    app.run(debug=True)
