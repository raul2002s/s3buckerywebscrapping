import boto3
from botocore import exceptions
import credentials

def main():
    key_id = credentials.key_id
    secret_access = credentials.secret_access
    region = credentials.region
    bucket_name = "raulys3bucket"
    file_name = 'c6ce8fa8b5a97dd022ecd006536eb5a4'

    s3_client = boto3.client('s3',aws_access_key_id=key_id, aws_secret_access_key=secret_access, region_name=region)
    s3_client.download_file(bucket_name, Key=file_name,Filename='downloadedfile')
    print("objeto descargado con exito")
    exit(0)
if __name__ == "__main__":
    try:
        main()
    except ConnectionRefusedError:
        print("no se pudo concentar")    
    except exceptions.ClientError:
        print("objeto no encontrado")    
    except KeyboardInterrupt:
        print("\n saliendo")    