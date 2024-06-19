from flask import Flask,jsonify,json
import mysql.connector
from config import db_config
import pandas as pd
from query import query 
# make a config file(seperate file) and then fetch the data from there(jSON FILE)


app = Flask(__name__)

@app.route('/')
def status():
    return "Hi this API is working "

@app.route('/getdata')
def get_json_data():
    with open('student-data.json', 'r') as file:
        data = json.load(file)
        #print(data)
        return "Json data fetched successfully"
    

@app.route('/sql')
def fetching():
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        cursor.execute(query)
        results = cursor.fetchall()
        final_results = pd.DataFrame(results,columns = ['student_id','student_name','age',
                                                        'gender','phone'])
        print(final_results)

        return 'fetched data successful'
        
    except mysql.connector.errors.ProgrammingError:
        return 'Error in connection or query'

    except Exception as e:
        return e
    
    finally:
        cursor.close()
        conn.close()
        
        
if __name__ == "__main__":
    app.run(debug = True)

