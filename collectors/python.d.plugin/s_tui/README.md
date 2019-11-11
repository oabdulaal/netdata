# S-TUI

This module monitors the [s-tui](https://github.com/amanusk/s-tui) cli tool.

**Requirements and Notes:**

-   You must have the `s-tui` tool installed. [installation](https://github.com/amanusk/s-tui#simple-installation)

-   Make sure that the plugin is enabled in `python.d.plugin/python.d.conf`.

-   Make sure `netdata` user can execute `/usr/local/bin/s-tui` or wherever your binary is.


- Make sure that `s-tui` is running on the dashboard. Sometimes it takes a bit of time to start up. If not, try restarting Netdata. 

- For debugging the plugin check the collectors [documentation](https://github.com/netdata/netdata/tree/master/collectors/python.d.plugin)

**Produces:**

1.  Monitors the overall CPU:

    -   Power consumption
    -   Temperature

