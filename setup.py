from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

ext = Extension(
    "ochre",
    ["ochre.pyx"],
    language="c++",
    include_dirs = ["."],
    libraries = ["stdc++"],
    extra_link_args = ["-lSDL2", "-lSDL2_ttf", "-lGLEW", "-lGL", "-lSOIL"],
    cmdclass = {'build_ext': build_ext}
)

setup(
    cmdclass = {'build_ext': build_ext},
    ext_modules = [ext]
)

