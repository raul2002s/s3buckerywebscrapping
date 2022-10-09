import boto3
from botocore import config
import os

#obteniendo la lista de los objetos de los buckets de s3 en AWS 



file = open('/root/.aws/credentials','r')
data = file.read().split()
file.close()
key_id = data[3]
secret_access = data[6]
region = 'us-east-2'

#forma 1

#session = boto3.Session(key_id, secret_access,region_name=region)

#s3 = session.resource('s3')
#objects = s3.Bucket('raulys3bucket').objects.all()
#print(f"{objects}")

#for obj in objects:
#    print(f" Item: {obj.key}")

#exit()

#forma 2

s3 = boto3.resource(service_name='s3', aws_access_key_id=key_id, aws_secret_access_key=secret_access, region_name=region)
objectsSum = s3.Bucket('raulys3bucket').objects.all()
for objsum in objectsSum:
    print(f"Item: {objsum.key}")

exit()


#forma 3

resource = boto3.resource(service_name='s3', region_name=region,
                          aws_access_key_id=key_id, 
                          aws_secret_access_key = secret_access,
                          )
 #config = config(signature_version='s3v4')
objectsSumary = resource.Bucket('cf-templates-1mcxr0f06y0sz-us-east-2').objects.all()

for objectsum in objectsSumary:
    print(f"Item: {objectsum.key}")

exit(0)

