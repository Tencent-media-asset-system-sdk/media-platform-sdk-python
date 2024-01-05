from setuptools import setup, find_packages

#This is a list of files to install, and where
#(relative to the 'root' dir, where setup.py is)
#You could be more specific.
files = ["protobufspec/*", "trpc_mock/*"]

setup(name = "aimediasdk",
    version = "100",
    description = "tencent 媒体AI中台 sdk",
    author = "willzhen",
    author_email = "willzhen@tencent.com",
    url = "",
    #Name the folder where your packages live:
    #(If you have other packages (dirs) or modules (py files) then
    #put them into the package directory - they will be found
    #recursively.)
    packages=find_packages(),
    #'package' package must contain files (see list above)
    #I called the package 'package' thus cleverly confusing the whole issue...
    #This dict maps the package name =to=> directories
    #It says, package *needs* these files.
    package_data = {'package' : files },
    #'runner' is in the root.
    # scripts = ["runner"],
    # long_description = """Really long text here.""",
    #
    #This next part it for the Cheese Shop, look a little down the page.
    #classifiers = []
    python_requires='>=3.6'
)