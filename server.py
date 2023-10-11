from flask import Flask
from flask import render_template, request, redirect
import os

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route('/pages/create', methods=['POST', 'GET'])
def create_page():
    if request.method == 'POST':
    	name = request.form.get('name')
    	file_path = "templates/generated_"+name+".html"
    	if os.path.exists(file_path):
    		os.remove(file_path)
    	f = open(file_path, "a")
    	f.truncate()
    	f.write(request.form.get('html'))
    	f.close()
    	return redirect("/pages/"+name)
    return render_template('generate_html_page.html')

@app.route("/pages/<page_name>")
def display_page(page_name):
    return render_template("generated_"+page_name+".html")

@app.route("/pages/<page_name>/update")
def update_page(page_name):
	f = open("templates/generated_"+page_name+".html", "r")
	content = f.read()
	f.close()
	return render_template("update_html_page.html", name=page_name, content=content)

@app.route("/video")
def video():
    return render_template('video.html')

if __name__ == '__main__':  
   app.run(debug=True)

