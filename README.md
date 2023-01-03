# py3stun

[![PyPI version](https://badge.fury.io/py/py3stun.svg)](https://badge.fury.io/py/py3stun)

Python 3 fork of [pystun](https://github.com/jtriley/pystun)

A Python STUN client for getting NAT type and external IP.

## Install

```bash
python -m pip install .
```

or

```bash
python -m pip install py3stun
```

## Usage

```powershell
$ python py3stun.py -h
# or if you install
$ py3stun.exe -h
usage: py3stun [-h] [-d] [-H STUN_HOST] [-P STUN_PORT] [-i SOURCE_IP] [-p SOURCE_PORT] [--version]

options:
  -h, --help            show this help message and exit
  -d, --debug           Enable debug logging (default: False)
  -H STUN_HOST, --stun-host STUN_HOST
                        STUN host to use (default: None)
  -P STUN_PORT, --stun-port STUN_PORT
                        STUN host port to use (default: 3478)
  -i SOURCE_IP, --source-ip SOURCE_IP
                        network interface for client (default: 0.0.0.0)
  -p SOURCE_PORT, --source-port SOURCE_PORT
                        port to listen on for client (default: 54320)
  --version             show program's version number and exit
```

## Run

```powershell
$ py3stun.exe --debug
```

## Sample Output

```
2023-01-02 22:20:22,240 - pystun.get_nat_type - DEBUG - Do Test1
2023-01-02 22:20:22,240 - pystun.get_nat_type - DEBUG - Trying STUN host: stun.qq.com
2023-01-02 22:20:22,241 - pystun.stun_test - DEBUG - sendto: ('stun.qq.com', 3478)
2023-01-02 22:20:22,278 - pystun.stun_test - DEBUG - recvfrom: ('106.55.202.232', 3478)
2023-01-02 22:20:22,278 - pystun.get_nat_type - DEBUG - Result: {'Resp': True, 'ExternalIP': '111.187.111.117', 'ExternalPort': 32064, 'SourceIP': '106.55.202.232', 'SourcePort': 3478, 'ChangedIP': '106.55.201.252', 'ChangedPort': 8000}
2023-01-02 22:20:22,278 - pystun.get_nat_type - DEBUG - Do Test2
2023-01-02 22:20:22,279 - pystun.stun_test - DEBUG - sendto: ('stun.qq.com', 3478)
2023-01-02 22:20:24,290 - pystun.stun_test - DEBUG - sendto: ('stun.qq.com', 3478)
2023-01-02 22:20:26,295 - pystun.stun_test - DEBUG - sendto: ('stun.qq.com', 3478)
2023-01-02 22:20:28,308 - pystun.stun_test - DEBUG - sendto: ('stun.qq.com', 3478)
2023-01-02 22:20:30,310 - pystun.get_nat_type - DEBUG - Result: {'Resp': False, 'ExternalIP': None, 'ExternalPort': None, 'SourceIP': None, 'SourcePort': None, 'ChangedIP': None, 'ChangedPort': None}
2023-01-02 22:20:30,310 - pystun.get_nat_type - DEBUG - Do Test1
2023-01-02 22:20:30,310 - pystun.stun_test - DEBUG - sendto: ('106.55.201.252', 8000)
2023-01-02 22:20:30,348 - pystun.stun_test - DEBUG - recvfrom: ('106.55.201.252', 8000)
2023-01-02 22:20:30,348 - pystun.get_nat_type - DEBUG - Result: {'Resp': True, 'ExternalIP': '111.187.111.117', 'ExternalPort': 32065, 'SourceIP': '106.55.201.252', 'SourcePort': 8000, 'ChangedIP': '106.55.202.232', 'ChangedPort': 3478}
NAT Type: Symmetric NAT
External IP: 111.187.111.117
External Port: 32065
```