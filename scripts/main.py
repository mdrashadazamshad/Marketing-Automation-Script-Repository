from utils import send_email, generate_report
import json

# Load config
with open("../config/config.json") as f:
    config = json.load(f)

def automate_campaign():
    print("Starting marketing automation...")

    # Example: send email to leads
    send_email(config["email"], "Welcome!", "Hello! Thank you for joining our campaign.")

    # Example: generate report
    report = generate_report()
    print("Generated report:", report)

if __name__ == "__main__":
    automate_campaign()
