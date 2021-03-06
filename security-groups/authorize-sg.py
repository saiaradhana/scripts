#!/usr/bin/python 
__author__ = "unnisathya"

import argparse
import boto3


def main():
 parser = argparse.ArgumentParser()
 parser.add_argument("security_group",help="Example: sg-28f3ed4c")
 parser.add_argument("port_number",help="Example: 22")
 parser.add_argument("ip",help="Example: 192.168.1.1/32")
 parser.add_argument("region",help="Example: us-east-1")

 args = parser.parse_args()

 ec2 = boto3.resource('ec2', region_name=args.region)
 security_group = ec2.SecurityGroup(args.security_group)
 response = security_group.authorize_ingress(IpProtocol="tcp",FromPort=int(args.port_number),ToPort=int(args.port_number),CidrIp=args.ip)
 
 if response["ResponseMetadata"]["HTTPStatusCode"] == 200:
  print "Rule Added"
 else:
  print "Error Adding Rule"

 with open("IPList.txt",'a') as Tmpfile:
  Tmpfile.write(args.ip + '\n')

 

if __name__ == '__main__':

 main()

