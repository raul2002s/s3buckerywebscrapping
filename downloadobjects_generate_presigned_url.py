from ast import parse
import boto3
from botocore import exceptions
import credentials
import argparse #generar una version mas avanzada para descargar una lista de files
import requests


def main():
    
    key_id = credentials.key_id
    secret_access = credentials.secret_access
    region = credentials.region
    bucket_name = 'raulys3bucket'
    file_name = 'c6ce8fa8b5a97dd022ecd006536eb5a4'
    
    
    s3_client = boto3.client('s3',aws_access_key_id=key_id, aws_secret_access_key= secret_access, region_name=region)
    url = s3_client.generate_presigned_url('get_object',Params={'Bucket': bucket_name, 'Key': file_name})
    
    #response = requests.get(url=url) ---> descarga el objeto o file pero no encuentro la ubicacion
    #print(f"se ha descargado el archivo exitosamente: {response}")
    
    print(f"try to open this url on your browser to download the file \n {url}")
if __name__ == "__main__":
    try:
        main()
    except exceptions.ClientError as e:
        if e.response['Error']['Code'] == "404":
            print("\n no se encontro el objeto")
    except ConnectionRefusedError:
        print("\n no se pudo conectar")
    except KeyboardInterrupt:
        print("\n saliendo")