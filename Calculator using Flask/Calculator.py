from flask import Flask, request, render_template,jsonify

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def showpage():
    return render_template('home.html')

@app.route('/maths',methods=['POST'])
def math_operation():
    if(request.method == 'POST'):
        operation = request.form['operation']
        num1 = int(request.form['num1'])
        num2 = int(request.form['num2'])
        if(operation == 'add'):
            r = num1+num2
            result = 'The sum is '+str(r)
        if(operation=='subtract'):
            r = num1-num2
            result = 'The subtraction is '+str(r)
        if(operation=='Multiplication'):
            r = num1*num2
            result = 'The Multiplication is '+str(r)
        if(operation=='Division'):
            r = num1/num2
            result = 'The Division is '+str(r)
    return render_template('result.html',result = result)

if __name__ == '__main__':
    app.run()