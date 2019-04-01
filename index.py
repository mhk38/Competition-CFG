# Import requests
import requests

# Import Flask
from flask import Flask, render_template, request

app = Flask("MyApp")
# Load index.html
@app.route("/")
def hello():
    return render_template("index.html")

# Load Contact Us page
@app.route("/contact_us")
def contact_page():
    return render_template("contact_us.html")

# Post form when submit button is clicked
@app.route("/contact_us", methods=["POST"])
def contact_us():
    form_data = request.form
    print (form_data["email"])
    send_simple_message()
    return hello()

# To Cathy: Modify contact_us function with the mailgun API.

def send_simple_message():
    form_data = request.form
    return requests.post(
		"https://api.mailgun.net/v3/sandboxfa96724b71f040c88fa450724763469b.mailgun.org/messages",
		auth=("api", "0f7face814c7c77bbb1535e843dbe29d-de7062c6-e7c48a8e"),
		data={"from": "Excited User <postmaster@sandboxfa96724b71f040c88fa450724763469b.mailgun.org>",
			"to": form_data["email"],
			"subject": "Helloooooooooooooooo",
			"text": "Testing some Mailgun awesomness!"})


# Run app if application is debugged
app.run(debug=True)
app.run(port = 5000)
