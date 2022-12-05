import socket
import os
import configparser
import requests

class Method:
    def ReadIni(config_path,section,Param,value=""):#读配置项
        conf = configparser.ConfigParser()
        try:
            conf.read(config_path)
        except:
            return("发现问题,配置文件中拥有两个相同的配置节.")
        try:
            return(conf.get(section,Param))
        except:
            return("")
    def WriteIni(config_path,section,Param,value):#写配置项
        conf = configparser.ConfigParser()
        conf.read(config_path)
        try:
            conf.set(section,Param,value)
        except:
            conf.add_section(section)
            conf.set(section,Param,value)
        conf.write(open(config_path,'w+'))
        return(config_path+"  "+section+"  "+Param+"  "+value)
    def RunPath():#取运行目录
        proDir = os.path.split(os.path.realpath(__file__))[0]
        return(proDir)
    def Socket(IP,Port,msg):
        ADDR = (IP,int(Port))
        tcpCliSock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        tcpCliSock.connect(ADDR)
        tcpCliSock.sendall(msg.encode('utf-8'))
        data1 = tcpCliSock.recv(1024)
        tcpCliSock.close()
        return(data1.decode('utf-8'))
    def download_web(url,save_path):
        r = requests.get(url,allow_redirects=True)
        f = open(save_path,'wb')
        f.write(r.content)
        f.close()
        return(save_path)
    def read_web(url):
        return(requests.get(url).text)
    def post_web(url):
        return(requests.post(url).text)
class 方法:
    def 读配置项(config_path,section,Param,value=""):#读配置项
        conf = configparser.ConfigParser()
        try:
            conf.read(config_path)
        except:
            return("发现问题,配置文件中拥有两个相同的配置节.")
        return(conf.get(section,Param))
    def 写配置项(config_path,section,Param,value):#写配置项
        conf = configparser.ConfigParser()
        conf.read(config_path)
        try:
            conf.set(section,Param,value)
        except:
            conf.add_section(section)
            conf.set(section,Param,value)
        conf.write(open(config_path,'w+'))
        return(config_path+"  "+section+"  "+Param+"  "+value)
    def 取运行目录():#取运行目录
        proDir = os.path.split(os.path.realpath(__file__))[0]
        return(proDir)