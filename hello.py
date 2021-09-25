from azureml.core import Workspace
from azureml.core.authentication import AzureCliAuthentication
cli_auth = AzureCliAuthentication()
ws = Workspace(subscription_id="2b044625-9119-453a-8f50-53426430883b",
               resource_group="testingApp",
               workspace_name="bhushan-workspace",auth=cli_auth)
# connect to your workspace
#ws = Workspace.from_config()
ws.write_config('.azureml')

Workspace.from_config()
#experiment_name = "get-started-with-jobsubmission-tutorial"
#exp = Experiment(workspace=ws, name=experiment_name)

print(ws)
