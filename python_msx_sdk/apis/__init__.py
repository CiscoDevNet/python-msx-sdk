
# flake8: noqa

# Import all APIs into this package.
# If you have many APIs here with many many models used in each API this may
# raise a `RecursionError`.
# In order to avoid this, import only the API that you directly need like:
#
#   from .api.auditing_generic_events_api import AuditingGenericEventsApi
#
# or import this package, but before doing it, use:
#
#   import sys
#   sys.setrecursionlimit(n)

# Import APIs into API package:
from python_msx_sdk.api.auditing_generic_events_api import AuditingGenericEventsApi
from python_msx_sdk.api.device_templates_api import DeviceTemplatesApi
from python_msx_sdk.api.devices_api import DevicesApi
from python_msx_sdk.api.health_api import HealthApi
from python_msx_sdk.api.offers_api import OffersApi
from python_msx_sdk.api.products_api import ProductsApi
from python_msx_sdk.api.roles_api import RolesApi
from python_msx_sdk.api.security_api import SecurityApi
from python_msx_sdk.api.services_api import ServicesApi
from python_msx_sdk.api.sites_api import SitesApi
from python_msx_sdk.api.tenants_api import TenantsApi
from python_msx_sdk.api.users_api import UsersApi
from python_msx_sdk.api.workflow_categories_api import WorkflowCategoriesApi
from python_msx_sdk.api.workflow_events_api import WorkflowEventsApi
from python_msx_sdk.api.workflow_instances_api import WorkflowInstancesApi
from python_msx_sdk.api.workflow_schemas_api import WorkflowSchemasApi
from python_msx_sdk.api.workflow_targets_api import WorkflowTargetsApi
from python_msx_sdk.api.workflows_api import WorkflowsApi
