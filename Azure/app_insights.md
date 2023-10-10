# Application Insights

* [Kusto Tutorial](https://docs.microsoft.com/en-us/azure/data-explorer/kusto/query/tutorial?pivots=azuredataexplorer)
* [Kusto Strings](https://docs.microsoft.com/en-us/azure/data-explorer/kusto/query/datatypes-string-operators)

## Dev Dashboard

**Frontend Errors Count**
```kusto
exceptions
| order by client_Type asc
| where timestamp > ago(31d)
| where client_Type == 'Browser' 
| project timestamp, operation_Name, outerMessage
| summarize _count=count(outerMessage) by outerMessage
| order by _count
;
```

**Frontend Errors**
```kusto
exceptions
| order by client_Type asc
| where timestamp > ago(31d)
| where client_Type == 'Browser' 
| project timestamp, errMsg=tostring(outerMessage)
| where errMsg!=""
;
```

**Frontend Errors Pie Chart**
```kusto
exceptions
| order by client_Type asc
| where timestamp > ago(31d)
| where client_Type == 'Browser' 
| project client_Type, ['type'], errMsg=outerMessage
| where errMsg!=""
| summarize _count=count(errMsg) by tostring(errMsg)
| order by _count
| render piechart 
;
```

## Backend

**Backend Errors Count**
```kusto
exceptions
| order by client_Type asc
| where timestamp > ago(31d)
| where client_Type == 'PC' 
| project client_Type, ['type'], errMsg=tostring(split(outerMessage, "\n")[-1])
| where errMsg!=""
| summarize _count=count(errMsg) by errMsg
| order by _count
;
```

**Backend Errors**
```kusto
exceptions
| order by client_Type asc
| where timestamp > ago(31d)
| where client_Type == 'PC' 
| project timestamp, ['type'], errMsg=tostring(split(outerMessage, "\n")[-1])
| where errMsg!=""
;
```

**Backend Errors Pie Chart**
```kusto
exceptions
| order by client_Type asc
| where timestamp > ago(31d)
| where client_Type == 'PC' 
| project client_Type, ['type'], errMsg=tostring(split(outerMessage, "\n")[-1])
| where errMsg!=""
| project errMsg=split(errMsg, 'Error:')[-1]
| summarize _count=count(errMsg) by tostring(errMsg)
| order by _count
| render piechart 
;
```

## BI Dashboard

**Unique Users**
```kusto
let events = dynamic(["*"]);
let grain = iff(true, 1d, 1h);
let mainTable = union pageViews, customEvents, requests
    | where timestamp > ago(90d)
    | extend name =replace("\n", "", name)
    | where '*' in (events) or name in (events)
    | where true;
let resultTable = mainTable;
resultTable
| make-series Users = dcountif(user_Id, 'user_Id' != 'user_AuthenticatedId' or ('user_Id' == 'user_AuthenticatedId' and isnotempty(user_Id)))
    default = 0
    on timestamp
    from ago(90d) to now() step grain
| render columnchart  
```

**Page Visits**
```kusto
let events = dynamic(["*"]);
let filterByName = '';
let mainTable = union pageViews, customEvents, requests
    | where timestamp > ago(90d)
    | extend name =replace("\n", "", name)
    | where '*' in (events) or name in (events)
    | where true
    | where isempty(filterByName) or name contains filterByName;
let queryTable = mainTable; 
queryTable
| summarize arg_max(timestamp, itemId), Users=dcount(user_Id), Sessions = dcount(session_Id), Instances= count(), Item = any(itemId) by name, itemType
| extend rank = 2
| union (queryTable
    | summarize Users = dcount(user_Id), Sessions = dcount(session_Id), Instances = count(), Item = any(itemId)
    | extend name = 'Overall', rank = 1)
| extend jkey = 1
| join kind = inner (queryTable 
    | summarize AllUsers = dcount(user_Id), AllSessions = dcount(session_Id), AllInstances = count(), Item = any(itemId)
    | extend jkey = 1)
    on jkey 
| where isempty(filterByName) or name contains filterByName
| project ['Name'] = case(itemType == 'pageView', strcat('📄 ', name), itemType == 'customEvent', strcat('📅 ', name), itemType == 'request', strcat('💬 ', name), name), ['Users'] = Users,
    ['Sessions'] = Sessions,
    ['Count'] = Instances, rank
| order by rank asc, ['Users'] desc
| project-away rank
```

**Active Users**
```kusto
let ts = now() - ago(30d);
let start = startofday(ago(ts + 28d));
union customEvents, pageViews
| where timestamp >= start
| where name in ('*') or '*' in ('*') or ('%' in ('*') and itemType == 'pageView') or ('#' in ('*') and itemType == 'customEvent')
| where 'All events' == 'All events' or 'All events' == '🔸 Overall' or name == 'All events'
| evaluate activity_engagement(user_Id, timestamp, start, now(), 1d, 28d)
| where timestamp >= startofday(ago(ts))
| project timestamp, ["All events"] = dcount_activities_outer
| render areachart 
```

## Custom Events

```kusto
// Get all Lukasz's events
customEvents
| order by timestamp
| where name contains "Lukasz"
// | count
```

```kusto
// Count occurance of an event that happend in 1 hour
customEvents 
| summarize event_count=count() by bin(timestamp, 1h)
| render columnchart 
```

```kusto
// Count occurance of an event
customEvents
| summarize event_count=count(name) by name
```
