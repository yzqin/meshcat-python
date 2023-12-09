from setuptools import setup, find_packages

setup(name="meshcat-sim_web_fork",
      version="0.4.0",
      description="WebGL-based visualizer for 3D geometries and scenes",
      url="https://github.com/rdeits/meshcat-python",
      author="Robin Deits",
      author_email="mail@robindeits.com",
      license="MIT",
      packages=find_packages("src",  exclude=["*.tests"]),
      package_dir={"": "src"},
      test_suite="meshcat",
      entry_points={
          "console_scripts": [
              "meshcat-server=meshcat.servers.zmqserver:main"
          ]
      },
      install_requires=[
          "ipython >= 5",
          "u-msgpack-python >= 2.4.1",
          "numpy >= 1.14.0",
          "tornado >= 4.0.0",
          "pyzmq >= 17.0.0",
          "pyngrok >= 4.1.6",
          "pillow >= 7.0.0"
      ],
      zip_safe=False,
      include_package_data=True
      )
