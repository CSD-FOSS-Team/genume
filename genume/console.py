from genume.logging.logger import init as initLogger
from genume.extract import extract
from genume.genume import main


def console_entry():
    initLogger()
    extract()
    main()
