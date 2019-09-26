#!/usr/bin/python3.6

import boto3

mehdir26aws = boto3.session.Session(profile_name='mehdir26aws')


ec2 = mehdir26aws.resource('ec2')

security_group_iterator = ec2.security_groups.filter(
        Filters=[
            {
                'Name': 'ip-permission.cidr',
                'Values': [ '0.0.0.0/0' ]
            },
            {
                'Name': 'ip-permission.to-port',
                'Values': [ '22' ]
            }, 
        ]
    )


for group in security_group_iterator:
    print(group.id)
    sg = ec2.SecurityGroup(group.id)
    sg.revoke_ingress(CidrIp='0.0.0.0/0', FromPort=22, IpProtocol='TCP', ToPort=22)


