import React, { useState, useEffect } from "react";
import Fullcalendar from "@fullcalendar/react";
import dayGridPlugin from "@fullcalendar/daygrid";
import interactionPlugin from "@fullcalendar/interaction";
import frLocale from "@fullcalendar/core/locales/fr"; // Importer la locale française

function Calendar() {
  const [selectedDate, setSelectedDate] = useState(""); // État pour stocker la date sélectionnée
  const [selectedCell, setSelectedCell] = useState(null); // État pour suivre la cellule cliquée

  // Fonction pour obtenir la date d'aujourd'hui au format YYYY-MM-DD
  const getTodayDate = () => {
    const today = new Date();
    return today.toISOString().split("T")[0];
  };

  // Fonction pour gérer le clic sur un jour du calendrier
  const handleDateClick = (info) => {
    // Mettre à jour la date sélectionnée dans le bon format
    const selected = new Date(info.dateStr);
    const options = { weekday: "long", month: "long", day: "numeric" }; // Format du jour en français
    const formattedDate = selected.toLocaleDateString("fr-FR", options);
    setSelectedDate(formattedDate); // Mettre à jour l'état avec la date formatée

    // Gérer la classe pour la cellule cliquée
    if (selectedCell) {
      selectedCell.classList.remove("selected-cell"); // Retirer la classe de la cellule précédente
    }
    setSelectedCell(info.dayEl); // Stocker la nouvelle cellule sélectionnée
    info.dayEl.classList.add("selected-cell"); // Ajouter la classe à la nouvelle cellule cliquée
  };

  // Utiliser useEffect pour ajouter une classe "today-cell" au jour actuel
  useEffect(() => {
    const todayDate = getTodayDate();
    const todayElement = document.querySelector(`[data-date="${todayDate}"]`);
    if (todayElement) {
      todayElement.classList.add("today-cell");
    }
  }, []);

  return (
    <div className="calendar-container">
      <h3>
        {selectedDate
          ? `Date sélectionnée : ${selectedDate}`
          : "Cliquez sur une date pour la sélectionner"}
      </h3>
      <Fullcalendar
        plugins={[dayGridPlugin, interactionPlugin]}
        initialView="dayGridMonth"
        aspectRatio={1}
        height={600}
        headerToolbar={{
          start: "prev,next",
          center: "title",
          end: "",
        }}
      
        locale={frLocale} // Utilisation de la langue française
        firstDay={1} // Démarrer la semaine le lundi
        showNonCurrentDates={false} // Ne pas afficher les jours du mois précédent/suivant
        dateClick={handleDateClick} // Rendre les dates cliquables
      />
    </div>
  );
}

export default Calendar;
