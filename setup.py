from setuptools import setup

setup(
    name='my_app',
    version='0.1.0',
    author='Vskoboinikov_Ihor',
    author_email='voskoboinikov777@.jmail.com',
    description='FastApi app',
    scripts=['test_project/app.py'],
    install_requires=[
            'fastapi==0.82.0',
            'pydantic==1.10.2',
            'uvicorn==0.18.3',
            'python-dotenv==0.21.0',
            'SQLAlchemy==1.4.41',
            'python-dotenv==0.21.0'
    ]
)
