from conans import ConanFile
from conans import CMake


class UselessLib(ConanFile):
    name = 'useless-lib'
    version = '0.1'
    settings = 'os', 'arch', 'build_type', 'compiler' # build_type is debug/release

    def source(self):
        
        url = 'https://github.com/konstantin89/useless-conan-lib'
        self.run('git clone %s useless-lib' % url)



    def _configure_cmake(self):
        cmake = CMake(self)
        cmake.configure(source_dir='useless-lib')
        return cmake

    def build(self):
        
        cmake = self._configure_cmake()
        cmake.build()
        #cmake.install()

    def package_info(self):
        self.cpp_info.libs = ['useless-lib']    # Which library the users should link against


    def package(self):

        #self.copy("*.h", "include", "build/include", keep_path=False)
        cmake = self._configure_cmake()
        cmake.install()