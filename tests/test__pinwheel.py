from expects import *

import pinwheel


def test__should_have_version():
    expect(pinwheel).to(have_property('__version__'))
    expect(pinwheel.__version__).to(match(r'^\d+\.\d+\.\d+$'))


