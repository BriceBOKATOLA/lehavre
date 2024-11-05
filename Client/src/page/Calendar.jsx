import React, { useState } from "react";
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
    // Permet d'ajouter un nouvel événement en cliquant sur une date
    const title = prompt("Entrez le titre de l'événement:");
    if (title) {
      setEvents([...events, { title, date: info.dateStr }]);
    }
  };

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

export default Calendar;
