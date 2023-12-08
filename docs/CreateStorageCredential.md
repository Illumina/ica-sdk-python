# CreateStorageCredential


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the credentials | 
**type** | **str** | The type of the credentials | 
**aws_credentials** | [**AwsCredentials**](AwsCredentials.md) |  | [optional] 

## Example

```python
from icasdk.models.create_storage_credential import CreateStorageCredential

# TODO update the JSON string below
json = "{}"
# create an instance of CreateStorageCredential from a JSON string
create_storage_credential_instance = CreateStorageCredential.from_json(json)
# print the JSON string representation of the object
print CreateStorageCredential.to_json()

# convert the object into a dict
create_storage_credential_dict = create_storage_credential_instance.to_dict()
# create an instance of CreateStorageCredential from a dict
create_storage_credential_form_dict = create_storage_credential.from_dict(create_storage_credential_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


