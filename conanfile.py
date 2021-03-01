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

    def package_info(self):
        self.cpp_info.libs = ['useless-lib']    # Which library the users should link against

    def package(self):

        # Public headers
        self.copy(pattern="*.h", dst="include", src="useless-lib/include", keep_path=False)

        # Library bins
        self.copy(pattern="*.lib", dst="lib", src="useless-lib/output", keep_path=False)
        self.copy(pattern="*.a", dst="lib", src="useless-lib/output", keep_path=False)
