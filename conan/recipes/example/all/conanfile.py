from conan import ConanFile
from conan.tools.cmake import CMake, cmake_layout
from conan.tools.files import apply_conandata_patches, export_conandata_patches, get


class exampleRecipe(ConanFile):
    name = "example"
    package_type = "library"

    # Optional metadata
    license = "LLVM-exception"
    author = "Beman Project <noreply@bemanproject.org>"
    url = "https://github.com/beman-project/beman"
    description = "Example Beman Project library"
    topics = ("education", "C++")

    # Binary configuration
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False], "fPIC": [True, False]}
    default_options = {"shared": False, "fPIC": True}

    # Build configuration
    generators = "CMakeDeps", "CMakeToolchain"

    def config_options(self):
        if self.settings.os == "Windows":
            self.options.rm_safe("fPIC")

    def configure(self):
        if self.options.shared:
            self.options.rm_safe("fPIC")

    def export_sources(self):
        export_conandata_patches(self)

    def source(self):
        get(self, **self.conan_data["sources"][self.version], destination=self.source_folder,
            strip_root=True)
        apply_conandata_patches(self)

    def layout(self):
        cmake_layout(self, src_folder="src")

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        cmake = CMake(self)
        cmake.install()

    def package_info(self):
        self.cpp_info.libs = ["example"]
        # Disable Conan generation of CMake modules for this package.
        # This package already provides one!
        self.cpp_info.set_property("cmake_find_mode", "none")
        # Tell conan to set up discovery of CMake modules for this package.
        # The CMake modules for this project are installed under `lib`.
        self.cpp_info.builddirs.append(".")
    
