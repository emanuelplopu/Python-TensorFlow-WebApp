from flask import Flask
# Import flask 

# Pass in __name__ to help flask determine root path
app = Flask(__name__)

# Routing/Mapping
# @ signifies a decorator which is a way to wrap a function and modify its behaviour
@app.route("/") # Connect to webpage. "/" is a root directory
def main():
    return "Hello World!"

 
if __name__ == "__main__":
    app.run() # Start the web server