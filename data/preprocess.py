import pandas as pd

def preprocess_session_data(raw_data):
    df = pd.DataFrame(raw_data)
    df['duration'] = df['end_time'] - df['start_time']
    features = df[['duration', 'command_count', 'resource_accessed_count']]
    return features

