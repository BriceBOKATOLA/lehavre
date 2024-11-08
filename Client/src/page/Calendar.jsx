import React, { useState } from "react";
import FullCalendar from "@fullcalendar/react";
import dayGridPlugin from "@fullcalendar/daygrid";
import timeGridPlugin from "@fullcalendar/timegrid";
import interactionPlugin from "@fullcalendar/interaction";
import frLocale from "@fullcalendar/core/locales/fr";
import Events from "./Events";

const Calendar = () => {
  const [events, setEvents] = useState([
    { title: "Événement 1", date: "2024-11-05" },
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
    <div style={styles.container}>
      {/* Section du calendrier */}
      <div style={styles.calendarContainer}>
        <FullCalendar
          plugins={[dayGridPlugin, timeGridPlugin, interactionPlugin]}
          initialView="dayGridMonth"
          locale={frLocale} // Définit la langue française
          events={events} // Passe les événements existants
          dateClick={handleDateClick} // Gère les clics pour ajouter des événements
          headerToolbar={{
            left: "prev,next today",
            center: "title",
            right: '',
          }}
          selectable={true} // Permet la sélection de dates
          editable={true} // Permet de déplacer les événements
        />
      </div>

      {/* Section des événements */}
      <div style={styles.eventsContainer}>
        <Events showBackButton={false} /> {/* Cacher le bouton */}
      </div>
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
