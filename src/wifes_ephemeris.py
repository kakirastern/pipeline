import numpy
import re

"""
Note:
 This sub-module is designed exclusively for astronomical coordinate
 calculations performed internal to the pywifes package. Designed to
 prevent dependencies on external astronomical packages.

"""

def sex2dd(radec_str):
    """
    Converts sexagesimal coordinates strings like 'hh:mm:ss.ss +-dd:mm:ss.s'
    into a decimal degrees tuples (rr.rr, dd.dd).
    """
    ra_hms, dec_dms = radec_str.split()
    ra_hms = ra_hms[1:]
    dec_dms = dec_dms[1:]
#    print('ra_hms', ra_hms)
#    print('dec_dms', dec_dms)
    # fix ra
    ra_hh, ra_mm, ra_ss = re.findall(r"([\d.]*\d+)", ra_hms)
#    print(ra_hh, ra_mm, ra_ss) # For Debug, remove later
    ra_dd = 15.0*(float(ra_hh)
                  +float(ra_mm)/60.0
                  +float(ra_ss)/3600.0)
    # fix dec
    dec_hh, dec_mm, dec_ss = re.findall(r"([\d.]*\d+)", dec_dms)
#    print(dec_hh, dec_mm, dec_ss)
#    print(dec_dms[1])
    if dec_dms[1] == '-':
        sign = -1.0
    else:
        sign = 1.0
#    dec_hh, dec_mm, dec_ss = dec_dms[1:].split(':')
    dec_dd = sign*(abs(float(dec_hh))
                   +float(dec_mm)/60.0
                   +float(dec_ss)/3600.0)
    return (ra_dd, dec_dd)

def angsep(pos1, pos2):
    """
    Angular separation between two astronomical coordinates, in arcseconds
    """
    # get ra/dec of both positions in decimal degrees...
    try:
        ra1 = pos1[0]
        dec1 = pos1[1]
    except:
        ra1, dec1 = sex2dd(pos1)
    try:
        ra2 = pos2[0]
        dec2 = pos2[1]
    except:
        ra2, dec2 = sex2dd(pos2)
    # calculate separation
    sep = 3600.0*(
        (dec1-dec2)**2+
        (numpy.cos(numpy.radians(dec1))*(ra1-ra2))**2)**0.5
    return sep
