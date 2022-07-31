from flask import Flask , render_template , jsonify

app = Flask(__name__,template_folder='templates')

JOBS = [
  { 'id':1,
   'Title':'Data analyst',
   'location': 'Bengluru, India',
   'Salary': 'Rs 10,000,00'},
  { 'id':2,
   'Title':'Data scientist',
   'location': 'Mumbai, India',
   'Salary': 'Rs 18,000,00'},
  { 'id':3,
   'Title':'Data Engineer',
   'location': 'Bengluru, India',
   'Salary': 'Rs 22,000,00'},
  { 'id':4,
   'Title':'Software devops',
   'location': 'Bengluru, India'}
]

@app.route("/")
def hello():
    return render_template('home.html',jobs = JOBS)


@app.route("/api/jobs")
def job_list():
    return jsonify(JOBS)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug = True)

