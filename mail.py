from flask import Flask
from flask_mail import Mail, Message
from flask import Flask, render_template, request

app = Flask(__name__)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'YOUR EMAIL ADDRESS'
app.config['MAIL_PASSWORD'] = 'YOUR PASSWORD'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)


@app.route('/')
def email_form():
   return render_template('email_input.html')

@app.route('/result', methods = ['POST', 'GET'])
def index():
   msg = Message(request.form['subject'], sender='helene.bieber093@gmail.com', recipients=[request.form['address']])
   msg.body = request.form['message']
   mail.send(msg)
   return render_template("email_output.html")

if __name__ == '__main__':
    app.run(debug=True)
    
