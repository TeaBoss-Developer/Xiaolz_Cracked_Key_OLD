from datetime import datetime
from flask import *
import os
import requests
from Method import Method
import random
list1 = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","1","2","3","4","5","6","7","8","9","0","@","!","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
se = requests.session()
app = Flask(__name__)
debug = False
@app.route("/", methods=["GET"])
def home():
    if __name__ == "__main__":
        global debug
        mode = request.args.get("mode",default="read")
        d_k = request.args.get("dk",default="")
        apikey = request.args.get('apikey',default="")
        count = request.args.get('count',default="1")
        qq = request.args.get('qq',default="1000110001")
        if(mode == "getkey"):
            if(debug):
                return(Get_Key())
            else:
                return("11586625323")
        if(mode == "add_key"):
            if(d_k == Get_Key()):
                bufkey = Get_Apikey()
                Write_File(Method.RunPath()+"\\Key\\"+bufkey+".txt",count)
                return jsonify({"code":"200","apikey":bufkey,"remain":count})
            else:
                return jsonify({"code":"500","msg":"You do not have permission to operate the database"})
        if(mode == "read_key"):
            ak = apikey
            bufcount = Get_File(Method.RunPath()+"\\Key\\"+apikey+".txt")
            bufrec = str(int(bufcount)-1)
            if(int(bufrec)<0):
                return jsonify({"code":"500","msg":"The Apikey not have enrough remain"})
            Write_File(Method.RunPath()+"\\Key\\"+ak+".txt",bufrec)
            return jsonify({"code":"200","apikey":ak,"remain":bufrec,"Pojie_Key":Get_Pojiekey(int(qq))})
def Write_File(file_path,text):
    e = open(file_path,'w')
    e.write(text)
    e.close()
def Get_Key():
    array_datetime = str(datetime.now()).split(" ")[0].split("-");
    return(str(int(array_datetime[0])*1.5).replace('.0','')+str(int(array_datetime[1])*5)+str(int(array_datetime[2])*8)+str(int(gethour())*4))
def Get_File(file_path):
    files = open(file_path,'r')
    m = files.read()
    files.close()
    return(m)
def Get_Apikey():
    b = ""
    a = 0
    i = 1;
    while i<=5:
        a=0
        while a <=5:
            rad = random.choice(list1)
            a += 1
            b += rad
        if(i<5):
            b+="-"
        i+=1
    return(b)
def Get_Pojiekey(qq):
    a =str(hex(qq))
    buf = a[2:10]
    result =  a[8:10]+a[6:8]+a[4:6]+a[2:4]
    return(str.upper('04'+result+result+'0400'+result+'000F'))
def gethour():
    a = str(datetime.now())
    return(a[11:13])
if __name__ == "__main__":
    app.run(host="0.0.0.0", port="2117")
