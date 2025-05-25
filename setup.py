from setuptools import setup, find_packages

setup(
    name='desersion_escolar',
    version='0.1.0',
    description='Conversión de CSV a base de datos SQLite para análisis de deserción escolar',
    author='cibarguen1018',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    include_package_data=True,
    install_requires=[
        "pandas>=2.0.0",
        "click>=8.0.0"
    ],
    entry_points={
        'console_scripts': [
            'convertir-csv-sqlite=convertir_csv_sqlite:main',
        ],
    },
)
