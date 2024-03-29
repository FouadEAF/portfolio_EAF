from flask import Flask, render_template#, request

app = Flask(__name__)

@app.route('/')
def index_page():
    return render_template('index.html')

@app.route('/myBlog')
def single_page():
    return render_template('single.html')

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=80)
