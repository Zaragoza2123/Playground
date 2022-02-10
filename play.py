from flask import Flask, render_template
app = Flask(__name__)



@app.route('/play/<int:x>/<color>')
def threeBlueBoxes(x, color):
    return render_template('play.html', x=x, y=color)





if __name__=="__main__":
    app.run(debug=True)
