from decimal import Decimal

from sympy import Symbol, solve
from numpy.testing import assert_allclose

NICKNAME = "underham2ter"


def solve_quad(b, c):
    """ Parameters
    ----------
    b, c : float
       Coefficients

    Returns
    -------
    x1, x2 : float or complex
        Roots.
    """
    # sqrt и с_sqrt не дают нужную точночть

    # аккуратный подсчет d
    # d = (Decimal(b ** 2) - Decimal(4 * c))

    x = Symbol('x')
    sol = solve(x ** 2 + b * x + c, x)

    if len(sol) == 1:
        return [complex(sol[0]), complex(sol[0])]
    else:
        return [complex(sol[0]), complex(sol[1])]
    raise NotImplementedError()


# Your implementation should pass tests in this cell.
#
# Do not remove or alter this cell. You may run it, but do not remove or alter it.
# Your changes to this cell will be ignored on grading.
# There will be additional tests.
#


variants = [{'b': 4.0, 'c': 3.0},
            {'b': 2.0, 'c': 1.0},
            {'b': 0.5, 'c': 4.0},
            {'b': 1e10, 'c': 3.0},
            {'b': -1e12, 'c': -1.0}]

for var in variants:
    x1, x2 = solve_quad(**var)
    assert_allclose(x1*x2, var['c'], rtol=1e-15)
