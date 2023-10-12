from setuptools import setup

package_name = 'ros_lsm6dsox_lis3mdl'

setup(
    name=package_name,
    version='0.0.1',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='rosblox',
    maintainer_email='polzin.max@gmail.com',
    description='Estimates the slope.',
    license='BSD3',
    entry_points={
        'console_scripts': [
                'slope_estimator = ros_slope_estimation.slope_estimator:main',
        ],
    },
)
