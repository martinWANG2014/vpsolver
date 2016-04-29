#!/usr/bin/env python
"""
This code is part of the Arc-flow Vector Packing Solver (VPSolver).

Copyright (C) 2013-2016, Filipe Brandao
Faculdade de Ciencias, Universidade do Porto
Porto, Portugal. All rights reserved. E-mail: <fdabrandao@dcc.fc.up.pt>.

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as
published by the Free Software Foundation, either version 3 of the
License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""
from __future__ import print_function


def test_mvpsolver2013():
    """Test mvpsolver2013."""
    from pyvpsolver.solvers import mvpsolver2013 as mvpsolver
    Ws = [(100, 75), (75, 50)]
    Cs = [3, 2]
    Qs = [-1, -1]
    ws = [
        [(75, 50)],
        [(40, 15), (25, 25)]
    ]
    b = [2, 1]
    solution = mvpsolver.solve(Ws, Cs, Qs, ws, b, script="vpsolver_glpk.sh")
    obj, patterns = solution
    assert obj == 5


def test_draw():
    from pyvpsolver import MVP, AFG
    instance = MVP.from_file("instance.mvp")
    AFG(instance).draw("graph.svg")


if __name__ == "__main__":
    test_mvpsolver2013()
