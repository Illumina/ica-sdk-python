# Introduction to ICA Python SDK

### Areas Covered
- Installation and Authentication
- Projects
- Project Data
- Project Pipelines
- Project Analysis


### Installation and Authentication
#### How to download and install ICA Python SDK
You can access the git repository for the ICA Python SDK at the following link [Illumina Git](https://github.com/Illumina)

**Install using pip**
``` bash
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run pip with root permission: sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git)
Then import the package:

``` bash
import icasdk
```

**Install using Setuptools**
``` python
python setup.py install --user
```
```
sudo python setup.py install
```
Then import the pacakage:
``` bash
import icasdk
```

#### How to generate a JWT token using APIKEY or Username/Password

After install the SDK and confirming the package is imported you can use the APIKEY from platform authentication to generate a JWT
Adapted from [Link to TokenApi](https://git.illumina.com/SEES/ica-sdk-python/blob/main/docs/apis/tags/TokenApi.md)

Via APIKEY
``` python
import icasdk
from icasdk.apis.tags import token_api
from icasdk.model.token import Token
from icasdk.model.problem import Problem
from pprint import pprint

# Defining the host is optional and defaults to /ica/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = icasdk.Configuration(host="https://ica.illumina.com/ica/rest")

# Configure API key authorization: ApiKeyAuth
configuration.api_key["ApiKeyAuth"] = "APIKEY"

# Enter a context with an instance of the API client
with icasdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = token_api.TokenApi(api_client)

    # example passing only optional values
    query_params = {
        "tenant": "TENANT",
    }
    try:
        # Generate a JWT using an API-key, Basic Authentication or a psToken.
        api_response = api_instance.create_jwt_token(
            query_params=query_params,
        )
        pprint(api_response)
        jwt = api_response.body["token"]
    except icasdk.ApiException as e:
        print("Exception when calling TokenApi->create_jwt_token: %s\n" % e)
```
Via Username and Password
``` python
import icasdk
from icasdk.apis.tags import token_api
from icasdk.model.token import Token
from icasdk.model.problem import Problem
from pprint import pprint

# Defining the host is optional and defaults to /ica/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = icasdk.Configuration(host="https://ica.illumina.com/ica/rest")

# Configure HTTP basic authorization: BasicAuth
configuration.username = "USERNAME"
configuration.password = "PASSWORD"
configuration.access_token = None

# Enter a context with an instance of the API client
with icasdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = token_api.TokenApi(api_client)

    # example passing only optional values
    query_params = {
        "tenant": "TENANT",
    }
    try:
        # Generate a JWT using an API-key, Basic Authentication or a psToken.
        api_response = api_instance.create_jwt_token(
            query_params=query_params,
        )
        pprint(api_response)
        jwt = api_response.body["token"]
    except icasdk.ApiException as e:
        print("Exception when calling TokenApi->create_jwt_token: %s\n" % e)
```

### Projects
Adapted from [Link to ProjectApi](https://git.illumina.com/SEES/ica-sdk-python/blob/main/docs/apis/tags/ProjectApi.md)

#### How to create a new project
Required parameters to create a project via API request
- name (User Supplied String)
- storageBundleId (Explained below)
- billingMode( Only option is "Project")
- dataSharingEnabled (True or False)
- regionId (Based on desired ICA regions, explained below)

You can use the storageBunldeId API endpoint to grab both the storageBundleId and associated region, as seen below. Data sharing mode allows you to bundle data for cross-project or cross-tenant data sharing. 

``` python
import icasdk
from icasdk.apis.tags import project_api
from icasdk.model.create_project import CreateProject
from icasdk.model.project import Project
from icasdk.model.problem import Problem
from icasdk.apis.tags import storage_bundle_api
from icasdk.model.storage_bundle_list import StorageBundleList
from pprint import pprint

# Defining the host is optional and defaults to /ica/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = icasdk.Configuration(host="https://ica.illumina.com/ica/rest")

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key["ApiKeyAuth"] = "YOUR_API_KEY"

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with icasdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = storage_bundle_api.StorageBundleApi(api_client)
    try:
        # Retrieve a list of storage bundles.
        api_response = api_instance.get_storage_bundles()
        pprint(api_response)
        items = api_response.body["items"]
        for i in items:
            pprint(f"storageBundleName:Id={i.entitlementName}:{i.id}")
            pprint(f"regionName:Id={i.region.country.name}:{i.region.id}")
            storageId = i.id
            regionId = i.region.id

    except icasdk.ApiException as e:
        print("Exception when calling StorageBundleApi->get_storage_bundles: %s\n" % e)

    api_instance = project_api.ProjectApi(api_client)

    # example passing only optional values
    body = {
        "name": "ProjectTestName",
        "regionId": regionId,
        "billingMode": "PROJECT",
        "dataSharingEnabled": True,
        "storageBundleId": storageId,
    }
    try:
        # Create a new project.
        api_response = api_instance.create_project(
            body=body,
        )
        pprint(api_response)
    except icasdk.ApiException as e:
        print("Exception when calling ProjectApi->create_project: %s\n" % e)
```

#### How to list projects and find project ID
``` python
import icasdk
from icasdk.apis.tags import project_api
from icasdk.model.problem import Problem
from icasdk.model.project_paged_list import ProjectPagedList
from pprint import pprint
configuration = icasdk.Configuration(host="https://ica.illumina.com/ica/rest")

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key["ApiKeyAuth"] = "YOUR_API_KEY"

with icasdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = project_api.ProjectApi(api_client)

    # example passing only optional values
    query_params = {"pageSize": "50"}
    try:
        # Retrieve a list of projects.
        api_response = api_instance.get_projects(
            query_params=query_params,
        )
        pprint(api_response)
        for i in api_response.body["items"]:
            pprint(f"{i.name}:{i.id}")
    except icasdk.ApiException as e:
        print("Exception when calling ProjectApi->get_projects: %s\n" % e)

```



### Project Data
Adapated from [Project Data Api](https://git.illumina.com/SEES/ica-sdk-python/blob/main/docs/apis/tags/ProjectDataApi.md)
#### How to list data and search within a project
There are several options for how to search through folders and data using combinations of file paths, full text search, filePathMatchModes which can be case sensitive or insensitive
```python
import icasdk
from icasdk.apis.tags import project_data_api
from icasdk.model.project_data_paged_list import ProjectDataPagedList
from icasdk.model.problem import Problem
from pprint import pprint

# Defining the host is optional and defaults to /ica/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = icasdk.Configuration(host="https://ica.illumina.com/ica/rest")

# Configure API key authorization: ApiKeyAuth
configuration.api_key["ApiKeyAuth"] = "YOUR_API_KEY"

# Enter a context with an instance of the API client
with icasdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = project_data_api.ProjectDataApi(api_client)

    projectId = "e501a0d5-f5e7-458c-a590-586c79bb87e0"
    # example passing only required values which don't have defaults set
    path_params = {
        "projectId": projectId,
    }
    query_params = {}
    try:
        # Retrieve the list of project data.
        api_response = api_instance.get_project_data_list(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except icasdk.ApiException as e:
        print("Exception when calling ProjectDataApi->get_project_data_list: %s\n" % e)

    # example passing only optional values
    path_params = {
        "projectId": projectId,
    }
    query_params = {"fullText": ".gvcf", "pageSize": "100"}
    try:
        # Retrieve the list of project data.
        api_response = api_instance.get_project_data_list(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
        for i in api_response.body["items"]:
            print(
                f"{i.data.get_item_oapg('details').get_item_oapg('path')}/{i.data.get_item_oapg('details').name}"
            )
    except icasdk.ApiException as e:
        print("Exception when calling ProjectDataApi->get_project_data_list: %s\n" % e)

```

#### How to download a set of data from a project
Building on the previous code snippet of how to get a list of data from a project, you can create download URLs and download a list of files
```python
import icasdk
from icasdk.apis.tags import project_data_api
from icasdk.model.project_data_paged_list import ProjectDataPagedList
from icasdk.model.problem import Problem
from pprint import pprint

from icasdk.model.download import Download
import requests

# Defining the host is optional and defaults to /ica/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = icasdk.Configuration(host="https://ica.illumina.com/ica/rest")

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key["ApiKeyAuth"] = "YOUR_API_KEY"

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'


# Enter a context with an instance of the API client
with icasdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = project_data_api.ProjectDataApi(api_client)

    projectId = "e501a0d5-f5e7-458c-a590-586c79bb87e0"
    # example passing only required values which don't have defaults set
    path_params = {
        "projectId": projectId,
    }
    query_params = {}
    try:
        # Retrieve the list of project data.
        api_response = api_instance.get_project_data_list(
            path_params=path_params,
            query_params=query_params,
        )
        # pprint(api_response)
    except icasdk.ApiException as e:
        print("Exception when calling ProjectDataApi->get_project_data_list: %s\n" % e)

    # example passing only optional values
    path_params = {
        "projectId": projectId,
    }
    query_params = {"fullText": ".gvcf", "pageSize": "5"}
    try:
        # Retrieve the list of project data.
        api_response = api_instance.get_project_data_list(
            path_params=path_params,
            query_params=query_params,
        )
        # pprint(api_response)
        fileList = {}
        for i in api_response.body["items"]:
            # fileList[
            #     f"{i.data.get_item_oapg('details').get_item_oapg('path')}/{i.data.get_item_oapg('details').name}"
            # ] = i.data.get_item_oapg("id")
            fileList[i.data.get_item_oapg("id")] = {
                "path": i.data.get_item_oapg("details").get_item_oapg("path"),
                "name": i.data.get_item_oapg("details").name,
            }
            print(i.data.get_item_oapg("id"))
            print(
                f"{i.data.get_item_oapg('details').get_item_oapg('path')}/{i.data.get_item_oapg('details').name}"
            )
    except icasdk.ApiException as e:
        print("Exception when calling ProjectDataApi->get_project_data_list: %s\n" % e)

    try:
        # Retrieve a download URL for this data.
        for file in fileList:
            api_response = api_instance.create_download_url_for_data(
                path_params={
                    "projectId": projectId,
                    "dataId": file,
                }
            )
            # pprint(api_response)
            url = api_response.body["url"]
            pprint(url)
            response = requests.get(url)
            fileName = fileList[file]["name"]
            open(fileName, "wb").write(response.content)

    except icasdk.ApiException as e:
        print(
            "Exception when calling ProjectDataApi->create_download_url_for_data: %s\n"
            % e
        )

```


### Project Pipelines
How to upload a CWL pipeline

How to upload a Nextflow pipeline

How to retrieve input parameters for a pipeline

### Project Analysis
How to get the status of an analyses

How to launch a CWL pipeline

How to launch a Nextflow pipeline
