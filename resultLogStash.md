docker@docker-Virtual-Machine:~/elk-csv/data$ curl -X GET "0.0.0.0:9200/csv-data/_search?q=*" | jq
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100  3123  100  3123    0     0   102k      0 --:--:-- --:--:-- --:--:--  105k
{
  "took": 23,
  "timed_out": false,
  "_shards": {
    "total": 1,
    "successful": 1,
    "skipped": 0,
    "failed": 0
  },
  "hits": {
    "total": {
      "value": 4173,
      "relation": "eq"
    },
    "max_score": 1.0,
    "hits": [
      {
        "_index": "csv-data",
        "_type": "_doc",
        "_id": "xINs25QBrwZecoARvMN_",
        "_score": 1.0,
        "_source": {
          "orderDate": "2014-06-02 10:16:51",
          "orderId": "1734",
          "location": {
            "lon": -74.972738,
            "lat": 29.262919
          },
          "orderPaymentType": "MULTINET",
          "orderGUID": "1e61b0e1-c693-4d17-93ff-dcd4f9b773ad",
          "orderPaymentAmount": "38.48"
        }
      },
      {
        "_index": "csv-data",
        "_type": "_doc",
        "_id": "xYNs25QBrwZecoARvMN_",
        "_score": 1.0,
        "_source": {
          "orderDate": "2014-12-17 03:10:25",
          "orderId": "1735",
          "location": {
            "lon": 34.892914,
            "lat": -82.70256
          },
          "orderPaymentType": "CASH",
          "orderGUID": "b6443076-21eb-4c7e-b7b9-7a25abe78e74",
          "orderPaymentAmount": "186.77"
        }
      },
      {
        "_index": "csv-data",
        "_type": "_doc",
        "_id": "xoNs25QBrwZecoARvMN_",
        "_score": 1.0,
        "_source": {
          "orderDate": "2020-02-21 11:42:28",
          "orderId": "1736",
          "location": {
            "lon": -93.693093,
            "lat": 73.673445
          },
          "orderPaymentType": "MULTINET",
          "orderGUID": "828efeb0-f545-474c-85f9-9e557020bb57",
          "orderPaymentAmount": "258"
        }
      },
      {
        "_index": "csv-data",
        "_type": "_doc",
        "_id": "x4Ns25QBrwZecoARvMN_",
        "_score": 1.0,
        "_source": {
          "orderDate": "2017-04-12 08:54:02",
          "orderId": "1737",
          "location": {
            "lon": -173.734906,
            "lat": -9.303806
          },
          "orderPaymentType": "CAD",
          "orderGUID": "f68cbf72-9a89-409b-8a7a-7928709d3bff",
          "orderPaymentAmount": "316.22"
        }
      },
      {
        "_index": "csv-data",
        "_type": "_doc",
        "_id": "yINs25QBrwZecoARvMN_",
        "_score": 1.0,
        "_source": {
          "orderDate": "2019-10-07 08:44:48",
          "orderId": "1738",
          "location": {
            "lon": 52.859234,
            "lat": 61.581247
          },
          "orderPaymentType": "EUR",
          "orderGUID": "6239c67d-f00f-4cfa-ae01-8f6ddc2647a9",
          "orderPaymentAmount": "303.51"
        }
      },
      {
        "_index": "csv-data",
        "_type": "_doc",
        "_id": "yYNs25QBrwZecoARvMN_",
        "_score": 1.0,
        "_source": {
          "orderDate": "2019-08-11 12:49:04",
          "orderId": "1739",
          "location": {
            "lon": -179.964455,
            "lat": 22.640022
          },
          "orderPaymentType": "SET_CARD",
          "orderGUID": "4cceed6c-3f64-4ab8-8ee9-3cc88e02cf43",
          "orderPaymentAmount": "280.23"
        }
      },
      {
        "_index": "csv-data",
        "_type": "_doc",
        "_id": "yoNs25QBrwZecoARvMN_",
        "_score": 1.0,
        "_source": {
          "orderDate": "2019-06-30 10:34:06",
          "orderId": "1740",
          "location": {
            "lon": -163.404567,
            "lat": 6.209494
          },
          "orderPaymentType": "CAD",
          "orderGUID": "d870f102-bf7b-4a67-ab99-aa7c98510199",
          "orderPaymentAmount": "304.33"
        }
      },
      {
        "_index": "csv-data",
        "_type": "_doc",
        "_id": "y4Ns25QBrwZecoARvMN_",
        "_score": 1.0,
        "_source": {
          "orderDate": "2017-11-14 03:00:16",
          "orderId": "1741",
          "location": {
            "lon": -158.112318,
            "lat": -84.138399
          },
          "orderPaymentType": "SET_CARD",
          "orderGUID": "0088e8fc-3893-45c8-8f95-ed89d162b992",
          "orderPaymentAmount": "34.16"
        }
      },
      {
        "_index": "csv-data",
        "_type": "_doc",
        "_id": "zINs25QBrwZecoARvMN_",
        "_score": 1.0,
        "_source": {
          "orderDate": "2016-11-30 06:48:33",
          "orderId": "1742",
          "location": {
            "lon": 61.903873,
            "lat": -15.868914
          },
          "orderPaymentType": "USD",
          "orderGUID": "bee43a55-7cf5-4b7d-b089-b7afa596b056",
          "orderPaymentAmount": "112.32"
        }
      },
      {
        "_index": "csv-data",
        "_type": "_doc",
        "_id": "zYNs25QBrwZecoARvMN_",
        "_score": 1.0,
        "_source": {
          "orderDate": "2016-09-20 10:12:03",
          "orderId": "1743",
          "location": {
            "lon": -83.047282,
            "lat": 67.380163
          },
          "orderPaymentType": "SODEXO",
          "orderGUID": "4c8171fb-5426-4cf3-84d0-f24e56b9adba",
          "orderPaymentAmount": "170.82"
        }
      }
    ]
  }
}