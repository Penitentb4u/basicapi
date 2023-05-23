from flask import *
import json,time,socket   

app=Flask(__name__)
@app.route('/',methods=['GET'])
def home_page():
    data_set={'Page': 'Home' , 'Message':'Successful!!','Timestamp':time.time()}
    json_dump= json.dumps(data_set)
    return json_dump

@app.route('/user/',methods=['GET'])
def request_page():
    user_query=str(request.args.get('ip'))  #user/?ip=something  
    hostname=socket.gethostname()   
    IPAddr=socket.gethostbyname(hostname)   
    data_set={'Page': 'Amex' , 'Message':f'User said=  {user_query}  ','Host name is':f'{hostname}', 'IP address':f'{IPAddr} '}
    json_dump= json.dumps(data_set)
    return json_dump

if __name__== '__main__':
    app.run(port=8069)
