""" Running the Xetra ETL Application """

import logging
import logging.config  
import yaml

def main():
    """
    Entry point to run the xetra ETL job
    
    """

    # Parsing YAML file
    config_path = '/home/damola/Documents/xetra_project/xetra_stocks/configs/xetra-report1-config.yaml'
    config = yaml.safe_load(open(config_path))
    # configure logging
    log_config = config['logging']
    logging.config.dictConfig(log_config)
    logger = logging.getLogger(__name__)
    logger.info("This is a test.")
    

if __name__ == '__main__':
    main()