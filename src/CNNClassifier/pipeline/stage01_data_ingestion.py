from CNNClassifier.components.stage01_data_ingestion import DataIngestion
from CNNClassifier.config import ConfigurationManager
from CNNClassifier import logger

# create obj for  configurationmanager


logger.info(f"data ingestion stage started")
config = ConfigurationManager()
data_ingestion_config = config.get_data_ingestion_config()

# create object for dataingestion class
data_ingestion = DataIngestion(config=data_ingestion_config)

data_ingestion.download_file()

data_ingestion.unzip_and_clean()

logger.info(f"data ingestion stage completed")