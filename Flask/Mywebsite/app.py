from flask import Flask, render_template, jsonify

#Object of the class Flask
app = Flask(__name__) 

JOBS = [
    {
        'id' : 1,
        'title' :'Data Scientist',
        'location' :'Delhi, India',
        'Salary' : 'Rs 15lpa'
    },
    {
        'id' : 2,
        'title' : 'Data Engineer',
        'location' : 'Mumbai, India',
        'Salary' : ''
    },
    {
        'id' : 3,
        'title' : 'SAP Developer',
        'location' : 'Bangalore, India',
        'Salary' : 'Rs 10lpa'
    }
]

@app.route("/")
def create_app():
    return render_template('home.html', jobs = JOBS, company_name ="Hello" )

@app.route("/api/jobs")
def list_jobs():
    return jsonify(JOBS)

#Make changes automatically
if __name__ =="__main__":
    app.run(debug=True)