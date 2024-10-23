from flask import Flask, render_template, redirect, url_for, request, session, flash
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'
bcrypt = Bcrypt(app)

# Dummy data for product listings
products = [
    {"id": 1, "name": "Product 1", "price": 10.99, "image": "product1.jpg"},
    {"id": 2, "name": "Product 2", "price": 20.99, "image": "product2.jpg"},
    {"id": 3, "name": "Product 3", "price": 30.99, "image": "product3.jpg"}
]

# User credentials for login
users = {
    "user@example.com": bcrypt.generate_password_hash("password").decode('utf-8')
}

def add_user(email, password):
    if email in users:
        print(f"User {email} already exists.")
    else:
        users[email] = bcrypt.generate_password_hash(password).decode('utf-8')
        print(f"User {email} added successfully.")

# Function to verify login
def verify_login(email, password):
    if email in users:
        if bcrypt.check_password_hash(users[email], password):
            return True
        else:
            return False
    else:
        return False

# Now call the function to add users
add_user("anil@gmail.com", "a123")
add_user("bob@example.com", "bobpassword")
add_user("charlie@example.com", "charliepassword")
add_user("david@example.com", "davidpassword")

# Example usage of login verification
email_to_check = "anil@gmail.com"
password_to_check = "a123"

if verify_login(email_to_check, password_to_check):
    print("Login successful!")
else:
    print("Invalid email or password.")



@app.route('/')
def home():
    return redirect(url_for('product_list'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user_password = users.get(email)

        if user_password and bcrypt.check_password_hash(user_password, password):
            session['email'] = email
            return redirect(url_for('product_list'))
        else:
            flash('Invalid email or password', 'danger')
    
    return render_template('login.html')
@app.route('/logout')
def logout():
    session.pop('email', None)
    flash('You have been logged out', 'info')
    return redirect(url_for('login'))


@app.route('/products')
def product_list():
    if 'email' not in session:
        return redirect(url_for('login'))

    return render_template('product_list.html', products=products)


@app.route('/checkout', methods=['GET', 'POST'])
def checkout():
    if 'email' not in session:
        return redirect(url_for('login'))

    if request.method == 'POST':
        flash('Payment successful! Thank you for your purchase.', 'success')
        return redirect(url_for('product_list'))

    return render_template('checkout.html', products=products)

@app.route('/profile')
def profile():
    if 'email' not in session:
        return redirect(url_for('login'))
    return render_template('profile.html')

@app.route('/payment', methods=['GET', 'POST'])
def payment():
    if request.method == 'POST':
        # Simulate processing the payment
        flash('Payment Successful!')  # Flash the success message
        return redirect(url_for('product_list'))  # Redirect to product_list
    return render_template('payment.html')

if __name__ == '__main__':
    app.run(debug=True)
