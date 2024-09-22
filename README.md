# Primitive Peer 2 Peer Protocol (P4)
> A simple peer to peer protocol for file sharing.

## Intro
P4 is a simple peer to peer protocol for file sharing. It is designed to be simple and easy to implement. It is a http and gRPC based protocol, with a simple REST API for control and a gRPC for data transfer.

## Requirements
1. Python 3.11+
2. mutiple peers (it can be addressed by using Docker or modifying each peer working port)
3. If using with multiple computers, by default, the 8000 is used as the control port and 8001 is used as the data port, so theses ports should be open in the firewall.

## Quick Start
Full setup and user guide can be found in the [User manual](https://github.com/02loveslollipop/PrimitivePeer2PeerProtocol/wiki/User-manual)

1. Clone the repository
```bash
git clone https://github.com/02loveslollipop/PrimitivePeer2PeerProtocol.git
cd PrimitivePeer2PeerProtocol
```

2. (Optional) Create a conda environment
```bash
conda create -n p4 python=3.11
conda activate p4
```

3. Install the requirements
```bash
pip install -r requirements.txt
```

4. Start the server
```bash
python ./Server/server.py
```

5. Start peer server
```bash
python ./Peer/peer.py --server
```

6. Start peer client
```bash
python ./Peer/peer.py
```


