import spbdl
import requests

url = spbdl.randImg()
url2 = spbdl.getImg("epic") #Uses the default arguments for getting image url
url3 = spbdl.getImg("epic",sort='top', order='created_at',direction="ASC") #Passes custom arguments for getting image url

print(url)
print(url2)
print(url3)