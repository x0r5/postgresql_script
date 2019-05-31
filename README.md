# Database Deployment script

Functionality: from the attached .json file (sample.json) it can upload the data to the preferred (config.py) postgresql database.

### What you should create to use it:
```python
    #config.py
    USERNAME = ""
    PASSWORD = ""
    HOST = ""
    DBNAME = ""
```

Connection to db via terminal psql: 
```
    psql "sslmode=disable dbname=postgres user=postgres hostaddr=[public ip]"
```


#### sample.json example file
```json
{
  "slize_count": 0,
  "backup_id": "044568e3-7650-483f-aa2c-e3a577cd5e6e",
  "structure": [
    "next_step_id",
    "service",
    "datacenter",
    "alarmgroup",
    "name",
    "show_starting_relevant_to_start_time",
    "show_starting_relevant_to_escalation_start_time",
    "critical_at_relevant_to_start_time",
    "critical_at_relevant_to_escalation_start_time",
    "description",
    "url",
   "action_url",
    "show_starting_relevant_to_last_update",
    "status",
    "critical_at_relevant_to_last_update"
  ],
  "data": [
    [
      1,
      "BOC",
      null,
      null,
      "NOTNOW",
      0,
      null,
      5,
      null,
      "Assign Issue 1",
      null,
      null,
      null,
      null,
      null
    ],
    [
      2,
      "BOC",
      null,
      null,
      "NOTNOW",
      0,
      null,
      5,
      null,
      "Assign Issue 2",
      null,
      null,
      null,
      null,
      null
    ],[
      3,
      "BOC",
      null,
      null,
      "NOTNOW",
      0,
      null,
      5,
      null,
      "Assign Issue 3",
      null,
      null,
      null,
      null,
      null
    ],[
      4,
      "BOC",
      null,
      null,
      "NOTNOW",
      0,
      null,
      5,
      null,
      "Assign Issue 4",
      null,
      null,
      null,
      null,
      null
    ],[
      5,
      "BOC",
      null,
      null,
      "NOTNOW",
      0,
      null,
      5,
      null,
      "Assign Issue 5",
      null,
      null,
      null,
      null,
      null
    ]
  ]
}
```
