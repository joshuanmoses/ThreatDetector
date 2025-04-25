from utils.logger import setup_logger

logger = setup_logger(__name__)

def analyze_movement(user_movements):
    unusual_paths = ["finance_db", "security_logs"]
    movement_score = sum(1 for loc in user_movements if loc in unusual_paths) / len(user_movements)
    
    if movement_score > 0.5:
        logger.info(f"Suspicious movement detected: {user_movements}")
        return True
    return False
