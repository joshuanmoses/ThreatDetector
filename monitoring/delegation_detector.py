from utils.logger import setup_logger

logger = setup_logger(__name__)

def detect_delegation(account_permissions):
    if "delegate" in account_permissions.get("privileges", []):
        logger.warning(f"Delegation risk detected: {account_permissions['user_id']}")
        return True
    return False
