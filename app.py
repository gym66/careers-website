from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS =[ {

  'id':1,
  'title':'Python Developer',
  'location':'New York',
  'salary':100000,
  'company':'Google'
}
,
 {
   'id':2,
   'title':'Data Scientist',
   'location':'India',
   'salary':190000,
   'company':'Google'
 }
,
{
  'id':3,
  'title':'Frontend Engineer',
  'location':'Remote',
  
  'company':'Google'
}
,
{
  'id':4,
  'title':'Backend Engineer',
  'location':'Remote',
  'salary':150000,
  'company':'Google'
}

]
@app.route("/")
def Hello_world():
  return render_template('home.html',
                        jobs=JOBS,
                        company_name='Carrers')
@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
