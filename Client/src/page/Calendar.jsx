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

  // Référence pour accéder à l'instance de FullCalendar
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

    // Naviguer automatiquement vers le mois sélectionné dans FullCalendar
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

  return (
    <div style={{ padding: "20px" , margin: "50px" }}>

      <h1>Calendrier des événements</h1>
      
      <FilterPanel
        selectedCategories={selectedCategories}
        onCategoryChange={handleCategoryChange}
        selectedLocation={selectedLocation}
        onLocationChange={handleLocationChange}
        selectedMonth={selectedMonth}
        onMonthChange={handleMonthChange}
      />

<div style={styles.container}>
      {/* Section du calendrier */}
      <div style={styles.calendarContainer}>

      <FullCalendar
        ref={calendarRef} // Ajout de la référence
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
      />
    </div>
        {/* Section des événements */}
        <div style={styles.eventsContainer}>
        <Events showBackButton={false} /> {/* Cacher le bouton */}
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
    margin: "50px",
  },
  calendarContainer: {
    flex: 3, // Largeur pour le calendrier
    minWidth: "600px",
  },
  eventsContainer: {
    flex: 1, // Largeur pour la section des événements
    minWidth: "300px",
  },
};

export default Calendar;
