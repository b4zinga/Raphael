# author: myc

import os
import re
import sys

from utils.net import to_ips, to_ports
from utils.file import read_dict
from lib.patch import patch_requests
from lib.cmdline import cmdline_parser
from lib.data import task_queue, user_args, logger, pl


def _set_targets(raw):
    targets = []
    if os.path.isfile(raw):  # file
        logger.info("read targets from: {}".format(raw))
        targets.extend(read_dict(raw, strict=True))
    elif re.match("[A-Za-z]+", raw):  # domain
        logger.info("set target: {}".format(raw))
        targets.append(raw)
    else:  # ip or cidr
        logger.info("convert ip segment into ip address")
        targets.extend(to_ips(raw))
    logger.debug("targets: {}".format(targets))
    return targets


def _prepare_user_args():
    if user_args.pop("list"):
        plugins = pl.find_plugin()
        logger.info("plugin path: {}\nAll Plugins:\n\t".format(pl.get_plugin_dir()) + "\n\t".join(plugins))
        sys.exit()

    if not user_args.get("host"):
        logger.error("need target or target file")
        sys.exit()
    user_args.update({"targets": user_args.pop("host")})

    if not user_args.get("plugin"):
        logger.error("need plugin keyword")
        sys.exit()

    if user_args.get("port"):
        user_args.update({"port": to_ports(user_args.get("port"))})


def _set_task_queue():
    targets = _set_targets(user_args.pop("targets"))
    modules = pl.load_plugin(keyword=user_args.pop("plugin"))
    if not modules:
        logger.error("no suitable plugin found")
        sys.exit()
    module_name = "".join("\n\t" + m.__name__ for m in modules)
    logger.info("found {} plugin: {}".format(len(modules), module_name))
    for target in targets:
        for module in modules:
            task_queue.put((target, module))


def init():
    user_args.update(cmdline_parser().__dict__)
    logger.debug(user_args)
    _prepare_user_args()
    _set_task_queue()
    patch_requests()
