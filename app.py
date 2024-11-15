from flask import Flask, render_template

app = Flask(__name__)

@app.route('/autobiography')
def autobiography():
    return render_template('autobiography.html')

@app.route('/metod')
def about():
    return render_template('metod.html')

@app.route('/recommendations')
def recommendations():
    return render_template('recommendations.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')


if __name__ == '__main__':
    app.run(debug=True)
