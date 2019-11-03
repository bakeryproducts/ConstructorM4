# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.1
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _lti
else:
    import _lti

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)


def _swig_setattr_nondynamic_instance_variable(set):
    def set_instance_attr(self, name, value):
        if name == "thisown":
            self.this.own(value)
        elif name == "this":
            set(self, name, value)
        elif hasattr(self, name) and isinstance(getattr(type(self), name), property):
            set(self, name, value)
        else:
            raise AttributeError("You cannot add instance attributes to %s" % self)
    return set_instance_attr


def _swig_setattr_nondynamic_class_variable(set):
    def set_class_attr(cls, name, value):
        if hasattr(cls, name) and not isinstance(getattr(cls, name), property):
            set(cls, name, value)
        else:
            raise AttributeError("You cannot add class attributes to %s" % cls)
    return set_class_attr


def _swig_add_metaclass(metaclass):
    """Class decorator for adding a metaclass to a SWIG wrapped class - a slimmed down version of six.add_metaclass"""
    def wrapper(cls):
        return metaclass(cls.__name__, cls.__bases__, cls.__dict__.copy())
    return wrapper


class _SwigNonDynamicMeta(type):
    """Meta class to enforce nondynamic attributes (no new attributes) for a class"""
    __setattr__ = _swig_setattr_nondynamic_class_variable(type.__setattr__)


class Vec3(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    x = property(_lti.Vec3_x_get, _lti.Vec3_x_set)
    y = property(_lti.Vec3_y_get, _lti.Vec3_y_set)
    z = property(_lti.Vec3_z_get, _lti.Vec3_z_set)

    def __init__(self):
        _lti.Vec3_swiginit(self, _lti.new_Vec3())
    __swig_destroy__ = _lti.delete_Vec3

# Register Vec3 in _lti:
_lti.Vec3_swigregister(Vec3)

class Ray(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    orig = property(_lti.Ray_orig_get, _lti.Ray_orig_set)
    dir = property(_lti.Ray_dir_get, _lti.Ray_dir_set)

    def __init__(self):
        _lti.Ray_swiginit(self, _lti.new_Ray())
    __swig_destroy__ = _lti.delete_Ray

# Register Ray in _lti:
_lti.Ray_swigregister(Ray)

class Pair(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    val = property(_lti.Pair_val_get, _lti.Pair_val_set)
    idx = property(_lti.Pair_idx_get, _lti.Pair_idx_set)

    def __init__(self):
        _lti.Pair_swiginit(self, _lti.new_Pair())
    __swig_destroy__ = _lti.delete_Pair

# Register Pair in _lti:
_lti.Pair_swigregister(Pair)


def sub(a, b):
    return _lti.sub(a, b)

def dot(a, b):
    return _lti.dot(a, b)

def len(v):
    return _lti.len(v)

def normalize(v):
    return _lti.normalize(v)

def cross(a, b):
    return _lti.cross(a, b)

def randomSphere():
    return _lti.randomSphere()

def rayTriangleIntersect(r, v0, v1, v2):
    return _lti.rayTriangleIntersect(r, v0, v1, v2)

def fact(npyTriVert2D, npyRayVert2D):
    return _lti.fact(npyTriVert2D, npyRayVert2D)

