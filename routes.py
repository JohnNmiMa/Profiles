import pdb
from flask import Flask, render_template
 
app = Flask(__name__)      
 
@app.route('/')
def github():
    #return render_template('index.html')
    print "At first route request"
    return render_template('github_portfolio.html')

@app.route('/GitHubPortfolio')
def github_portfolio():
    print "At GitHubPortfolio route request"
    return render_template('github_portfolio.html')

@app.route('/Experience')
def experience():
    print "At Experience route request"
    return render_template('experience.html')

@app.route('/Skills')
def skills():
    print "At Skills route request"
    return render_template('skills.html')

if __name__ == '__main__':
  app.run(debug=False)

