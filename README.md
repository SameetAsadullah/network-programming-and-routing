# Route Bridge

C TCP/UDP socket services and Cisco Packet Tracer network topologies covering routing and network services.

The socket programs implement client/server communication, while the topologies model routed networks and services. Source files, topology files, and validation checks are organized by subsystem.

## Contents

| Area | Implementations |
|---|---|
| Socket programming | [TCP client/server](sockets/tcp-client-server), [multi-client TCP](sockets/tcp-multi-client), [UDP client/server](sockets/udp-client-server), and a [`select`-based concurrent server](sockets/select-concurrent-server) |
| Packet Tracer | [Static routing](packet-tracer/static-routing), [dynamic routing](packet-tracer/dynamic-routing), [DHCP](packet-tracer/dhcp), [OSPF](packet-tracer/ospf), [EIGRP](packet-tracer/eigrp), and an [integrated routed/server network](packet-tracer/integrated-network) |

## Toolchains

- A POSIX environment with a C compiler for socket examples
- Cisco Packet Tracer for `.pkt` topology files

Each component includes its README, source, screenshots, and topology files where available.

## Provenance and licensing

See [PROVENANCE.md](PROVENANCE.md) for source history and licensing. Existing component licenses are retained; no blanket license is applied to previously unlicensed work.
