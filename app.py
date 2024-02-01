from flask import Flask,render_template,request,jsonify

app = Flask(__name__)

@app.route('/', methods=['POST','GET'])
def hello_world():
    bmi=float()
    weight=int()
    height=int()
    if request.method == 'POST' and 'weight'  in request.form:
        weight = int(request.form.get('weight'))
        height = int(request.form.get('height'))
        bmi = calc_bmi(weight,height)
        return render_template('result.html',bmi=bmi)
    else:
        return render_template('index.html',bmi=bmi)
    
        
def calc_bmi(weight,height):
    x = round(weight/((height/100)**2),2)
    return x 
@app.errorhandler(Exception)
def value_error(e):
    return jsonify({'msg': 'Please enter any value'}), 304

if __name__ == '__main__':
    app.run(debug=True)
