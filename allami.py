
import boto3


#list all ami and filter for ubuntu

def List_Ami():
    client = boto3.client('ec2')
    response = client.describe_images(Filters=
    [
            {
                'Name': 'name',
                'Values': [
                    '*Ubuntu*'
                          ]
            }
    ],                                )
    return response

