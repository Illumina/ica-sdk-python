# TempCredentials


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aws_temp_credentials** | [**AwsTempCredentials**](AwsTempCredentials.md) |  | [optional] 
**rclone_temp_credentials** | [**RcloneTempCredentials**](RcloneTempCredentials.md) |  | [optional] 

## Example

```python
from icasdk.models.temp_credentials import TempCredentials

# TODO update the JSON string below
json = "{}"
# create an instance of TempCredentials from a JSON string
temp_credentials_instance = TempCredentials.from_json(json)
# print the JSON string representation of the object
print TempCredentials.to_json()

# convert the object into a dict
temp_credentials_dict = temp_credentials_instance.to_dict()
# create an instance of TempCredentials from a dict
temp_credentials_form_dict = temp_credentials.from_dict(temp_credentials_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


