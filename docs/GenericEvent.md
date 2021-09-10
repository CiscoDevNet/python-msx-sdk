# GenericEvent


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**time** | **datetime** |  | [optional] 
**severity** | [**GenericEventSeverity**](GenericEventSeverity.md) |  | [optional] 
**subtype** | **str** |  | [optional] 
**service** | **str** | Service that generated the event | [optional] 
**keywords** | **str** | Space separated list of keywords to be used for search | [optional] 
**details** | **{str: (str,)}** |  | [optional] 
**trace** | [**GenericEventTrace**](GenericEventTrace.md) |  | [optional] 
**security** | [**GenericEventSecurity**](GenericEventSecurity.md) |  | [optional] 
**description** | **str** |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


