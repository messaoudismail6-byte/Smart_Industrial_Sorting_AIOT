# Network and cybersecurity baseline

Separate the OT control network from the normal office LAN where possible.

Suggested zones:

```text
[OT VLAN]
 PLC / HMI / Robot / VFD / Factory I/O

        |
     Firewall
        |

[IIoT VLAN]
 MQTT / Node-RED / AI / Historian

        |
     Firewall
        |

[IT]
 Engineering workstation / reporting
```

Baseline controls:
- change default credentials
- restrict MQTT access
- use TLS/authentication outside a lab
- firewall unnecessary ports
- back up TIA/HMI/robot projects
- log operator actions
- keep safety functions independent from AI
