from openshift import Result
import openshift as oc

try:
    r = Result("run-test")
    r.add_action(oc.oc_action(oc.cur_context(), "new-app", cmd_args=["--template=postgresql-persistent-test", "--name=postgresql-test","--param=DATABASE_SERVICE_NAME=postgresql-test", "--param=POSTGRESQL_USER=user", "--param=POSTGRESQL_PASSWORD=1234", "--param=POSTGRESQL_DATABASE=database", "--param=POSTGRESQL_VERSION=12", "--param=MEMORY_LIMIT=512Mi", "--param=VOLUME_CAPACITY=1Gi", "--param=CPU_LIMIT=1", None]))
    print("Output: {}".format(r.out().strip()))
except Exception as e:
    print(e)