from pybuilder.core import init, use_plugin

use_plugin("python.core")
use_plugin("python.install_dependencies")
use_plugin("python.unittest")
use_plugin("python.coverage")
use_plugin("python.pycharm")
use_plugin("python.distutils")

default_task = ["install_dependencies", "install"]


@init
def initialize(project):
    project.depends_on_requirements('requirements.txt')
    project.build_depends_on('mockito')
    project.build_depends_on('coveralls')
    project.set_property('distutils_console_scripts', ['dmr=main:main'])
