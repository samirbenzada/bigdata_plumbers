import requests
import json 

myheaders = {
   	"x-rapidapi-host": "free-nba.p.rapidapi.com",
	"x-rapidapi-key": "14a8b42a6cmshceb9a36e240a1cep1dc18ejsnf5536497b56e",
	"useQueryString": 'true'
}

post = {
	"name": "lss_application",
	"active": true,
	"prefixKey": "sf/lss",
	"sourceSchemaDb": "schemadb_raw",
	"sourceSchemaGlue": [{
			"name": "currencybase",
			"type": "string"
		},
		{
			"name": "cashvalue",
			"type": "string"
		},
		{
			"name": "divisoreod",
			"type": "double"
		},
		{
			"name": "id_index",
			"type": "string"
		},
		{
			"name": "currencyreturnmtdbase",
			"type": "double"
		},
		{
			"name": "returndailybase",
			"type": "string"
		},
		{
			"name": "date",
			"type": "string"
		},
		{
			"name": "indexdescription",
			"type": "string"
		},
		{
			"name": "system",
			"type": "string"
		},
		{
			"name": "year",
			"type": "string"
		},
		{
			"name": "month",
			"type": "string"
		},
		{
			"name": "day",
			"type": "string"
		}
	],
	"destinationSchemaDb": "schemadb",
	"destinationSchemaGlue": [{
			"name": "currencybase",
			"type": "string"
		},
		{
			"name": "cashvalue",
			"type": "string"
		},
		{
			"name": "divisoreod",
			"type": "double"
		},
		{
			"name": "id_index",
			"type": "string"
		},
		{
			"name": "currencyreturnmtdbase",
			"type": "double"
		},
		{
			"name": "returndailybase",
			"type": "string"
		},
		{
			"name": "date",
			"type": "string"
		},
		{
			"name": "indexdescription",
			"type": "string"
		},
		{
			"name": "system",
			"type": "string"
		},
		{
			"name": "year",
			"type": "string"
		},
		{
			"name": "month",
			"type": "string"
		},
		{
			"name": "day",
			"type": "string"
		},
		{
			"name": "edptimestamp",
			"type": "string"
		}
	],
	"dataQuality": {
		"className": "com.idata.edl.dataquality.DataQualityCheck",
		"file": "s3://idata-config/spark/edl-dataquality-assembly-0.1.jar",
		"sourceFileAttributes": {
			"type": "csv",
			"delimiter": "|",
			"header": true
		},
		"destinationFileAttributes": {
			"type": "csv",
			"delimiter": "|",
			"header": true
		},
		"rules": {
			...
		}
	},
	"transform": {
		"className": "com.idata.edl.csvtoparquet.CsvToParquet",
		"file": "s3://idata-config/spark/edl-csvtoparquet-assembly-0.1.jar",
		"sourceFileAttributes": {
			"type": "csv",
			"delimiter": "|",
			"header": true
		},
		"keyFields": ["id", "index"],
		"partitionBy": ["date"],
		"useDelta": true,
		"useHudi": false
	}
}


requests.post('https://free-nba.p.rapidapi.com/stats', headers=myheaders)

# x= requests.get('https://free-nba.p.rapidapi.com/stats', headers=myheaders)
# t = x.json()
# print(t)