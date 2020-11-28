import re
from bs4 import BeautifulSoup
#from os import path
import os
  
#print(a)

def conversion(data):
    p=re.compile('<td.*>+<span.*"displayLabel">')
    
    a=p.sub('<div class="col-sm-4"><label class="col-sm-4 control-label">',data) 

    b=a.replace('</td>', '</label></div>')
    c=b.replace("<%", "&lt;%")
    d=c.replace("%>", "%&gt;")
    e=d.replace("displayButton", "btn btn-primary pull-right")
    soup = BeautifulSoup(e)
   # selects = soup.findAll('script')
    #for match in selects:
     #   match.decompose()
        
    for elem in soup.find_all(['span','table','p']):
        elem.unwrap()
    
   

    
    while True: 
        h2 = soup.find('tr')
        if not h2:
            break
        h2.name = 'div'
        h2['class'] ='form-group'
        
    
    

        
    while True: 
        h2 = soup.find('spring:message')
        if not h2:
            break
        h2.name = 'c:set'
        h2.value= 'HEADER.GENMAS.TITLE'
        h2.var= 'pagetitle'
        h2.scope='page'
 
    while True: 
        h2 = soup.find('bean:message')
        if not h2:
            break
        h2.name = 'spring:message'  
       
        del h2['bundle']
      
       
  
        
    while True: 
        h2 = soup.find('td')
        if not h2:
            break
        h2.name = 'div'
        h2['class'] ='col-sm-4'
        del h2['width']
        
    
    while True: 
        h2 = soup.find('select')
        if not h2:
            break
        h2.name = 'Select'
        h2['class'] ='form-control input-sm select'   
        
        
        
    while True: 
        h2 = soup.find('input')
        if not h2:
            break
        h2.name = 'Input'
        h2['class'] ='form-control input-sm'   
      
        
    while True: 
        h2 = soup.find('form')
        if not h2:
            break
        h2.name = 'Form'
        h2['class'] ='form-horizontal'
                    
       
      
    
    return str(soup.prettify(formatter=None))

if __name__ == "__main__":
   Path = str(r"C:\Users\ankus\Desktop\PDCStock")
   path2= str(r"C:\Users\ankus\Desktop\a")
   filelist = os.listdir(Path)
   print(filelist)

   for fname in filelist:
     
      with open( os.path.join( Path, fname ) ,"r") as fd:
          f = open(os.path.join( path2, fname ), "w")
          data=""
          for line in fd:
            data+=line
            #f.write(conversion(line))
         # print(data)
          f.write(conversion(data))
  
   f.close() 
   fd.close()
    
    