# initial setup
import requests
import re

# create session
s=requests.Session()

# first request
data={'answer':"answer"}
data
r = s.post(url = "http://docker.hackthebox.eu:30184/flag", data=data)
r.text

# second request
r1=re.findall("(\d*\.\d*) ([\+\-\*/]) (\d*\.\d*)", r.text)
r1
expression=""
expression=expression.join(r1[0])
#answer=str(eval(expression))
answer=round(eval(expression),2)
data={"answer":answer}
data
r = s.post(url = "http://docker.hackthebox.eu:30184/flag", data=data)
r.text

# third request
r1=re.findall("(\d*\.\d*) ([\+\-\*/]) (\d*\.\d*)", r.text)
r1
expression=""
expression=expression.join(r1[0])
#answer=str(eval(expression))
#answer=eval(expression)
answer=round(eval(expression),2)
data={"answer":answer}
data
r = s.post(url = "http://docker.hackthebox.eu:30184/flag", data=data)
r.text

# fourth request
r1=re.findall("(\d*\.\d*) ([\+\-\*/]) (\d*\.\d*)", r.text)
r1
expression=""
expression=expression.join(r1[0])
#answer=str(eval(expression))
#answer=eval(expression)
answer=round(eval(expression),2)
data={"answer":answer}
data
r = s.post(url = "http://docker.hackthebox.eu:30184/flag", data=data)
r.text

# fifth request
r1=re.findall("(\d*\.\d*) ([\+\-\*/]) (\d*\.\d*)", r.text)
r1
expression=""
expression=expression.join(r1[0])
#answer=str(eval(expression))
#answer=eval(expression)
answer=round(eval(expression),2)
data={"answer":answer}
data
r = s.post(url = "http://docker.hackthebox.eu:30184/flag", data=data)
r.text

# sixth request
r1=re.findall("(\d*\.\d*) ([\+\-\*/]) (\d*\.\d*)", r.text)
r1
expression=""
expression=expression.join(r1[0])
#answer=str(eval(expression))
#answer=eval(expression)
answer=round(eval(expression),2)
data={"answer":answer}
data
r = s.post(url = "http://docker.hackthebox.eu:30184/flag", data=data)
r.text

# seventh request
r1=re.findall("(\d*\.\d*) ([\+\-\*/]) (\d*\.\d*)", r.text)
r1
expression=""
expression=expression.join(r1[0])
#answer=str(eval(expression))
#answer=eval(expression)
answer=round(eval(expression),2)
data={"answer":answer}
data
r = s.post(url = "http://docker.hackthebox.eu:30184/flag", data=data)
r.text

# eighth request
r1=re.findall("(\d*\.\d*) ([\+\-\*/]) (\d*\.\d*)", r.text)
r1
expression=""
expression=expression.join(r1[0])
#answer=str(eval(expression))
#answer=eval(expression)
answer=round(eval(expression),2)
data={"answer":answer}
data
r = s.post(url = "http://docker.hackthebox.eu:30184/flag", data=data)
r.text

# ninth request
r1=re.findall("(\d*\.\d*) ([\+\-\*/]) (\d*\.\d*)", r.text)
r1
expression=""
expression=expression.join(r1[0])
#answer=str(eval(expression))
#answer=eval(expression)
answer=round(eval(expression),2)
data={"answer":answer}
data
r = s.post(url = "http://docker.hackthebox.eu:30184/flag", data=data)
r.text

# tenth request
r1=re.findall("(\d*\.\d*) ([\+\-\*/]) (\d*\.\d*)", r.text)
r1
expression=""
expression=expression.join(r1[0])
#answer=str(eval(expression))
#answer=eval(expression)
answer=round(eval(expression),2)
data={"answer":answer}
data
r = s.post(url = "http://docker.hackthebox.eu:30184/flag", data=data)
r.text

# last time
data={"answer":"YES_I_CAN!"}
data
r = s.post(url = "http://docker.hackthebox.eu:30184/flag", data=data)
print(r.text)
