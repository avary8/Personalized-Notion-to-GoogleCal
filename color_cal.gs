//orig code https://www.linkedin.com/pulse/automate-color-coding-your-google-calendar-marguerite-thibodeaux-acc/?trk=articles_directory

function ColorEvents() {
 
  var today = new Date('January 1, 1999');
  var nextYear = new Date('December 31, 2200');

  Logger.log(today + " " + nextYear);
 
  var calendars = CalendarApp.getAllOwnedCalendars();
  Logger.log("found number of calendars: " + calendars.length);
 
  for (var i=0; i<calendars.length; i++) {
    var calendar = calendars[i];
    var events = calendar.getEvents(today, nextYear);

    for (var j=0; j<events.length; j++) {
      var e = events[j];
      var title = e.getTitle();
      var description = e.getDescription();
      
     if (title.includes("NLP")) {
        e.setColor(CalendarApp.EventColor.MAUVE);
        //e.setColor(CalendarApp.Color.PURPLE);
      }
     if (title.includes("enc3246")) {
       e.setColor(CalendarApp.EventColor.ORANGE);
       //e.setColor(CalendarApp.Color.RED-ORANGE);
      } 
      if (title.includes("cda3101")) {
        e.setColor(CalendarApp.EventColor.YELLOW);
      }
     if (title.includes("sta3032")) {
       e.setColor(CalendarApp.EventColor.PALE_BLUE);
      } 
      if (title.includes("cap3027")) {
       e.setColor(CalendarApp.EventColor.PALE_GREEN);
       //e.setColor(CalendarApp.Color.TEAL);
       //e.setColor("#38761d")
      } 
      if (title.includes("~")) {
        e.setColor(CalendarApp.EventColor.GRAY);
      }
    }
  }
}
