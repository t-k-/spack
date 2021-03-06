##############################################################################
# Copyright (c) 2013-2017, Lawrence Livermore National Security, LLC.
# Produced at the Lawrence Livermore National Laboratory.
#
# This file is part of Spack.
# Created by Todd Gamblin, tgamblin@llnl.gov, All rights reserved.
# LLNL-CODE-647188
#
# For details, see https://github.com/spack/spack
# Please also see the NOTICE and LICENSE files for our notice and the LGPL.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License (as
# published by the Free Software Foundation) version 2.1, February 1999.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the IMPLIED WARRANTY OF
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the terms and
# conditions of the GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA
##############################################################################
from spack import *


class Xclip(AutotoolsPackage):
    """xclip is a command line utility that is designed to run on any system
       with an X11 implementation. It provides an interface to X selections
       ("the clipboard") from the command line. It can read data from standard
       in or a file and place it in an X selection for pasting into other X
       applications. xclip can also print an X selection to standard out,
       which can then be redirected to a file or another program."""

    homepage = "https://github.com/astrand/xclip"
    url      = "https://github.com/astrand/xclip"

    version('0.13', git='https://github.com/astrand/xclip', commit='9aa7090c3b8b437c6489edca32ae43d82e0c1281')

    depends_on('libxmu')
    depends_on('libx11')
    depends_on('autoconf', type='build')
    depends_on('automake', type='build')
    depends_on('libtool', type='build')
    depends_on('m4', type='build')
