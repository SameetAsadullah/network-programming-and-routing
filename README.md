# Network Programming and Routing

A curated collection of TCP/UDP socket systems and Cisco Packet Tracer network designs.

The repository connects two sides of network engineering: implementing TCP/UDP communication in C and designing routed services and protocols in simulated networks. Original implementations and Packet Tracer files are retained with consistent organization and validation.

## Contents

| Area | Implementations |
|---|---|
| Socket programming | [TCP client/server](sockets/tcp-client-server), [multi-client TCP](sockets/tcp-multi-client), [UDP client/server](sockets/udp-client-server), and a [`select`-based concurrent server](sockets/select-concurrent-server) |
| Packet Tracer | [Static routing](packet-tracer/static-routing), [dynamic routing](packet-tracer/dynamic-routing), [DHCP](packet-tracer/dhcp), [OSPF](packet-tracer/ospf), [EIGRP](packet-tracer/eigrp), and an [integrated routed/server network](packet-tracer/integrated-network) |

## Toolchains

- A POSIX environment with a C compiler for socket examples
- Cisco Packet Tracer for `.pkt` topology files

Each implementation retains its README, source, screenshots, and topology files where available.

## Provenance and licensing

See [PROVENANCE.md](PROVENANCE.md). Per-project license files are retained where they existed; no blanket license is applied to previously unlicensed work.
