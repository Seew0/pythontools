#!/usr/bin/env python3

import argparse
import bcrypt

parser = argparse.ArgumentParser(description='Password Encryption Tool v1.0')

parser.add_argument('-v','--version',action='version',version='Password Encryption Tool v1.0')

parser.add_argument('passwd',type=str,help="The password to analyze")

args= parser.parse_args()

passwd= args.passwd

encode_passwd=passwd.encode('utf-8')

encrypted_passwd=bcrypt.hashpw(encode_passwd,bcrypt.gensalt())
print(encrypted_passwd)


