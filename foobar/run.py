import sys
from hypercorn.config import Config
from hypercorn.run import run as hypercorn_run
import multiprocessing

def run():
    print("Hypercorn runner starting...")
    if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
        multiprocessing.freeze_support()

    config_obj = Config()
    config_obj.application_path = "foobar.app:app"
    exitcode = hypercorn_run(config_obj)

    print("Hypercorn runner stopped.")
    sys.exit(exitcode)


if __name__ == "__main__":
    run()