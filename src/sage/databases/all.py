"""
This file gathers together all the tables in Sage.

    * ConwayPolynomials() -- database of selected Conway polynomials.

    * CremonaDatabase() - Cremona's tables of elliptic curves and related data.

    * JonesDatabase() -- returns the John Jones table of number fields
      with bounded ramification and degree <= 6.

    * SteinWatkinsAllData() and SteinWatkinsPrimeData() - The
      Stein-Watkins tables of elliptic curves and related data.

    * Sloane's tables -- sloane_sequence, sloane_find

    * SymbolicData() -- many benchmark and testing ideals

EXAMPLES::

    sage: ConwayPolynomials()
    Frank Luebeck's database of Conway polynomials

    sage: CremonaDatabase()
    Cremona's database of elliptic curves with conductor...

    sage: JonesDatabase()
    John Jones's table of number fields with bounded ramification and degree <= 6

    sage: SymbolicData()
    SymbolicData with ... ideals
"""

#*****************************************************************************
#       Copyright (C) 2005 William Stein <wstein@gmail.com>
#
#  Distributed under the terms of the GNU General Public License (GPL)
#  as published by the Free Software Foundation; either version 2 of
#  the License, or (at your option) any later version.
#                  http://www.gnu.org/licenses/
#*****************************************************************************


from sql_db import SQLQuery, SQLDatabase

from conway import ConwayPolynomials

from cremona import CremonaDatabase

from jones import JonesDatabase

from stein_watkins import SteinWatkinsAllData, SteinWatkinsPrimeData

from install import database_install

from sloane import sloane_sequence, sloane_find, SloaneEncyclopedia

from symbolic_data import SymbolicData

# commented out, since it's broken -- nobody updated the parser
# for the new format; nobody complained it didn't work, so it
# can't be that important.
#from lincodes import linear_code_bound

from odlyzko import zeta_zeros

from db_modular_polynomials import \
     ClassicalModularPolynomialDatabase, \
     DedekindEtaModularPolynomialDatabase, \
     DedekindEtaModularCorrespondenceDatabase, \
     AtkinModularPolynomialDatabase, \
     AtkinModularCorrespondenceDatabase

from db_class_polynomials import \
     HilbertClassPolynomialDatabase

from symbolic_data import SymbolicData

from cunningham_tables import cunningham_prime_factors
