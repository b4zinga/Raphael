# author: myc

from lib.report import Report
from lib.threads import run_threads
from lib.data import task_queue, output_queue, user_args, logger


def _run_task():
    while not task_queue.empty():
        target, module = task_queue.get()
        try:
            print("\r\ttasks: {:10}\r".format(task_queue.qsize(),), end="", flush=True)
            ret = module.run(target, **user_args)
            if ret:
                logger.info("[+] {} -> {} -> {}".format(target, module.__name__, ret))
                output_queue.put((target, module.__name__, ret))
        except Exception as err:
            if user_args.get("error"):
                logger.error("{} -> {}  -> {}".format(target, module.__name__, err))


def _output_result(report_name, fmt):
    report_dir = user_args.pop('output')
    report_path = "{}/{}.{}".format(report_dir, report_name, fmt)
    logger.info("report path: {}".format(report_path))
    report = Report()
    report.build_report(output_queue, fmt)
    report.save_report(report_path)


def start():
    task_count = task_queue.qsize()
    logger.info("raphael got total {} tasks".format(task_count))
    try:
        thread_num = user_args.pop('thread')
        logger.info("run task in {} threads".format(thread_num))
        run_threads(thread_num, _run_task)
    except Exception as err:
        logger.error(err)
    finally:
        report_fmt = user_args.pop('format')
        logger.info("total {} result".format(output_queue.qsize()))
        _output_result("raphael", report_fmt)
