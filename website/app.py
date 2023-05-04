from flask import Flask, render_template

import urllib.request, json

app = Flask(__name__)


@app.route('/')
def home_nishitha():
    return render_template('home_nishitha.html')

@app.route('/about')
def about_nishitha():
    return render_template('about_nishitha.html')

@app.route('/tracking')
def tracking_nishitha():
    return render_template('tracking_nishitha.html')

@app.route('/feature')
def feature_nishitha():
    return render_template('feature_nishitha.html')

@app.route('/login')
def login_nishitha():
    return render_template('login_nishitha.html')

@app.route('/dashboard')
def dashboard_nishitha():
    url = "http://www.qts.iitkgp.ac.in/last/1/10"
    response = urllib.request.urlopen(url)
    data = response.read()
    data = json.loads(data)
    #print(dict)

    url1 = "http://www.qts.iitkgp.ac.in/last/1/3600"
    response1 = urllib.request.urlopen(url1)
    data1 = response1.read()
    data1 = json.loads(data1)

    url2 = "http://www.qts.iitkgp.ac.in/last/2/3600"
    response2 = urllib.request.urlopen(url2)
    data2 = response2.read()
    data2 = json.loads(data2)

    url3 = "http://www.qts.iitkgp.ac.in/last/3/3600"
    response3 = urllib.request.urlopen(url3)
    data3 = response3.read()
    data3 = json.loads(data3)

    return render_template('dashboard_nishitha.html',data= json.dumps(data),data1=json.dumps(data1),data2=json.dumps(data2),data3=json.dumps(data3))

@app.route('/contact')
def contact_nishitha():
    return render_template('contact_nishitha.html')


if __name__ == '__main__':
    app.run(port = 5003)