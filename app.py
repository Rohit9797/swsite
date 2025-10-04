from flask import Flask, render_template, request, redirect, url_for, flash
import os
import csv

app = Flask(__name__)
app.secret_key = "yoursecretkey"

FILE_PATH = "subscribers.txt"

# make sure file exists
if not os.path.exists(FILE_PATH):
    with open(FILE_PATH, "w") as f:
        pass


# csv file path
CSV_FILE = "submissions.csv"

# Ensure CSV has headers if it doesn't exist
if not os.path.exists(CSV_FILE):
    with open(CSV_FILE, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Email", "Service", "Message"])



@app.route('/')
def index():
    return render_template('index.html')


@app.route('/service')
def service():
    return render_template('service.html')

@app.route('/price')
def price():
    return render_template('price.html')

@app.route('/product')
def product():
    return render_template('product.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/feature')
def feature():
    return render_template('feature.html')


@app.route('/career')
def career():
    return render_template('career.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route("/subscribe", methods=["POST"])
def subscribe():
    email = request.form.get("email")
    if email:
        # read existing emails
        with open(FILE_PATH, "r") as f:
            emails = f.read().splitlines()

        if email in emails:
            flash("⚠️ Email already subscribed.", "danger")
        else:
            # save new email
            with open(FILE_PATH, "a") as f:
                f.write(email + "\n")
            flash("✅ Thanks for subscribing!", "success")
    else:
        flash("⚠️ Please enter a valid email.", "danger")

    return redirect(request.referrer or url_for("index"))

@app.route("/submit_form", methods=["POST"])
def submit_form():
    name = request.form.get("name")
    email = request.form.get("email")
    service = request.form.get("service")
    message = request.form.get("message")

    # Save to CSV
    with open(CSV_FILE, mode="a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([name, email, service, message])

    return redirect(url_for("thank_you"))

@app.route("/thank_you")
def thank_you():
    return "<h2>Thank you! Your request has been submitted successfully.</h2>"

if __name__ == "__main__":
    app.run(debug=True)
