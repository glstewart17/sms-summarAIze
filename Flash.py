from flask import Flask, flash, redirect, render_template, request, session, url_for
from wikipedia_text import summarizer, train_markov, article_text

app = Flask(__name__)
app.secret_key = 'random string'


@app.route('/summary')
def summary():
   output = session['messages']  
   return render_template('summary.html', output=(output))

@app.route('/', methods = ['GET', 'POST'])
def handle():
   error = None
   
   if request.method == 'POST':
      length = request.form['length']
      topic = request.form['topic']
      try:
        length = int(length)
      except ValueError:
        length = None
      if length == None:
         error = 'Invalid topic or sentence length. Please try again!'
      else:
         flash('Succsessful Entry!')
         session['messages'] = summarizer(train_markov(article_text(topic)), length)
         return redirect(url_for('summary'))
			
   return render_template('handle.html', error = error)

if __name__ == "__main__":
   app.run(debug = True)