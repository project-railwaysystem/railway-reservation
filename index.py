from flask import Flask
app = Flask(__name__)
 
# @app.route("/",method=['POST'])
# def hello():
#   return "Hello World!"
 
@app.route('/')
def index():
   return render_template('index.html')
 
if __name__ == "__main__":
  app.run()   