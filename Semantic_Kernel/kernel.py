import os
import asyncio
from os.path import dirname
from dotenv import load_dotenv
from semantic_kernel import Kernel
from semantic_kernel.connectors.ai.open_ai import AzureChatCompletion

current_dir = dirname(os.path.abspath(__file__))
root_dir = dirname(dirname(current_dir))
env_file=os.path.join(root_dir, ".env")

def define_kernel() :
    krnl = Kernel()
    return krnl

def config_azure() :
    load_dotenv(env_file)
    deployment_name = os.environ["OPENAI_AZURE_DEPLOYMENT_NAME"]
    end_point = os.environ["OPENAI_AZURE_ENDPOINT"]
    API_KEY = os.environ["OPENAI_AZURE_API_KEY"]
    return deployment_name, end_point, API_KEY


def kernel_with_azure_chat_service() :
    kr = define_kernel()
    deployment_name,end_point, API_KEY = config_azure()
    kr.add_service(AzureChatCompletion(
        deployment_name=deployment_name,
        endpoint=end_point,
        api_key=API_KEY
    ))
    return kr

def kernel_prompt() :  
    kernel= kernel_with_azure_chat_service() 
    response = kernel.invoke_prompt(
     "Give me detailed implementation process to create a test automation ai agent for Playwright python using semantic kernel in python code. AI agent should be able to perform Self Healing")
    print("Assistant > " + str(response))      
    return response;

async def main() :
    prompt = kernel_prompt()
    print(prompt)


if __name__ == "__main__":

    asyncio.run(main())
