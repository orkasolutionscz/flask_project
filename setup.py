from setuptools import setup

setup(
    name="markdown_blog",
    version="0.1",
    packages=["mdblog"],
    zip_safe=False,
    include_package_data=True,
    install_requires=[
        "celery==5.0.5",
        "Flask==1.1.2",
        "Flask-SQLAlchemy==2.5.1",
        "Flask-WTF==0.14.3",
        "email-validator==1.1.2",
    ]
)
