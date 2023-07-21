# Imports the Google Cloud client library
from google.cloud import logging

# Instantiates a client
logging_client = logging.Client()


credits_logger = logging_client.logger("credits_logs")
third_party_apis_logger = logging_client.logger("third_party_apis_logs")
internal_services_logger = logging_client.logger("internal_services_logs")


def log_credits(credits):
    """Log credits"""
    credits_logger.log_text(f"credits: {credits}")


def log_third_party_apis(api_name, api_url, api_response):
    """Log third party API calls"""
    third_party_apis_logger.log_text(
        f"api_name: {api_name}, api_url: {api_url}, api_response: {api_response}"
    )


def log_internal_services(service_name, service_url, error):
    """Log internal service calls"""
    internal_services_logger.log_text(
        f"service_name: {service_name}, service_url: {service_url}, error: {error}"
    )
