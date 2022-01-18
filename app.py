from flask import Flask, request, url_for, render_template
import pickle
import pandas as pd 
from flask_cors import CORS

app  = Flask(__name__)
CORS(app)

model = pickle.load(open("model.pk", "rb"))

@app.route('/')
def use_template():
    return render_template("index.html")


@app.route('/predict', methods=['POST', 'GET'])
def predict():
    input_one  = request.form.get('1',False)
    input_two  = request.form.get('2',False)
    input_three  = request.form.get('3',False)
    input_four  = request.form.get('4',False)
    input_five  = request.form.get('5',False)
    input_six  = request.form.get('6',False)
    input_seven  = request.form.get('7',False)
    input_eight  = request.form.get('8',False)

    setup_df = pd.DataFrame([pd.Series([input_one,input_two, input_three, input_four, input_five, input_six, input_seven, input_eight])])
    diabetes_prediction = model.predict_proba(setup_df)
    output = '{0:.{1}f}'.format(diabetes_prediction[0][1], 2)
    output = str(float(output)*100)+"%"
    if output>str(0.5):
        return render_template('index.html', pred=f'You have the following chance of having diabetes based on the given iput.\nProbability of having Diabetes is {output}')
    else:
        return render_template('index.html', pred=f'You have low chance of diabetes which is currently considered safe (this is only an example, please consult a certified doctor for further consultation or medical advice).\n Probability of having diabetes is {output}')


if __name__ == '__main__':
    app.run(debug=True)
