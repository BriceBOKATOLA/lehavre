import React, { useState, useRef } from "react";
import FullCalendar from "@fullcalendar/react";
import dayGridPlugin from "@fullcalendar/daygrid";
import timeGridPlugin from "@fullcalendar/timegrid";
import interactionPlugin from "@fullcalendar/interaction";
import frLocale from "@fullcalendar/core/locales/fr";
import dayjs from "dayjs";
import FilterPanel from "../composant/filtrePanel";

const Calendar = () => {
  const [events, setEvents] = useState([
    { title: "Événement 1", date: "2024-11-12", category: "Emploi", location: "Paris" },
    { title: "Événement 2", date: "2024-11-15", category: "Personnel", location: "Lyon" },
    { title: "Événement 3", date: "2024-12-01", category: "Santé", location: "Marseille" },
    { title: "Événement 4", date: "2024-12-05", category: "Travail", location: "Bordeaux" },
  ]);

  const [selectedCategories, setSelectedCategories] = useState([]);
  const [selectedLocation, setSelectedLocation] = useState("All");
  const [selectedMonth, setSelectedMonth] = useState(dayjs().format("YYYY-MM"));

  // Référence pour accéder à l'instance de FullCalendar
  const calendarRef = useRef(null);

  const handleDateClick = (info) => {
    const title = prompt("Entrez le titre de l'événement:");
    const category = prompt("Entrez la catégorie de l'événement (Emploi, Travail, Personnel, Santé) :");
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
      <h1>Calendrier des événements</h1>
      
      <FilterPanel
        selectedCategories={selectedCategories}
        onCategoryChange={handleCategoryChange}
        selectedLocation={selectedLocation}
        onLocationChange={handleLocationChange}
        selectedMonth={selectedMonth}
        onMonthChange={handleMonthChange}
      />

      <FullCalendar
        ref={calendarRef} // Ajout de la référence
        plugins={[dayGridPlugin, timeGridPlugin, interactionPlugin]}
        initialView="dayGridMonth"
        locale={frLocale}
        events={filteredEvents}
        dateClick={handleDateClick}
        headerToolbar={{
          left: "prev,next today",
          center: "title",
          right: "dayGridMonth,timeGridWeek,timeGridDay",
        }}
        selectable={true}
        editable={true}
      />
    </div>
  );
};

export default Calendar;
