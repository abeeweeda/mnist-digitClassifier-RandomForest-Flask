from flask import Flask , request, render_template
import digit_class_using_pickle

app = Flask(__name__)
app.debug = True

@app.route('/', methods=['POST', 'GET'])
def home():
	if request.method == 'GET':
		img = digit_class_using_pickle.processImage('digit.jpg')
		print(digit_class_using_pickle.estimator.predict(img))
		predicted = digit_class_using_pickle.estimator.predict(img)[0]
		return render_template('digit_class.html', digit=predicted)
    
		
		
#for running the application from this file only
if __name__ == '__main__':
    app.run(debug=True)