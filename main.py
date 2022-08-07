from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def portfolio():
    return render_template('index.html')


@app.route('/phone')
def phone():
    return render_template('phone.html')

@app.route('/contactme')
def contact_me():
    return render_template('contactme.html')

@app.route('/thankyou')
def thank_you():
    return render_template('thankyou.html')

if __name__ == '__main__':
    app.run()
