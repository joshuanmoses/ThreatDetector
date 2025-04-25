from monitoring.session_monitor import analyze_session
from monitoring.delegation_detector import detect_delegation
from monitoring.movement_analyzer import analyze_movement
from models.threat_detector import ThreatDetector
from models.gpt_report_generator import generate_threat_report
from responders.email_alert import alert_security
from responders.threat_mitigator import mitigate_threat
from config import settings
from utils.logger import setup_logger

logger = setup_logger(__name__)

def main():
    threat_model = ThreatDetector()
    threat_model.load_model("models/trained_threat_model.pkl")
    
    session_data = get_live_session_data()
    delegation_data = get_account_permission_data()
    movement_data = get_user_movement_data()
    
    if analyze_session(session_data) or detect_delegation(delegation_data) or analyze_movement(movement_data):
        features = [[session_data['duration'], session_data['command_count'], len(movement_data)]]
        scores, predictions = threat_model.predict(features)
        
        if predictions[0] == -1 or scores[0] < settings.THREAT_SCORE_THRESHOLD:
            incident_details = {
                "user_id": session_data['user_id'],
                "session_duration": session_data['end_time'] - session_data['start_time'],
                "commands_executed": session_data['command_count'],
                "movement_path": movement_data
            }
            report = generate_threat_report(incident_details)
            alert_security("Potential Cyber Threat Detected", report)
            mitigate_threat(session_data['user_id'])

def get_live_session_data():
    # Replace with real data collection from SIEM, logs, etc.
    return {
        "user_id": "user123",
        "start_time": 0,
        "end_time": 5000,
        "command_count": 120
    }

def get_account_permission_data():
    return {
        "user_id": "user123",
        "privileges": ["read", "write", "delegate"]
    }

def get_user_movement_data():
    return ["dev_server", "finance_db", "email_gateway"]

if __name__ == "__main__":
    main()
