from setuptools import setup

setup(
    name='SSplines',
    version='2.0.0',
    packages=['SSplines'],
    url='https://github.com/qTipTip/SSplines2',
    license='MIT',
    author='Ivar Stangeby',
    author_email='istangeby@gmail.com',
    description='A small Python library for the evaluation of S-splines on the Powell-Sabin 12-split of a triangle.',
    long_description='''This Python library lets you instantiate constant,
    linear and quadratic spline spaces on the Powell-Sabin 12-split of a
    triangle. Given a set of coefficients a SplineSpace returns a callable
    SplineFunction which can be evaluated and differentiated.''',
    install_requires=['numpy', 'matplotlib'],
    python_requires='>=3',
)