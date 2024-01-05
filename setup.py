from setuptools import setup, find_packages

#This is a list of files to install, and where
#(relative to the 'root' dir, where setup.py is)
#You could be more specific.

setup(name = "mediasdk",
    version = "1.0.1",
    description = "tencent 媒体AI中台 sdk",
    author = "willzhen",
    author_email = "willzhen@tencent.com",
    url = "https://github.com/Tencent-media-asset-system-sdk/media-platform-sdk-python",
    #Name the folder where your packages live:
    #(If you have other packages (dirs) or modules (py files) then
    #put them into the package directory - they will be found
    #recursively.)
    packages=['mediasdk'],
    #'package' package must contain files (see list above)
    #I called the package 'package' thus cleverly confusing the whole issue...
    #This dict maps the package name =to=> directories
    #It says, package *needs* these files.
    #'runner' is in the root.
    # scripts = ["runner"],
    # long_description = """Really long text here.""",
    #
    #This next part it for the Cheese Shop, look a little down the page.
    #classifiers = []
    python_requires='>=3.6'
)