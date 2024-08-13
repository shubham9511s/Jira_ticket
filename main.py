from flask import Flask, request
from jira import JIRA

app = Flask(__name__)

# Jira configuration
jira_server = 'https://shubhamssc100-1715762728729.atlassian.net/'
jira_username = 'shubhamssc100-1715762728729'
jira_password = "ATATT3xFfGF0q-M7AORRo20mT7cjLAz4gNuDNe9Ds7Odp0ovPHOhdDgDJj3a-oAtVnuSFz8LdsvJWPx3okIu2ZoIYPMoIEO9z_OvtAuXtTXDkKySB3EftHe9H-rIll7-uS5B73gfhqfaTzj54CXxPIFtHI6Y-KUZtv3Kre4LmaMGAwJDBctNf2g=4194182A"
jira_project_key = 'KAN'
jira = JIRA(server=jira_server, basic_auth=(jira_username, jira_password))

@app.route('/jira', methods=['POST'])
def create_jira_ticket():
    data = request.json
    alerts = data.get('alerts', [])
    for alert in alerts:
        alertname = alert['labels'].get('alertname', 'Unknown Alert')
        summary = f"Alert: {alertname}"
        description = f"Alert details: {alert}"
        jira.create_issue(project=jira_project_key, summary=summary, description=description, issuetype={'name': 'Task'})
    return '', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
