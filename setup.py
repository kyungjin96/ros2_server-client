from setuptools import setup

package_name = 'mytest'
setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='plantstoen',
    maintainer_email='plantstoen@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'main_client = mytest.main_client:main',
            'main_server = mytest.main_server:main',
            'sig_client = mytest.sigmoid_client:main',
        
        ],
    },
)

