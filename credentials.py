file = open('/root/.aws/credentials','r')
data = file.read().split()
file.close()
key_id = data[3]
secret_access = data[6]
region = 'us-east-2'
