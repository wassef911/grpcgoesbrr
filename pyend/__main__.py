import logging
from pyend.app import App
from pyend.ml import HighlySophisticatedModel
import sys

logging.basicConfig(stream=sys.stdout, level=logging.INFO)
logger = logging.getLogger(__name__)

if __name__ == "__main__":
    app = App(fraud_model=HighlySophisticatedModel("path/to/model.pkl"))
    try:
        app.run()
    except Exception as exc:
        logger.error(f"Error: {exc}")
        app.stop()
