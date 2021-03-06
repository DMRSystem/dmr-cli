from pybuilder.core import init, use_plugin, Author

use_plugin("python.core")
use_plugin("python.install_dependencies")
use_plugin("python.unittest")
use_plugin("python.coverage")
use_plugin("python.pycharm")
use_plugin("python.distutils")

default_task = ["install_dependencies", "publish", "install"]

version = '0.0.1'
summary = 'Command Line Interface for the DMR System'
authors = (Author('Connor Boyle', 'cjblink1@gmail.com'),)
license = 'MIT'
url = 'DMRSystem.github.io/documentation'


@init
def initialize(project):
    project.depends_on_requirements('requirements.txt')
    project.build_depends_on('mockito')
    project.build_depends_on('coveralls')
    project.set_property('distutils_console_scripts', ['dmr=dmr.cli.main:main'])
