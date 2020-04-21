# Python3
import numpy;
import scipy;
import matplotlib;
import gmpy2;

# print version
print('scipy      version ', scipy.__version__);
print('numpy      version ', numpy.__version__);
print('matplotlib version ', matplotlib.__version__);
print('gmpy2      version ', gmpy2.version());

#print(matplotlib.__file__);


#print(gmpy2.license());
print(gmpy2.mp_version());
print(gmpy2.mpfr_version());
print(gmpy2.mpc_version());

