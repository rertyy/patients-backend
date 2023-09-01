from setuptools import setup, find_packages

setup(
    name="your-package-name",  # Replace with your package name
    version="0.1.0",  # Replace with your package version
    description="Description of your package",
    long_description="Long description of your package",  # Optional
    author="Your Name",
    author_email="your@email.com",
    packages=find_packages(),  # Automatically discover and include all Python packages
    install_requires=[
        # List your package's dependencies here
        "pymongo",
        "Flask",
        "flask-cors",
        "Gunicorn",
    ],
    classifiers=[],
)
