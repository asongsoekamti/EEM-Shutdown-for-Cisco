from cli import *
ifname = cli('show logging | grep  ".*%ETHPORT-4-IF_SFP_WARNING:.* Power Warning" | last 1 | awk "{print $8}" | sed s/,//')
if (len(ifname) != 0):
        show_sfp_command = "show clock | head lines 1 >> int_error.txt ; show interface " + ifname.rstrip('\r\n') + " transceiver detail >> int_error.tx$
        show_int_command = "show clock | head lines 1 >> int_error.txt ; show interface " + ifname.rstrip('\r\n') + " | i Eth|CRC|drop|error|discard >> $
        int_desc_command = "show int " + ifname.rstrip('\r\n') + " | i Desc | sed 's/Description: //'"
        int_desc = cli(int_desc_command)
        shut_command = "conf t ; interface " + ifname.rstrip('\r\n') + " ; shutdown ; desc " + int_desc.rstrip('\r\n') + " shutdown by EEM"
        cli(show_sfp_command)
        cli(show_int_command)
        cli(shut_command)
else :
        ifname = cli('show logging | grep  ".*%ETH_PORT_CHANNEL-5-FOP_CHANGED:.* to none" | last 1 | awk "{print $13}"')
        show_sfp_command = "show clock | head lines 1 >> int_error.txt ; show interface " + ifname.rstrip('\r\n') + " transceiver detail >> int_error.tx$
        show_int_command = "show clock | head lines 1 >> int_error.txt ; show interface " + ifname.rstrip('\r\n') + " | i Eth|CRC|drop|error|discard >> $
        int_desc_command = "show int " + ifname.rstrip('\r\n') + " | i Desc | sed 's/Description: //'"
        int_desc = cli(int_desc_command)
        shut_command = "conf t ; interface " + ifname.rstrip('\r\n') + " ; shutdown ; desc " + int_desc.rstrip('\r\n') + " shutdown by EEM"
        cli(show_sfp_command)
        cli(show_int_command)
        cli(shut_command)
