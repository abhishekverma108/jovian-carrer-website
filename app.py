from flask import Flask, render_template,jsonify
app=Flask(__name__)
JOBS=[
  {
    "id" :1,
    "title":"data analyst",
    "location": "banglore",
    "salary": "Rs 5,00,000"
  },
  {
    "id" :2,
    "title":"data scientist",
    "location": "Delhi,India",
    "salary": "Rs 8,00,000"
  },
  {
    "id" :3,
    "title":"sde",
    "location": "pune",
    "salary": "Rs 9,00,000"
  },
  {
    "id" :4,
    "title":"frontend",
    "location": "remote",
    
  }
]
@app.route("/")
def hello_world():
  return render_template("home.html",jobs=JOBS)

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)



if __name__=="__main__":
  app.run(host="0.0.0.0",debug=True)