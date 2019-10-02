#!/usr/bin/python3.6

import boto3
from botocore.exceptions import ClientError
import json

session = boto3.session.Session(profile_name='mehdir26aws')

s3 = session.resource('s3')

client = session.client('s3')



def lockdown_public_buckets_by_policy():

    for bucket in s3.buckets.all():
        try:
            bucket_policy = json.loads(client.get_bucket_policy(Bucket=bucket.name)['Policy'])
            principal = bucket_policy['Statement'][0]['Principal']
            effect = bucket_policy['Statement'][0]['Effect']
            if principal == '*' and effect == 'Allow':
                response = client.put_public_access_block(
                            Bucket= bucket.name,
                            PublicAccessBlockConfiguration={
                                'BlockPublicAcls': True,
                                'BlockPublicPolicy': True,
                                'RestrictPublicBuckets': True,
                                'IgnorePublicAcls': True
                                }
                             )
        except ClientError:
             pass


if __name__ == '__main__':
    lockdown_public_buckets_by_policy()


