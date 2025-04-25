from config import settings
from utils.logger import setup_logger

logger = setup_logger(__name__)

def analyze_session(session_data):
    duration = session_data['end_time'] - session_data['start_time']
    commands_executed = session_data['command_count']
    
    if duration > settings.SESSION_DURATION_THRESHOLD or commands_executed > settings.COMMAND_COUNT_THRESHOLD:
        logger.info(f"Anomalous session detected: {session_data['user_id']}")
        return True
    return False

