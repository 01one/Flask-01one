from flask import Flask,render_template
app=Flask(__name__)

@app.route('/')
def hello_wolrd():
	title="Where nature says nothing but we interprete 'nothing'"
	return render_template('index.html',title=title)
if __name__=='__main__':
	app.run(debug=True)




