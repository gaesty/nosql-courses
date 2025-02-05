GET receipe/_search
{
  "query": {
    "match_all": {}
  }
}

GET receipe/_search
{
  "query": {
    "range": {
      "preparation_time_minutes": {
        "gte": 60
      }
    }
  }
}

GET receipe/_search
{
  "query": {
    "match": {
      "ingredients.name": "sugar"
    }
  }
}

