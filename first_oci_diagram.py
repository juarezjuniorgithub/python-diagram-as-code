# first_oci_diagram.py

from diagrams import Diagram
from diagrams.oci.compute import Container
from diagrams.oci.database import ADB
from diagrams.oci.network import LoadBalancer

with Diagram("OCI Web Service", show=False):
    LoadBalancer("Load Balancer") >> Container("Spring Boot") >> ADB("Customer DB")