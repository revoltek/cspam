#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2014 - Francesco de Gasperin - Huib Intema
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA

def cspam_step_selfcal(conf):
    """
    Selfcal step
    """


                    # reload only static initial flags
                    default('flagmanager')
                    flagmanager(vis=MS.file_name, mode='restore', versionname='AfterInitialFlagging')

                    # run aoflagger
                    syscommand = '~/opt/src/aoflagger/build/src/aoflagger -column CORRECTED_DATA -strategy ~/phd/obs/GMRT/rfi_GMRT610.rfis -indirect-read ' + MS.file_name
                    os.system(syscommand)

                    # flag statistics after flagging
                    stats_flag(MS.file_name)

                    default('flagmanager')
                    flagmanager(vis=MS.file_name, mode='save', versionname='AfterDeepFlagging', comment=str(datetime.datetime.now()))
                    logging.info("Saved flags in AfterDeepFlagging")

