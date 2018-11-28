
# This file was *autogenerated* from the file ellipticcurve.sage
from sage.all_cmdline import *   # import sage library

_sage_const_775807209463167910095539163959068826 = Integer(775807209463167910095539163959068826); _sage_const_775010084514487531788273912037060561 = Integer(775010084514487531788273912037060561); _sage_const_1 = Integer(1); _sage_const_771157329084582589666569152178346504 = Integer(771157329084582589666569152178346504); _sage_const_323141381196798033512190262227161667 = Integer(323141381196798033512190262227161667); _sage_const_869049850567812139357308211622374273 = Integer(869049850567812139357308211622374273); _sage_const_591153005086204165523829267245014771 = Integer(591153005086204165523829267245014771); _sage_const_238266381988261346751878607720968495 = Integer(238266381988261346751878607720968495); _sage_const_889774351128949770355298446172353873 = Integer(889774351128949770355298446172353873); _sage_const_12 = Integer(12); _sage_const_67890 = Integer(67890); _sage_const_341454032985370081366658659122300896 = Integer(341454032985370081366658659122300896); _sage_const_12345 = Integer(12345)
from sage.all import *

def _EllipticCurve(p, a, b):
    E = EllipticCurve(GF(p), [a, b])
    return E

def _add(P, Q):
    return P + Q

def _scalar_mul(c, P):
    return c*P

def _testECC():
    """
    Reference: https://ctftime.org/task/6860

    Testing validity for single instance
    """
    # Defining the Elliptic Curve
    p = _sage_const_889774351128949770355298446172353873 
    a = _sage_const_12345 
    b = _sage_const_67890 
    E = _EllipticCurve(p, a, b)

    # Defining points on the Elliptic Curve
    px, py = (_sage_const_238266381988261346751878607720968495 , _sage_const_591153005086204165523829267245014771 )
    qx, qy = (_sage_const_341454032985370081366658659122300896 , _sage_const_775807209463167910095539163959068826 )
    P = E((px, py))
    Q = E((qx, qy))

    P_plus_Q = E((_sage_const_323141381196798033512190262227161667 , _sage_const_775010084514487531788273912037060561 ))
    twelveP = E((_sage_const_771157329084582589666569152178346504 , _sage_const_869049850567812139357308211622374273 ))

    try:
        assert _add(P, Q) == P_plus_Q
        assert _scalar_mul(_sage_const_12 , P) == twelveP
    except:
        return -_sage_const_1 
    return _sage_const_1 

if _testECC() == _sage_const_1 :
    print "[+] Test Passed!"
else:
    print "[-] Test Failed!"
