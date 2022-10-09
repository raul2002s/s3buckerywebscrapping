import sys
import re

def main():
    web_file = open("webscrapping/web.html","rb")
    
    inicio = "<li>"
    fin = "</li>"

    inicio_title = "<title>"
    fin_title = "</title>"
    for line in web_file.readlines():
        #print(f"line:{line}")
        line = str(line)

        if inicio in line:
            #print(f"line:{line}")
            x = line.find(inicio)
            x = x + len(inicio)
            y = line.find(fin)
            line_content = line[x:y]
            print(f"li tag  line content: {line_content}")

        if inicio_title in line:
            x = line.find(inicio_title)
            x = x + len(inicio_title)
            y = line.find(fin_title)
            print(f"wesite title: {line[x:y]}")
    
    
    web_file.close()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()                