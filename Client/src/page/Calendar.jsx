import React, { useState, useRef } from "react";
import FullCalendar from "@fullcalendar/react";
import dayGridPlugin from "@fullcalendar/daygrid";
import timeGridPlugin from "@fullcalendar/timegrid";
import interactionPlugin from "@fullcalendar/interaction";
import frLocale from "@fullcalendar/core/locales/fr";
import dayjs from "dayjs";
import FilterPanel from "../composant/filtrePanel";
import Events from "./Events";

const Calendar = () => {
  const [events, setEvents] = useState([
    { title: "Événement 1", date: "2024-11-12", category: "Emploi", location: "Paris" },
  ]);

  const [selectedCategories, setSelectedCategories] = useState([]);
  const [selectedLocation, setSelectedLocation] = useState("All");
  const [selectedMonth, setSelectedMonth] = useState(dayjs().format("YYYY-MM"));

  const calendarRef = useRef(null);

  const handleDateClick = (info) => {
    const title = prompt("Entrez le titre de l'événement:");
    const category = prompt("Entrez la catégorie de l'événement (Emploi, Travail) :");
    const location = prompt("Entrez le lieu de l'événement :");

    if (title && category && location) {
      setEvents([...events, { title, date: info.dateStr, category, location }]);
    }
  };

  const handleCategoryChange = (e) => {
    const { value, checked } = e.target;
    if (checked) {
      setSelectedCategories([...selectedCategories, value]);
    } else {
      setSelectedCategories(selectedCategories.filter((category) => category !== value));
    }
  };

  const handleLocationChange = (e) => {
    setSelectedLocation(e.target.value);
  };

  const handleMonthChange = (e) => {
    setSelectedMonth(e.target.value);

    const calendarApi = calendarRef.current.getApi();
    const selectedDate = dayjs(e.target.value).toDate();
    calendarApi.gotoDate(selectedDate);
  };

  const filteredEvents = events.filter((event) => {
    const isCategoryMatch = selectedCategories.length === 0 || selectedCategories.includes(event.category);
    const isLocationMatch = selectedLocation === "All" || event.location === selectedLocation;
    const isMonthMatch = dayjs(event.date).format("YYYY-MM") === selectedMonth;
    return isCategoryMatch && isLocationMatch && isMonthMatch;
  });

  // Fonction pour ajouter l'icône dans chaque événement
  const renderEventContent = (eventInfo) => (
    <div style={{ display: "flex", alignItems: "center", gap: "5px" }}>
      {/* Icône de travail (peut être personnalisée) */}
      <span role="img" aria-label="work-icon">📃📚</span> 
      <span>{eventInfo.event.title}</span>
    </div>
  );

  return (
    <div style={{ padding: "20px", margin: "50px" }}>
      <h1>Calendrier des événements</h1>
      
      
      
      <FilterPanel
        selectedCategories={selectedCategories}
        onCategoryChange={handleCategoryChange}
        selectedLocation={selectedLocation}
        onLocationChange={handleLocationChange}
        selectedMonth={selectedMonth}
        onMonthChange={handleMonthChange}
      />

{/* Affichage du mois en cours */}
<h2 style={styles.currentMonth}>{dayjs(selectedMonth).format("MMMM YYYY")}</h2>

      <div style={styles.container}>
        <div style={styles.calendarContainer}>
          <FullCalendar
            ref={calendarRef}
            plugins={[dayGridPlugin, timeGridPlugin, interactionPlugin]}
            initialView="dayGridMonth"
            locale={frLocale}
            events={filteredEvents}
            dateClick={handleDateClick}
            headerToolbar={{
              left: "prev,next today",
              center: "",
              right: '',
            }}
            selectable={true}
            editable={true}
            eventContent={renderEventContent} // Ajout de l'icône de travail
          />
        </div>
        
        <div style={styles.eventsContainer}>
          <Events showBackButton={false} />
        </div>
      </div>
    </div>
  );
};

const styles = {
  container: {
    display: "flex",
    flexDirection: "row",
    padding: "20px",
    gap: "20px",
    margin: "50px",
  },
  calendarContainer: {
    flex: 3,
    minWidth: "600px",
  },
  eventsContainer: {
    flex: 1,
    minWidth: "300px",
  },
  currentMonth: {
    fontSize: "20px",
    fontWeight: "bold",
    textAlign: "center",
    marginBottom: "20px",
    color: "#333",
  },
};

export default Calendar;
