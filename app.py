from flask import Flask, render_template

# Initialize Flask app
app = Flask(__name__, static_url_path='/static')

# Route for the Spinner page
@app.route('/')
def spinner():
    return render_template('spinner.html')

# Route for the Jokes page
@app.route('/jokes')
def jokes():
    return render_template('jokes.html')

# Run the app
if __name__ == '__main__':
 app.run(host='0.0.0.0', port=5000, debug=True)

