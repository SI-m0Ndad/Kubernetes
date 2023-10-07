from flask import Flask

# Create a Flask web application instance
app = Flask(__name__)

# Define a route for the root URL ("/")
@app.route("/")
def hello():
    return "Hello, World!"

# Define a custom route ("/about")
@app.route("/about")
def about():
    return "This is a simple Flask app."

# Run the Flask application if this script is executed directly
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=50000)
