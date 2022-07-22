# EEM-Shutdown-for-Cisco
Shutdown Interface Automatically on Cisco

###########
# Pre-req #
###########
- show processes cpu
- show processes memory
- show logging | last 20
- show interface transceiver detail | I Eth|Measure|Tx|Rx
- show interface | I Eth|Desc|CRC|drop|discard
- show vpc summary
- show port-channel summary

##############
# Deployment #
##############
copy scp//dradmins@10.38.129.34/NET_DUMP/nx_shutint.py bootflash:
event manager applet PROACTIVE_SHUTDOWN_PORT
  event syslog tag sfp_warning pattern ".*%ETHPORT-4-IF_SFP_WARNING:.* Power Warning"
  event syslog tag port_down pattern ".*%ETH_PORT_CHANNEL-5-FOP_CHANGED:.* to none"
  tag sfp_warning or port_down happens 1 in 1
  action 1.0 cli python bootflash:///nx_shutint.py
  action 2.0 syslog priority alerts msg interface shutdown by EEM Script. Do show int desc
  
###################
# Post deployment #
###################
- show event manager history event
- show processes cpu
- show processes memory
- show logging | last 20"
- show interface transceiver detail | I Eth|Measure|Tx|Rx
- show interface | I Eth|Desc|CRC|drop|discard"
- show vpc summary
- show port-channel summary
