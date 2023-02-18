---
date: 2023-02-06
---
# GGS Web Service

## response JSON

```json
{
   "dataTotalCount": 3,
   "result": "OK",
   "errorCode": "",
   "errorMessage": "",
   "endTime": "2023/02/03 17:01:59,661",
   "data": [...]
}
```

## data

**案１**

```json
[
  {
    "Node ID of the basic substance": "456",
    "Classification Code of the material": "1.1",
    "Substance Application ID": "46",
    "Percentage Max": "0.100000",
    "Percentage Min": "-1.000000"
  },
  {
    "Node ID of the basic substance": "456",
    "Classification Code of the material": "1.1.1",
    "Substance Application ID": "46",
    "Percentage Max": "0.100000",
    "Percentage Min": "-1.000000"
  },
  {
    "Node ID of the basic substance": "456",
    "Classification Code of the material": "1.1.2",
    "Substance Application ID": "46",
    "Percentage Max": "0.100000",
    "Percentage Min": "-1.000000"
  }
]
```

**案２**

```json
[
	["Node ID of the basic substance","Classification Code of the material","Substance Application ID","Percentage Max","Percentage Min"],
	["456","1.1","46","0.100000","-1.000000"],
	["456","1.1.1","46","0.100000","-1.000000"],
	["456","1.1.2","46","0.100000","-1.000000"]
]
```

MDS150 Performance
- server response time: 3.75s
- download: 4.82s

参考
- [【JavaScript】blocked by CORS policy エラーの簡単な解決法 | PisukeCode - Web開発まとめ](https://pisuke-code.com/js-blocked-by-cors-policy-error/)
- 