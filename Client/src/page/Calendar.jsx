import React, { useState, useRef } from "react";
import FullCalendar from "@fullcalendar/react";
import dayGridPlugin from "@fullcalendar/daygrid";
import timeGridPlugin from "@fullcalendar/timegrid";
import interactionPlugin from "@fullcalendar/interaction";
import frLocale from "@fullcalendar/core/locales/fr";

const Calendar = () => {
  const [events, setEvents] = useState([
    { title: "Événement 1", date: "2024-11-12" },
    { title: "Événement 2", date: "2024-11-15" },
  ]);

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
    <div style={{ padding: "20px" }}>
      <FullCalendar
        plugins={[dayGridPlugin, timeGridPlugin, interactionPlugin]}
        initialView="dayGridMonth"
        locale={frLocale} // Définit la langue française
        events={events} // Passe les événements existants
        dateClick={handleDateClick} // Gère les clics pour ajouter des événements
        headerToolbar={{
          left: "prev,next today",
          center: "",
          right: '',
        }}
        selectable={true} // Permet la sélection de dates
        editable={true} // Permet de déplacer les événements
      />
    </div>
  );
};

const styles = {
  container: {
    display: "flex",
    flexDirection: "row",      // Aligne les éléments horizontalement
    padding: "20px",
    gap: "20px",               // Espace entre le calendrier et les événements
    margin: "50px",
  },
  calendarContainer: {
    flex: 3,                   // Largeur pour le calendrier
    minWidth: "600px",
  },
  eventsContainer: {
    flex: 1,                   // Largeur pour la section des événements
    minWidth: "300px",
    display: "flex",           // Assure que les événements sont bien alignés horizontalement
    flexDirection: "column",   // Garde les événements dans une colonne si nécessaire
    gap: "20px",               // Espacement entre les événements
  },
};

export default Calendar;
