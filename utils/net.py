# author: myc

import re


def ip2num(ip):
    ips = [int(i) for i in ip.split('.')]
    return ips[0] << 24 | ips[1] << 16 | ips[2] << 8 | ips[3]


def num2ip(num):
    return '{}.{}.{}.{}'.format((num >> 24) & 0xff, (num >> 16) & 0xff, (num >> 8) & 0xff, num & 0xff)


def to_ips(raw):
    if '/' in raw and len(raw.split('.')) == 4 and raw.split('/')[1].isdigit():
        address, mask = raw.split('/')
        mask = int(mask)
        bin_addr = ''.join([(8 - len(bin(int(i))[2:])) * '0' + bin(int(i))[2:] for i in address.split('.')])
        start = bin_addr[:mask] + (32 - mask) * '0'
        end = bin_addr[:mask] + (32 - mask) * '1'
        bin_addrs = [(32 - len(bin(int(i))[2:])) * '0' + bin(i)[2:] for i in range(int(start, 2), int(end, 2) + 1)]
        dec_addrs = ['.'.join([str(int(bin_addr[8 * i:8 * (i + 1)], 2)) for i in range(0, 4)]) for bin_addr in
                     bin_addrs]
        return dec_addrs
    elif '-' in raw:
        if re.match(r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}-\d{1,3}$', raw):
            address, end = raw.split('-')
            end = int(end)
            start = int(address.split('.')[3])
            prefix = '.'.join(address.split('.')[:-1])
            return [prefix + '.' + str(i) for i in range(start, end + 1)]
        elif re.match(r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}-\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$', raw):
            start, end = [ip2num(x) for x in raw.split('-')]
            return [num2ip(num) for num in range(start, end + 1) if num & 0xff]
        else:
            return [raw]
    else:
        return [re.match(r'(https?://)?\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}(:\d{1,5})?', raw).group()]


def to_ports(raw):
    if "all" == raw:
        return [port for port in range(1, 65536)]
    elif "-" in raw:
        start, end = raw.split('-')
        try:
            return [port for port in range(int(start), int(end))]
        except:
            return []
    elif "," in raw:
        return [int(port) for port in raw.split(',')]
    else:
        return int(raw)
