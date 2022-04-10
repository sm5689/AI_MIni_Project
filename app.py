from flask import Flask, render_template, request
import diet_recommendation_system as dr
app = Flask(__name__)

@app.route('/')
def index():
    title = 'Diet Recommendation System'
    return render_template('index.html', title = title)


@app.route('/results', methods = ["POST", "GET"])
def results():
    title = 'Diet Recommendation System'
    age = request.form.get("age")
    weight = request.form.get("weight")
    height = request.form.get("height")
    func = request.form.get('func')
    print(age)
    print(weight)
    print(height)
    print(func)
    bmi = float(weight)/((float(height)/100)**2)
    bmi = round(bmi, 2)
    if func == 'wloss':
        print('Weight Loss')
        res = dr.Weight_Loss(bmi)
        print(res)
        func = 'Weight Loss'
    elif func == 'wgain':
        print('Weight Gain')
        res = dr.Weight_Gain(bmi)
        print(res)
        func = 'Weight Gain'
    elif func == 'main':
        print('Maintain')
        res = dr.Healthy(bmi)
        print(res)
        func = 'Maintaining your Weight'
    else:
        print('Nothin lmao')
        print(func)
    return render_template(
        "results.html",
        res=res,
        age=age,
        bmi=bmi,
        func=func
    )

if __name__ == '__main__':
    app.run(debug=True)

