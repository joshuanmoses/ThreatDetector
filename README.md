<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Threat Detector</title>
</head>
<body>

<h1>Threat Detector</h1>

<blockquote><em>An AI-powered cybersecurity system that uses machine learning and LLMs to detect, report, and respond to suspicious network activities in real-time.</em></blockquote>

<hr>

<h2>🚀 Project Overview</h2>

<p>Threat Detector is an advanced, modular platform that continuously monitors network session data, user behavior, delegation risks, and command patterns to detect potential cyber threats.<br>
Upon detecting a threat, it automatically generates a natural-language incident report via GPT and alerts the security team via email, while optionally taking mitigation actions such as account lockout or session termination.</p>

<p>This project combines:</p>
<ul>
  <li>Machine Learning (Isolation Forest) for anomaly detection</li>
  <li>LLM/GPT integration for automated threat report generation</li>
  <li>Automated real-time alerting and mitigation</li>
  <li>Full Docker containerization for easy deployment</li>
</ul>

<hr>

<h2>⚡ Features</h2>

<ul>
  <li>Detects threats based on <strong>user movement patterns</strong> across network resources</li>
  <li>Monitors <strong>session duration</strong> and <strong>command volume</strong> for abnormal behavior</li>
  <li>Identifies <strong>delegated accounts</strong> that are at high risk</li>
  <li>Automatically <strong>generates professional incident reports</strong> using GPT</li>
  <li>Sends <strong>real-time email alerts</strong> to SOC/security teams</li>
  <li>Supports <strong>automated mitigation</strong> actions</li>
  <li>Modular and <strong>easily extendable</strong> design</li>
  <li><strong>Dockerized</strong> for fast setup and deployment</li>
</ul>

<hr>

<h2>📂 Folder Structure</h2>

<pre><code>
network_threat_detector/
├── config/            # App settings (email, thresholds, model parameters)
├── data/              # Data preprocessing scripts
├── models/            # ML and LLM models
├── monitoring/        # Monitoring modules for sessions, delegation, movement
├── responders/        # Alerting and threat mitigation modules
├── utils/             # Logger and email helpers
├── app.py             # Main orchestrator
├── Dockerfile         # Docker build file
├── docker-compose.yml # Docker Compose config
├── requirements.txt   # Python dependencies
└── README.md          # Project documentation
</code></pre>

<hr>

<h2>🛠 Installation</h2>

<p>Clone the repository:</p>

<pre><code>git clone https://github.com/yourusername/network_threat_detector.git
cd network_threat_detector
</code></pre>

<p>Install dependencies:</p>

<pre><code>pip install -r requirements.txt
</code></pre>

<hr>

<h2>🐳 Docker Deployment</h2>

<p>Build and run using Docker Compose:</p>

<pre><code>docker-compose up --build
</code></pre>

<p>Run in detached mode:</p>

<pre><code>docker-compose up --build -d
</code></pre>

<hr>

<h2>⚙️ Configuration</h2>

<p>Modify settings in <code>config/settings.py</code>:</p>

<ul>
  <li>SMTP server settings for email alerts</li>
  <li>Threat scoring thresholds</li>
  <li>LLM model settings (e.g., GPT-3.5, GPT-4)</li>
  <li>API keys (preferably use environment variables in production)</li>
</ul>

<p>Example <code>.env</code> setup (optional):</p>

<pre><code>
OPENAI_API_KEY=your_openai_key_here
EMAIL_USERNAME=your_email@example.com
EMAIL_PASSWORD=your_password
</code></pre>

<hr>

<h2>🧪 Running the Application</h2>

<p>Local development:</p>

<pre><code>python app.py
</code></pre>

<p>Docker:</p>

<pre><code>docker-compose up
</code></pre>

<p>The system will start monitoring synthetic session data (or your integrated live sources), detect anomalies, generate incident reports, and email them to the configured recipients.</p>

<hr>

<h2>📝 Example Output</h2>

<p>Example threat detection alert email:</p>

<pre><code>
Subject: Potential Cyber Threat Detected

Dear SOC Team,

A potential cyberattack was detected involving user 'user123'.

Summary:
- Session Duration: 5000 seconds
- Commands Executed: 120
- Movement Path: ['dev_server', 'finance_db', 'email_gateway']

Recommended Actions:
- Immediate session review
- Possible account lockout
- Further investigation of accessed resources
</code></pre>

<hr>

<h2>📈 Future Improvements</h2>

<ul>
  <li>Integrate with SIEM platforms (Splunk, Elastic, Microsoft Sentinel)</li>
  <li>Build a web dashboard for real-time monitoring</li>
  <li>Expand LLM report generation with risk scoring and severity levels</li>
  <li>Train custom anomaly detection models for specific environments</li>
  <li>Add multi-tenant monitoring support</li>
</ul>

<hr>

<h2>📜 License</h2>

<p>MIT License.<br>
Feel free to fork, use, and contribute!</p>

<hr>

<h2>👨‍💻 Author</h2>

<ul>
  <li><a href="https://github.com/joshuanmoses">Joshua Moses</a> — AI & Threat Expert</li>
</ul>

</body>
</html>
