from flask import Flask, request, jsonify
import pickle

app = Flask(__name__)

clf_svm = pickle.load(open('clf.pkl','rb'))
tfidf = pickle.load(open('tfidf.pkl','rb'))

@app.route('/predict', methods=['POST'])
def predict():

    data = request.get_json()
    text = data["text"]

    vector = tfidf.transform([text])
    result = clf_svm.predict(vector)

    if result == 1:
        prediction = "AI-generated"
    else:
        prediction = "Human-written"

    return jsonify({
        "input_text": text,
        "prediction": prediction
    })

if __name__ == "__main__":
    app.run(debug=True)