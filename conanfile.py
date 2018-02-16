from conans import ConanFile, tools, AutoToolsBuildEnvironment
import os

class OmniorbConan(ConanFile):
    name = "omniorb"
    version = "4.2.2"
    license = "GNU Lesser General Public License (for the libraries), and GNU General Public License (for the tools)"
    url = "<Package recipe repository url here, for issues about the package>"
    description = "omniORB is a robust high performance CORBA ORB for C++ and Python"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=False"
    generators = "cmake"
    root = "omniORB-" + version
    install_dir = 'omniorb-install'

    def source(self):
        archive_name = "omniORB-%s.tar.bz2" % self.version
        source_url = "https://downloads.sourceforge.net/project/omniorb/omniORB/omniORB-%s/%s" % ( self.version, archive_name )
        tools.get(source_url)

    def build_configure(self):
        prefix = os.path.abspath(self.install_dir)
        with tools.chdir(self.root):
            env_build = AutoToolsBuildEnvironment(self)
            args = ['--prefix=%s' % prefix]
            env_build.configure(args=args)
            env_build.make()
            env_build.make(args=['install'])

    def build(self):
        self.build_configure()

    def package(self):
        inc_dir = os.path.join(self.install_dir, 'include')
        lib_dir = os.path.join(self.install_dir, 'lib')
        self.copy(pattern="*.h*", dst="include", src=inc_dir, keep_path=True)
        self.copy(pattern="*.so*", dst="lib", src=lib_dir, keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ['omniORB4','omnithread']
