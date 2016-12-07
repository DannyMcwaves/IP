from distutils.core import setup

setup(
    name="ip",
    version="1.0.0",
    packages=["ip", "ip/utils", "ip/tests", "ip/resolve"],
    author="Danny mcwaves",
    author_email="dannymcwaves96@gmail.com",
    url="https://github.com/DannyMcwaves/IP",
    description="A simple IP manipulation tool for ip addresses",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 1 - Beta",
        "Topic :: Software Development :: Libraries :: Python Modules"
    ]
)

