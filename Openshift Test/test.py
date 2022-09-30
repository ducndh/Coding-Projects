from telnetlib import PRAGMA_HEARTBEAT
from kubernetes import client, config
from openshift.dynamic import DynamicClient
import yaml
import urllib3

urllib3.disable_warnings()
k8s_client = config.new_client_from_config()
dyn_client = DynamicClient(k8s_client)

v1_projects = dyn_client.resources.get(api_version='project.openshift.io/v1', kind='Project')

project_list = [project.metadata.name for project in v1_projects.get().items]
print(project_list)

v1_services = dyn_client.resources.get(api_version='template.openshift.io/v1', kind='Template')
resp = v1_services.create(body="postgresql-persistent-test", namespace="fis-mbf-dplat")
print(resp)