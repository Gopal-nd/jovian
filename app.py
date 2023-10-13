from flask import Flask,render_template,jsonify

app = Flask(__name__)

JOBS = [
  {
    'id':1,
    'title':'Python developer',
    'location':'bengaluru ,India',
    'salary':'Rs.12,00,000'
  },
  {
    'id':2,
    'title':'Web developer',
    'location':'delhi ,India',
    'salary':'Rs.14,00,000'
  },
  {
    'id':3,
    'title':'Game developer',
    'location':'mumbai,India',
    'salary':'Rs.15,00,000'
  },
  {
    'id':4,
    'title':'Block chain developer',
    'location':'USA',
    'salary':'$120,000'
    
  }

]
@app.route("/")
def hello_world():
  return render_template('home.html',jobs=JOBS)

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)
if __name__ == "__main__":
  app.run(host='0.0.0.0',debug=True)