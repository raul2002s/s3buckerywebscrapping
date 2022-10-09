import boto3
import credentials # importando desde el modulo credentials

region = credentials.region
access_key = credentials.key_id
secret_access = credentials.secret_access

session = boto3.Session(aws_access_key_id=access_key,
                        aws_secret_access_key= secret_access,
                        region_name=region)
data_crential = open('./credentials.py','rb').read()
data_list = open('./listobjects_s3buckets.py').read()
#esto sube un fichero dentro del objeto especificado dentro de un bucket de manera simple pero no me deja crear una carpeta dentro del objeto
#session.resource('s3').Bucket('raulys3bucket').Object('c6ce8fa8b5a97dd022ecd006536eb5a4').upload_file('./credentials.py')

#esto crea un objeto con el nombre personalizado dentro de un bucket s3 y pone el contenido de un fichero dentro y ademas en el Key se puede 
#pasar un path: folder/filedeseado y se crea una carpeta automaticamente dentro del objeto y luego subir mas files a esa misma carpeta.

session.resource('s3').Bucket('raulys3bucket').put_object(Key='myproject/credential.py', Body=data_crential)
session.resource('s3').Bucket('raulys3bucket').put_object(Key='myproject/listobjects_s3buckets.py', Body=data_list)
session.resource('s3').Bucket('raulys3bucket').put_object(Key='myproject/uploadfiles_s3buckets.py', Body=data_list)

# revisar en mi s3 de aws pq no soporta el ACL='public-read' en el put_object de la linea de arriba

#esto me crea un objeto vacio dentro de un bucket s3
#session.resource('s3').Bucket('raulys3bucket').put_object(Key='mycustomobject', Body='')

#esto crea un bucket, en la funcion create hay q especificar las configs del bucket
#session.resource('s3').Bucket('raulyotherbucket').create()

#con esto subo de manera simple un file a un objeto en un bucket
#session.resource('s3').Bucket('raulys3bucket').Object('mycustomobject').upload_file('listobjects_s3buckets.py')



print("done")
exit()

