# flake8: noqa
import warnings
warnings.simplefilter('always', DeprecationWarning)
warnings.warn("Please convert to using 'miio' package, this package will "
              "be removed at some point in the future", DeprecationWarning,
              stacklevel=2)
from miio import *
