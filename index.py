# Import requests
import requests
import ssl

ssl._create_default_https_context = ssl._create_unverified_context
# Import Flask
from flask import Flask, render_template, request

app = Flask("MyApp")

# Load index.html
@app.route("/")
def hello():
    return render_template("index.html")

def getRecipeByIngredients(dish):
    payload = {
        'fillIngredients': False,
        'ingredients': dish,
        'limitLicense': False,
        #'number': 5,
        #'ranking': 1
    }

    api_key = "c7135f2f8bmsh9b6b78982ba931fp135282jsn85ad20e4d037"
    endpoint = "https://spoonacular-recipe-food-nutrition-v1.p.mashape.com/recipes/findByIngredients"
    headers={
        "X-Mashape-Key": "c7135f2f8bmsh9b6b78982ba931fp135282jsn85ad20e4d037",
    }
    r = requests.get(endpoint, params=payload, headers=headers)
    results = r.json()
    return results

# load recipe page
@app.route("/<dish>")
def recipe(dish):
    results = getRecipeByIngredients(dish)
    return render_template("recipe.html" , dish=dish.title(), results=results)

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
    return thanks_page()

# To Cathy: Modify contact_us function with the mailgun API.

def send_simple_message():
    form_data = request.form
    return requests.post(
		"https://api.mailgun.net/v3/sandboxfa96724b71f040c88fa450724763469b.mailgun.org/messages",
		auth=("api", "0f7face814c7c77bbb1535e843dbe29d-de7062c6-e7c48a8e"),
		data={"from": "Foodtopia <postmaster@sandboxfa96724b71f040c88fa450724763469b.mailgun.org>",
			"to": form_data["email"],
			"subject": "Contact us here",
			"text": "Hello new user, feel free to contact us on this email"})

@app.route("/thank_you")
def thanks_page():
    return render_template("ThankYou.html")

# Run app if application is debugged
app.run(debug=True)
app.run(port = 5000)
