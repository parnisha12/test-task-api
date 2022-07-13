import boto3
from botocore.exceptions import ClientError

def get_service_list():
    client = boto3.client('resourcegroupstaggingapi', )
    regions = boto3.session.Session().get_available_regions('ec2')

    for region in regions:
        print(region)
        try:
            client = boto3.client('resourcegroupstaggingapi', region_name=region)
            servece_list = []
            for mappint_list in client.get_resources().get('ResourceTagMappingList'):
                servece_list.append(mappint_list.get('ResourceARN').split(':')[2])
            for service in list(set(servece_list)):
                print (str.upper(service))
        except ClientError as e:
            print('Could not connect to region')

def main():
    get_service_list()

if __name__ == "__main__":
    main()
    