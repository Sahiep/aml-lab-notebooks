import os
from dotenv import load_dotenv
from azure.common.credentials import ServicePrincipalCredentials
from azure.mgmt.resource import ResourceManagementClient
from azure.mgmt.storage import StorageManagementClient
from azure.mgmt.storage.models import StorageAccountCreateParameters, SkuName, Sku, Kind
from azureml.core import Workspace
from azureml.core.authentication import ServicePrincipalAuthentication

# Load Environment configuration
load_dotenv()

# Load data for Azure Authentication
subscription_id = os.environ["subscription_id"]
client_id = os.environ["client_id"]
secret = os.environ["secret"]
tenant = os.environ["tenant"]

# Variable configuration
    # Resource Group Configuration
resource_group           = os.environ["resource_group"]
location                 = os.environ["location"]
storage_account_name     = os.environ["storage_account_name"]
container_registry_name  = os.environ["container_registry_name"]
key_vault_name           = os.environ["key_vault_name"]
app_insights_name        = os.environ["app_insights_name"]
workspace_name           = os.environ["workspace_name"]


# Create Azure Credential object
credentials = ServicePrincipalCredentials(
    client_id= client_id,
    secret=secret,
    tenant=tenant
)

client = ResourceManagementClient(credentials, subscription_id)

# Create Resource Group
resource_group_param = {"location" : location}
client.resource_groups.create_or_update(resource_group, resource_group_param)


# Create Azure Storage Account
storage_account_param =  StorageAccountCreateParameters(sku=Sku(name=SkuName.standard_ragrs), kind=Kind.storage,location = location)
storage_client = StorageManagementClient(credentials, subscription_id)
storage_async_operation = storage_client.storage_accounts.create(resource_group, storage_account_name, storage_account_param)
storage_account = storage_async_operation.result()

# Create Azure Keyvault
key_vault_params = {
    'location': location,
    'properties':  {
        'sku': {'family': 'A', 'name': 'standard'},
        'tenantId': tenant,
        'accessPolicies': [],
        'enabledForDeployment': True,
        'enabledForTemplateDeployment': True,
        'enabledForDiskEncryption': True
    }
}
key_vault_async_operation = client.resources.create_or_update(resource_group_name = resource_group,
                                  resource_provider_namespace = 'Microsoft.KeyVault',
                                  parent_resource_path = '',
                                  resource_type = 'vaults',
                                  resource_name = key_vault_name,
                                  api_version = '2015-06-01',
                                  parameters = key_vault_params)
key_vault = key_vault_async_operation.result()

# Create Azure Application Insights
app_insights_params = {
    'location' : location,
    'kind' : 'web',
    'properties' : {
        'Application_Type' : 'web'
    }
}
app_insights_async_operation = client.resources.create_or_update(resource_group_name = resource_group,
                                  resource_provider_namespace = 'Microsoft.Insights',
                                  parent_resource_path = '',
                                  resource_type = 'components',
                                  resource_name = app_insights_name,
                                  api_version = '2015-05-01',
                                  parameters = app_insights_params)
app_insights = app_insights_async_operation.result()


auth = ServicePrincipalAuthentication(tenant, client_id, secret, cloud='AzureCloud', _enable_caching=True) if tenant and client_id and secret else None

ws = Workspace.create(name = workspace_name,
                      auth = auth,
                      subscription_id = subscription_id,
                      resource_group = resource_group,
                      create_resource_group = True,
                      location = location,
                      storage_account = storage_account.id,
                      key_vault = key_vault.id,
                      app_insights = app_insights.id
                     )