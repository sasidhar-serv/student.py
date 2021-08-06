from flask import Flask, render_template, request
app = Flask(__name__)
@app.route('/')
def student():
    return render_template('index.html')
@app.route('/result',methods = ['POST', 'GET'])
def result():
    if request.method == 'POST':
        result = request.form
        print(result)
        print(result["Name"])
        print(result["Physics"])
        print(result["Chemistry"])
        print(result["Mathematics"])
        p = int(result["Physics"])
        c = int(result["Chemistry"])
        m = int(result["Mathematics"])
        result1 = result.copy()
        result1["Total"] = p + c + m
        print(result1)
        return render_template("result.html",result = result1)
if __name__ == '__main__':
    app.run(debug = True)
