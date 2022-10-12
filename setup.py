from setuptools import setup, find_packages

setup(name="detr",
      version="1.0",
      packages=find_packages(),
      install_requires =[
            "cython",
            "submitit",
            "torch>=1.5.0",
            "torchvision>=0.6.0",
            "scipy"
            ])
