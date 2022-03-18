from flask import Flask, render_template, request
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.sql import text
import psycopg2


DB_URL = 'postgresql://hszfokpundaypl:11b4974e310360624e2b63af69ca2e97190c156b48b0dffdc419ba15a6cc66e3@ec2-54-162-211-113.compute-1.amazonaws.com:5432/dda5k4khgrltai'
engine = create_engine(DB_URL)
con = engine.connect()

app = Flask(__name__)

def template(title = "HELLO!", text = ""):
    templateDate = {
        'text' : text,
        'tvalues' : getTValues(),
        'selected_tvalue' : 'Choose a Jack',
    }
    return templateDate

def getTValues():
    return ('Ankin', 'Sandeep')

@app.route('/', methods=['POST', 'GET'])
def home_page():
    # return '<h1>Jackkks GYM </h1>'
    tvalue = ''
    nvalue = request.form.get('mytitle')
    print(nvalue)
    if request.method == "POST":            
        tvalue = request.form['tvalue']

    v_name = tvalue
    p_id_name = con.execute("""SELECT id from wk_people where name = '{}'""".format(v_name))

    p_name = p_id_name.fetchall()
    
    try:
        p_id = p_name[0][0]
    except IndexError:
        p_id = 3
    statement = ("""SELECT date,day,exercise,sets,reps,weights,name from wk_data INNER JOIN wk_people on wk_data.person_id = wk_people.id
    where person_id = {}""")
    sc = con.execute(statement.format(p_id))

    sct = pd.DataFrame(sc.fetchall(), columns=['Date','Day','Exercise','Sets','Reps','Weights','Person'])

    #generating template data
    print(tvalue)
    templateData = template(text = tvalue)
    templateData['selected_tvalue'] = tvalue
    # return render_template('dashboard.html')
    # return render_template('dashboard.html', **templateData, tables=[sct.to_html(classes='data')], titles=sct.columns.values)
    return render_template('dashboard.html', **templateData, tables=sct.values.tolist(), titles=sct.columns.values)
if __name__ == '__main__':
    app.run(debug=True)
