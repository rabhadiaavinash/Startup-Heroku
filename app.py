from flask import Flask,render_template,request
import pickle
import numpy as np

app = Flask(__name__)

model = pickle.load(open("model.pkl","rb"))

@app.route("/")
def starting():
    return render_template("index.html")

@app.route("/predict",methods = ["POST"])
def predict():
    int_features = [x for x in request.form.values()]
    if int_features[-1] == "1":
          int_features.append("0")
    else:
          int_features.append("1")
    #final_features = np.array(int_features)
    final_features = [int_features]

    output = model.predict(final_features)
    output = round(output[0],2)
    #print("output : ",output)
    
    return render_template("index.html",prediction_text="Startup's Profit : $ {}".format(output))



if __name__=="__main__":
    app.run(debug=True)   


