# powertop

This module monitors the [powertop](https://wiki.archlinux.org/index.php/Powertop) cli tool.

**Requirements and Notes:**

-   You must have the `powertop` tool installed. Example [for ubuntu 16.04](https://linoxide.com/linux-how-to/install-use-powertop-ubuntu-16-04/)

-   Make sure that the plugin is enabled in `python.d.plugin/python.d.conf`.

-   Make sure `netdata` user can execute `/usr/sbin/powertop` or wherever your binary is, and also the `cat` command in `/bin/cat`.

-   Netdata needs to run `powertop` and `cat` in using `sudo`. So you need to enable `sudo` without password for the `netdata user` on the system you need to run on. Example:
    - Run `sudo visudo`
    - Add this line: 
        ```
        root    ALL=(ALL:ALL) ALL
        netdata ALL = NOPASSWD: /usr/sbin/powertop, /bin/cat
        ```

- Make sure that `powertop` is running on the dashboard. Sometimes it takes a bit of time to start up. If not, try restarting Netdata. 

- For debugging the plugin check the collectors [documentation](https://github.com/netdata/netdata/tree/master/collectors/python.d.plugin)

**Produces:**

1.  Per Proccess running on the CPU

    -   Percentage of power consumption

