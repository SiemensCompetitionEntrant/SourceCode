from version import version, required_versions
from setuptools import find_packages, setup


kwargs = dict(
    name='toil-rnaseq-sc',
    version=version,
    description="**redacted personally identifiable information** Toil-based RNA-seq single cell pipeline",
    author='**redacted personally identifiable information**',
    author_email='**redacted personally identifiable information**',
    url="**redacted personally identifiable information**",
    install_requires=[x + y for x, y in required_versions.iteritems()],
    tests_require=['pytest==2.8.3'],
    package_dir={'': 'src'},
    packages=find_packages('src'),
    entry_points={
        'console_scripts': ['toil-rnaseq-sc = toil_rnaseq_sc.rnaseq_sc_cgl_pipeline:main']})


setup(**kwargs)
