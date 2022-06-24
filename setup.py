from setuptools import setup
from torch.utils.cpp_extension import BuildExtension, CUDAExtension

setup(
    name='semnan_cuda',
    ext_modules=[
        CUDAExtension('semnan_cuda', [
            'semnan_cuda.cpp',
            'semnan_solver_kernel.cu',
        ], extra_compile_args={'cxx': ['/std:c++17']})
    ],
    cmdclass={
        'build_ext': BuildExtension
    },
    install_requires=[
       'torch>=1.10.1+cu102',
    ]
)
