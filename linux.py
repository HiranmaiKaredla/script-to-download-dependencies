import json
import subprocess

k=[]
with open('lib.txt') as jsonfile:
  data= json.load(jsonfile)
  for p in data["Dependencies"]:
    k.append(p)
    subprocess.Popen(["pip","install",p],stdout=subprocess.PIPE,universal_newlines=True)


w=subprocess.Popen(["pip","list"],stdout=subprocess.PIPE,universal_newlines=True)

out=w.communicate()

u=out.split("\n")
u=u[2:]
v=[]

for i in u:
  x=[]
  t=i.split(" ")
  for j in t:
   
    if j!='':
      x.append(j)
      
 
  
  v.append("==".join(x))


failed=[]
for i in k:
  if i not in v:
    failed.append(i)
  
    
if len(failed)==0:
  print("success")
else:
  print("failed to download :")
  for j in failed:
    print(j)

