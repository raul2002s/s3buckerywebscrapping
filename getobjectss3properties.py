
import boto3
from botocore import exceptions
import credentials
import sys

def main():
    key_secret = credentials.secret_access
    key_access = credentials.key_id
    region = credentials.region
    s3_bucket_name = 'raulys3bucket'
    file_name = 'c6ce8fa8b5a97dd022ecd006536eb5a4'
    
 
    s3_resource = boto3.resource('s3', aws_access_key_id=key_access, 
                            aws_secret_access_key=key_secret, region_name=region)

    bucket_object = s3_resource.Object(bucket_name=s3_bucket_name, key=file_name )

    print(f"bucket name: {bucket_object.bucket_name}")
    print(f"file name: {bucket_object.key}")
    print(f"type: {bucket_object.content_type}")
    print(f"size: {bucket_object.content_length}")
    print(f"updated at: {bucket_object.last_modified}")
    print(f"metadata: {bucket_object.metadata}")
    print(f"access control list: {s3_resource.ObjectAcl(bucket_name=s3_bucket_name,object_key=file_name).grants}")


    sys.exit(0)
    
if __name__ == '__main__':
    try: 
        main()
    except ConnectionRefusedError:
        print("\n no se pudo concectar al servicio")
    except exceptions.ClientError:
        print("\n no se encontro el objeto")
    except KeyboardInterrupt :
        print("\n saliendo")
