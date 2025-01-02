# Reminders to Clipboard
 A python program created to help me remind my class of the important stuff

## Configuration

This application requires a "config/config.json" to work, this json requires the following structure 

The message that comes before the schedule

```"scheduleMessage": [""]``` 

A header message for the reminders

```"headerMessage": ""```

A small text that comes before the reminders

```"remindersMessage": ""```

The path for the reminders json file

```"remindersJsonFilePath": "reminders.json"```

The path for a schedule in a .xlsx file 

```"scheduleXlsxFilePath": "schedule.xlsx"```

The columns letters equivalents of each day of the week, like in the example below 
```
"weekdayColumns": {
    
    "Sunday": null,
    "Monday": "B",
    "Tuesday": "C",
    "Wednesday": "D",
    "Thursday": "E",
    "Friday", "F",
    "Saturday": null
}
```