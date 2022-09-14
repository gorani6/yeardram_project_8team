# can be used as a blueprint
from . import app
from flask import render_template, request
import pandas as pd
import csv

@app.route("/test-page")
def test_page():
    return "this is test page with sample_page.py"

@app.route("/corona", methods=['GET', 'POST'])
def corona_data():
    if request.method == 'POST':
        data = []
        with open('../corona_daily_data.csv', 'r') as csvfile:
            reader = csv.reader(csvfile)
            for r in reader:
                data.append([r[1], r[3]]) # date and count
            
            df = pd.DataFrame(data[1:], columns=['date', 'cnt'])

            df['date'] = df['date'].apply(lambda x: pd.to_datetime(str(x), format='%Y-%m-%d'))
            df.set_index(df['date'], inplace=True)
            df = df.drop(columns='date')
            df['cnt'] = pd.to_numeric(df['cnt'], downcast="integer")

            df['cnt'] = (df.cnt - df.cnt.shift(-1)).fillna(0)
            df['cnt'] = pd.to_numeric(df['cnt'], downcast="integer")
              
        option = request.form.get('period')
        print(option)
        if option == 'monthly':
            temp_data = df['cnt'].resample('M').sum()[:-1].astype(int)
        elif option == 'weekly':
            temp_data = df['cnt'].resample('W-Mon').sum()[:-1].astype(int)
        else:
            temp_data = df['cnt'].resample('D').sum()[:-1].astype(int)
    
        res = []
        for date, cnt in temp_data.items():
            res.append( [str(date)[:10], cnt] )
    
        return render_template('corona.html', res=res)
    else:
        return render_template('corona.html')