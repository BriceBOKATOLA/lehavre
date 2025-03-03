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
    <div style={{ padding: "20px" }}>
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
        <div style={{ padding: "20px", height: "75vh" }}>
          <FullCalendar
            height='100%'
            plugins={[dayGridPlugin, timeGridPlugin, interactionPlugin]}
            initialView="dayGridMonth"
            locale={frLocale} // Définit la langue française
            events={events} // Passe les événements existants
            dateClick={handleDateClick} // Gère les clics pour ajouter des événements
            headerToolbar={{
              left: "prev,next today",
              center: "title",
              right: 'dayGridMonth,timeGridWeek,timeGridDay',
            }}
            selectable={true} // Permet la sélection de dates
            editable={true} // Permet de déplacer les événements
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
    gap: "20px", // Espace entre le calendrier et la section des événements
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
    fontSize: "24px",
    fontWeight: "bold",
    marginBottom: "20px",
    padding: "20px 20px 0px 20px",
    color: "#333",
  },
};

export default Calendar;
