#!/usr/bin/env python3
import os
import sys
from aws_cdk import App, Environment
from stacks.site import Site

from dotenv import load_dotenv

from aws_cdk import (
    aws_ec2 as ec2,
)

load_dotenv("../.env")

dev = Environment(account=os.getenv('AWS_ACCOUNT_ID'), region=os.getenv('AWS_REGION'))

app = App()

site = Site(app, 'template-site', env=dev)

app.synth()
