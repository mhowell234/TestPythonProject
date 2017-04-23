from pybuilder.core import init, task, use_plugin

use_plugin("python.core")
use_plugin("python.coverage")
use_plugin("python.distutils")
use_plugin("python.flake8")
use_plugin("python.install_dependencies")
use_plugin('python.pycharm')
use_plugin("python.unittest")

use_plugin("pypi:boto3")
use_plugin("pypi:click")
use_plugin("pypi:jmespath")
use_plugin("pypi:mockito")
use_plugin("pypi:prettytable")
use_plugin("pypi:pybuilder_aws_plugin")
use_plugin("pypi:simplejson")
use_plugin("pypi:click")


name = "TestPyProject"
default_task = "publish"

@init
def initialize(project):
    project.build_depends_on("gitpython")
    project.build_depends_on("pyyaml")
