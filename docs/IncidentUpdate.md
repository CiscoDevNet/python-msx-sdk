# IncidentUpdate


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | 
**attributes** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** |  | [optional] 
**category** | **str** | inquiry|software|hardware|network|database | [optional]  if omitted the server will use the default value of "inquiry"
**impact** | **str** |  | [optional]  if omitted the server will use the default value of "Low"
**priority** | **str** |  | [optional]  if omitted the server will use the default value of "Planning"
**severity** | **str** |  | [optional]  if omitted the server will use the default value of "Low"
**state** | **str** |  | [optional]  if omitted the server will use the default value of "New"
**subcategory** | **str** |  | [optional] 
**tenant** | **str, none_type** |  | [optional] 
**urgency** | **str** |  | [optional]  if omitted the server will use the default value of "Low"

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


