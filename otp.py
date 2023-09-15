from flask import Flask, request, render_template, redirect, flash, session
import pyotp
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)  # Generate a strong secret key

# Define a function to generate a random OTP
def generate_random_otp():
    return str(pyotp.random_base32())

# Routes and View Functions
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    phone_number = request.form.get('phone_number')
    
    # Generate a random OTP
    otp_secret = generate_random_otp()
    
    flash(f'Random OTP generated: {otp_secret}')
    
    return redirect('/')

# ... other routes ...

if _name_ == '__main__':
    app.run(debug=True)
