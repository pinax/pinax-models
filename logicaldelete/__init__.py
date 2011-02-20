VERSION = (1, 1, 0, "b", 1) # following PEP 386
DEV_N = 2
POST_N = 0


def build_version():
    version = "%s.%s" % (VERSION[0], VERSION[1])
    if VERSION[2]:
        version = "%s.%s" % (version, VERSION[2])
    if VERSION[3] != "f":
        version = "%s%s%s" % (version, VERSION[3], VERSION[4])
        if DEV_N:
            version = "%s.dev%s" % (version, DEV_N)
    elif POST_N > 0:
        version = "%s.post%s" % (version, POST_N)
    return version


__version__ = build_version()
