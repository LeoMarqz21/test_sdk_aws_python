import boto3
from io import StringIO 
import json 

#las credenciales las registran en la CLI o ver esto: 
# https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html

s3 = boto3.client('s3')
response = s3.list_buckets()

counter = 1

print('Buckets existentes:')
for bucket in response['Buckets']:
    print(f'#-{counter} Nombre de bucket: {bucket["Name"]}')
    counter += 1

iam = boto3.client('iam')
data = iam.get_user(UserName="leomarqz")
user = data['User']['UserName']

print(user)

