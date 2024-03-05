import os

from aws_cdk import (
    Stack,
    aws_s3 as s3,
    aws_s3_deployment as s3deploy
)

SITE_SOURCE_DIR = os.path.join(
    os.path.dirname(os.path.dirname(__file__)), os.pardir, 'site')

class Site(Stack):

    def __init__(self, scope, id, **kwargs):
        super().__init__(scope, id, **kwargs)
        
        self.bucket = s3.Bucket(self, "WebsiteBucket",
            website_index_document="index.html",
            block_public_access=s3.BlockPublicAccess(block_public_policy=False),
            public_read_access=True
        )

        s3deploy.BucketDeployment(self, "DeployWebsite",
            sources=[s3deploy.Source.asset("../site/dist")],
            destination_bucket=self.bucket,
            destination_key_prefix="/"
        )