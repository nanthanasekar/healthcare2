from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
import plotly.express as px
import os

# Initialize Flask app
app = Flask(__name__)

# Folder to save uploaded files
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Route for the main dashboard page
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get the form data
        name = request.form['name']
        age = request.form['age']
        
        # Handle file upload
        file = request.files['file']
        if file:
            filename = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filename)
        
        # Load some healthcare data (can be CSV, database, etc.)
        df = pd.read_csv('data/healthcare_data.csv')

        # Generate a plot using Plotly
        fig = px.bar(df, x='Age', y='HealthScore', title='Age vs Health Score')

        # Convert plot to HTML and pass it to the template
        graph_html = fig.to_html(full_html=False)

        # Render the template with the graph and user inputs
        return render_template('index.html', graph_html=graph_html, name=name, age=age)

    return render_template('index.html', graph_html=None)

if __name__ == '__main__':
    app.run(debug=True)
