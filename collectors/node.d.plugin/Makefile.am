# SPDX-License-Identifier: GPL-3.0-or-later

MAINTAINERCLEANFILES = $(srcdir)/Makefile.in
CLEANFILES = \
	node.d.plugin \
	$(NULL)

include $(top_srcdir)/build/subst.inc
SUFFIXES = .in

dist_libconfig_DATA = \
    node.d.conf \
    $(NULL)

dist_plugins_SCRIPTS = \
	node.d.plugin \
	$(NULL)

dist_noinst_DATA = \
	node.d.plugin.in \
	README.md \
	$(NULL)

usernodeconfigdir=$(configdir)/node.d
dist_usernodeconfig_DATA = \
    .keep \
    $(NULL)

nodeconfigdir=$(libconfigdir)/node.d
dist_nodeconfig_DATA = \
    $(NULL)

dist_node_DATA = \
	$(NULL)

include fronius/Makefile.inc
include named/Makefile.inc
include sma_webbox/Makefile.inc
include snmp/Makefile.inc
include stiebeleltron/Makefile.inc
include powertop/Makefile.inc

nodemodulesdir=$(nodedir)/node_modules
dist_nodemodules_DATA = \
	node_modules/netdata.js \
	node_modules/extend.js \
	node_modules/pixl-xml.js \
	node_modules/net-snmp.js \
	node_modules/asn1-ber.js \
	node_modules/glob.js \
	node_modules/html2json.js \
	node_modules/interpret.js \
	node_modules/rechoir.js \
	node_modules/shelljs.js \
	node_modules/sync.js \
	node_modules/plugin.js \
	node_modules/make.js \
	node_modules/global.js \
	node_modules/common.js \
	node_modules/commands.js \
	node_modules/tweetnacl.js \
	node_modules/streamsearch.js \
	node_modules/ssh2-streams.js \
	node_modules/safer.js \
	node_modules/bcrypt-pbkdf.js \
	node_modules/asn1.js
	$(NULL)

nodemoduleslibberdir=$(nodedir)/node_modules/lib/ber
dist_nodemoduleslibber_DATA = \
	node_modules/lib/ber/index.js \
	node_modules/lib/ber/errors.js \
	node_modules/lib/ber/reader.js \
	node_modules/lib/ber/types.js \
	node_modules/lib/ber/writer.js \
	$(NULL)

nodemoduleslibrechoirdir=$(nodedir)/node_modules/lib
dist_nodemoduleslibrechoir_DATA = \
	node_modules/lib/rechoir/extension.js \
	node_modules/lib/rechoir/normalize.js \
	node_modules/lib/rechoir/register.js \
	$(NULL)

nodemoduleslibdir=$(nodedir)/node_modules/lib
dist_nodemoduleslibrechoir_DATA = \
	node_modules/lib/buffer-helpers.js \
	node_modules/lib/constants.js \
	node_modules/lib/jsbn.js \
	node_modules/lib/keyParser.js \
	node_modules/lib/sftp.js \
	node_modules/lib/ssh.js \
	node_modules/lib/utils.js \
	$(NULL)

nodemoduleslibpuredir=$(nodedir)/node_modules/lib/pure
dist_nodemoduleslibpure_DATA = \
	node_modules/lib/pure/htmlparser.js \
	$(NULL)

nodemodulessrcshelljsdir=$(nodedir)/node_modules/src
dist_nodemodulessrcshelljs_DATA = \
	node_modules/src/common.js \
	node_modules/src/echo.js \
	node_modules/src/error.js \
	node_modules/src/exec-child.js \
	node_modules/src/exec.js \
	node_modules/src/which.js \
	node_modules/src/cat.js \
	node_modules/src/cd.js \
	node_modules/src/chmod.js \
	node_modules/src/cp.js \
	node_modules/src/dirs.js \
	node_modules/src/find.js \
	node_modules/src/grep.js \
	node_modules/src/head.js \
	node_modules/src/ln.js \
	node_modules/src/ls.js \
	node_modules/src/mkdir.js \
	node_modules/src/mv.js \
	node_modules/src/popd.js \
	node_modules/src/pushd.js \
	node_modules/src/pwd.js \
	node_modules/src/rm.js \
	node_modules/src/sed.js \
	node_modules/src/set.js \
	node_modules/src/sort.js \
	node_modules/src/tail.js \
	node_modules/src/tempdir.js \
	node_modules/src/test.js \
	node_modules/src/to.js \
	node_modules/src/toEnd.js \
	node_modules/src/touch.js \
	node_modules/src/uniq.js \
	$(NULL)

nodemoduleslibssh2dir=$(nodedir)/node_modules/lib/ssh2
dist_nodemoduleslibssh2_DATA = \
	node_modules/lib/ssh2/agent.js \
	node_modules/lib/ssh2/buffer-helpers.js \
	node_modules/lib/ssh2/Channel.js \
	node_modules/lib/ssh2/client.js \
	node_modules/lib/ssh2/http-agents.js \
	node_modules/lib/ssh2/keepalivemgr.js \
	node_modules/lib/ssh2/server.js \
	node_modules/lib/ssh2/SFTPWrapper.js \
	$(NULL)
