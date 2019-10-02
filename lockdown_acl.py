#!/usr/bin/python3.6

import boto3

session = boto3.session.Session(profile_name='mehdir26aws')

s3 = session.resource('s3')

client = session.client('s3')


def lockdown_public_buckets_by_acl():

    for bucket in s3.buckets.all():
        bucket_access = s3.BucketAcl(bucket.name).grants

        for i in range(0,len(bucket_access)):
            try:
                if bucket_access[i]['Grantee']['URI'] == 'http://acs.amazonaws.com/groups/global/AllUsers':
                    response = client.put_public_access_block(
                            Bucket= bucket.name,
                            PublicAccessBlockConfiguration={
                                'BlockPublicAcls': True,
                                'BlockPublicPolicy': True,
                                'RestrictPublicBuckets': True,
                                'IgnorePublicAcls': True
                                }
                            )
            except KeyError:
                pass


if __name__ == '__main__':
    lockdown_public_buckets_by_acl()

