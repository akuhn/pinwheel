# Contributing

Bug reports and pull requests are welcome on github at, https://github.com/akuhn/pinwheel

# Deployment

To build this package, run

    brew install pandoc
    pip install pypandoc
    python setup.py sdist

For my personal use, to deploy this package, run

    # Requires accounts on pypi
    # Requires .pypirc file in home folder
    twine upload -r test dist/pinwheel-0.0.0.tar.gz
    pip install --user -i https://testpypi.python.org/pypi pinwheel
    open https://test.pypi.org/project/pinwheel
    # Verify readme and package, and then continue with
    twine upload dist/pinwheel-0.0.0.tar.gz
