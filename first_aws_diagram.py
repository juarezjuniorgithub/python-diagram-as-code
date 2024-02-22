# first_aws_diagram.py

from diagrams import Diagram
from diagrams.aws.compute import EC2
from diagrams.aws.database import RDS
from diagrams.aws.network import ELB

with Diagram("AWS Web Service", show=False):
    ELB("lb") >> EC2("web") >> RDS("userdb")