import os
from autogen import AssistantAgent, UserProxyAgent, config_list_from_json
import google.auth

def setup_gemini_config():
    """Set up Gemini configuration with Google Cloud credentials"""
    try:
        # Get default credentials from environment
        credentials, project_id = google.auth.default(
            scopes=["https://www.googleapis.com/auth/cloud-platform"]
        )
        
        # Basic Gemini configuration
        gemini_config = {
            "model": "gemini-pro",
            "api_type": "google",
            "project_id": project_id,
            "credentials": credentials,
            "location": "us-west1",
            "temperature": 0.7,
        }
        
        # Vision model configuration
        gemini_vision_config = {
            "model": "gemini-pro-vision",
            "api_type": "google",
            "project_id": project_id,
            "credentials": credentials,
            "location": "us-west1",
            "temperature": 0.7,
        }
        
        return [gemini_config, gemini_vision_config]
    except Exception as e:
        print(f"Error setting up Gemini configuration: {e}")
        return None

def create_gemini_agent(name="gemini_assistant", seed=42):
    """Create an AG2 assistant agent using Gemini"""
    config_list = setup_gemini_config()
    if not config_list:
        raise RuntimeError("Failed to set up Gemini configuration")
    
    return AssistantAgent(
        name=name,
        llm_config={
            "config_list": config_list,
            "seed": seed,
            "request_timeout": 120,
            "temperature": 0.7,
        },
        max_consecutive_auto_reply=3,
        system_message="You are a helpful AI assistant powered by Gemini. You help users with their tasks and can write code when needed."
    )

def create_user_proxy(work_dir="workspace"):
    """Create a user proxy agent for interaction"""
    return UserProxyAgent(
        "user_proxy",
        code_execution_config={
            "work_dir": work_dir,
            "use_docker": False,
            "timeout": 60,
        },
        human_input_mode="NEVER",
        max_consecutive_auto_reply=10,
        is_termination_msg=lambda x: "TERMINATE" in str(x.get("content", ""))
    )