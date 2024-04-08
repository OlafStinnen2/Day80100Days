from flask import Flask, request

# Create a dictionary with user information
Users = {
    1: {
        "Name": "Olaf",
        "Password": "123"
    },
    2: {
        "Name": "Susi",
        "Password": "Hasi"
    },
    3: {
        "Name": "Heiner",
        "Password": "Depp"
    }
}

app = Flask(__name__)

@app.route("/process", methods=["POST"])
def process():
    page = ""
    form = request.form

    page = "Incorrect username or password. Please try again."
    for i in range(1, 4):
        if form['username'] == Users[i]["Name"] and form['password'] == Users[i]["Password"]:
            page = f"Welcome back, {form['username']}!"
            break

    return page

@app.route('/')
def index():
    page = """<form method = "post" action="/process">
    <p>Name: <input type="text" name="username" required> </p>
    <p>Password: <input type="Password" name="password"> </p>
    <button type="submit">Login</button>
    </form>"""
    
    return page

app.run(host='0.0.0.0', port=81)