from setuptools import find_packages, setup

package_name = 'lidar_scan_relay'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
         ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='blancjh',
    maintainer_email='blancjh@example.com',
    description='A simple ROS 2 node that relays /lidar/scan to /scan.',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'relay = lidar_scan_relay.relay:main',
        ],
    },
)
