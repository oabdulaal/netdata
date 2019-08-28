# SPDX-License-Identifier: GPL-3.0-or-later

# THIS IS NOT A COMPLETE Makefile
# IT IS INCLUDED BY ITS PARENT'S Makefile.am
# IT IS REQUIRED TO REFERENCE ALL FILES RELATIVE TO THE PARENT

# install these files
dist_node_DATA       += powertop/powertop.node.js
# dist_nodeconfig_DATA += powertop/powertop.conf

# do not install these files, but include them in the distribution
dist_noinst_DATA       += powertop/README.md powertop/Makefile.inc