
import sys
import urllib3

def main():
    web_file = open("webscrapping/web.html","a")
    web_file.close()
    web_file = open("webscrapping/web.html","wb")

    url = "https://lorem2.com"
    #req = urllib3.HTTPConnectionPool('jseocopywriter.com')
    #response = urllib3.HTTPResponse(request_method='GET',request_url=url)
    #req = urllib3.PoolManager()
    #response = req.request('GET',url)
    
    conn = urllib3.connection_from_url(url=url)
    response = conn.request(method='GET', url='/')
    response = response.data
    #response = req.urlopen(method="GET",url=url)
    web_file.write(response)
    #print(f"respuesta from {url}: \n {response}")


    
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()