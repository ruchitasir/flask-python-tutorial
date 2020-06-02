# YOUR FLASK APP HERE
from flask import Flask, render_template, request
from pymongo import MongoClient
import pprint

app = Flask(__name__)
app.config['DEBUG'] = True

client = MongoClient()

db = client.flask_database



# query for several loops
# print("Finding all blog posts:")
# for loop in loops.find():
#   pprint.pprint(loop)
# print()

@app.route("/")
def home():
  return render_template('index.html')

@app.route("/loops")
def loops_home():
    retrieved_loops= db.loops.find()
 
    return render_template('loops.html',retrieved_loops= retrieved_loops)  

@app.route("/operators", methods = ['POST', 'GET'])  
def operators_home():  
    retrived_operators = db.operators.find()
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        symbol = request.form['symbol']
        example = request.form['example']
        uses = request.form['uses']
        print('req.form',request.form)
        oper={
            'name':name,
            'description':description,
            'symbol': symbol,
            'example': example,
            'uses':uses
        }
        db.operators.insert_one(oper).inserted_id
    return render_template('operators.html',retrived_operators= retrived_operators)          




if __name__ == "__main__":
  app.run()