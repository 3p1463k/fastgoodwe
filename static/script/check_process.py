import os

import psutil


def process_check():
    """Check wheter process not running"""

    with open("static/data/pid", "r") as pidfile:

        old_pid = pidfile.readlines()[0]
        pidfile.close()

    """Get current pid"""

    new_pid = os.getpid()
    compare = new_pid == old_pid

    print(f" Process ID: \n old {old_pid} \n new {new_pid} \n PID's equal: {compare} ")

    #
    # try:
    #     old_process = psutil.Process(int(old_pid))
    #
    #     if old_process.status() in ["sleeping","running"]:
    #
    #         """Kill process if running"""
    #
    #         old_process.kill()
    #         print(f" Killing {old_pid} continue... ")
    #
    #         """Write current pid to file"""
    #
    #         with open("data/pid","w") as pid_file:
    #             pid_file.write(str(new_pid))
    #             pid_file.close()
    #             print(f" Writing new pid {new_pid} to a file {pid_file.name} ")
    #
    # except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
    #     pass
