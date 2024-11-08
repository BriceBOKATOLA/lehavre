import { useNavigate } from "react-router-dom";
import React, { useState } from "react";

const Events = ({ showBackButton = true }) => {
  // État pour savoir si l'on affiche tous les événements ou seulement 5
  const [showAllEvents, setShowAllEvents] = useState(false);

  // Fonction pour basculer l'état de l'affichage
  const handleShowMore = () => {
    setShowAllEvents(!showAllEvents);
  };

  return (
    <div style={styles.container}>
      {/* Bouton de retour (affiché seulement si showBackButton est true) */}
      {showBackButton && (
        <div style={styles.header}>
          <button style={styles.backButton}>← Revenir au Calendrier</button>
        </div>
      )}

      {/* Titre de la page */}
      <h1 style={styles.pageTitle}>ÉVÉNEMENTS DE LA SEMAINE</h1>

      {/* Sections des événements */}
      <EventSection title="EMPLOI & FORMATION" events={dummyEvents} showAll={showAllEvents} />
      
      {/* Bouton pour voir plus d'événements */}
      <div style={styles.showMoreButtonContainer}>
        <button style={styles.showMoreButton} onClick={handleShowMore}>
          {showAllEvents ? "Voir moins d'événements" : "Voir plus d'événements"}
        </button>
      </div>
    </div>
  );
};

// Section des événements (Emploi & Formation)
const EventSection = ({ title, events, showAll }) => {
  const eventsToDisplay = showAll ? events : events.slice(0, 5);

  return (
    <div style={styles.section}>
      <h2 style={styles.sectionTitle}>{title}</h2>
      <div style={styles.eventsList}>  {/* Ajout d'un conteneur flex pour les événements */}
        {eventsToDisplay.map((event, index) => (
       <React.Fragment key={index}>
       <EventCard event={event} />
       {/* Ajoute une ligne de séparation sauf après le dernier événement */}
       {index < eventsToDisplay.length - 1 && <hr style={styles.divider} />}
     </React.Fragment>
   ))}
      </div>
    </div>
  );
};


// Carte d'événement individuelle
const EventCard = ({ event }) => {
  const navigate = useNavigate();

  const handleCardClick = () => {
    navigate(`/EventCard`, { state: { event } });
  };

  return (
    <div style={styles.eventCard} onClick={handleCardClick}>
      <img src={event.image} alt="Events" style={styles.eventImage} />
      <div style={styles.eventInfo}>
        <h3 style={styles.eventTitle}>{event.title}</h3>
        <p style={styles.eventDetails}>Horaires : Lun 12 Septembre</p>
        <p style={styles.eventDetails}>De 12h00 à 17h00</p>
      </div>
    </div>
  );
};

// Données d'exemple
const dummyEvents = [
  {
    title: "Titre événement 1",
    image: "https://www.lehavre-etretat-tourisme.com/uploads/2020/04/le-havre_0000-00_week-end-de-la-glisse_erik-levilly-ville-du-havre.jpg", 
  },
  {
    title: "Titre événement 2",
    image: "https://www.lehavre-etretat-tourisme.com/uploads/2020/04/le-havre_0000-00_week-end-de-la-glisse_erik-levilly-ville-du-havre.jpg", 
  },
  {
    title: "Titre événement 3",
    image: "https://www.lehavre-etretat-tourisme.com/uploads/2020/04/le-havre_0000-00_week-end-de-la-glisse_erik-levilly-ville-du-havre.jpg", 
  },
  {
    title: "Titre événement 4",
    image: "https://www.lehavre-etretat-tourisme.com/uploads/2020/04/le-havre_0000-00_week-end-de-la-glisse_erik-levilly-ville-du-havre.jpg", 
  },
  {
    title: "Titre événement 5",
    image: "https://www.lehavre-etretat-tourisme.com/uploads/2020/04/le-havre_0000-00_week-end-de-la-glisse_erik-levilly-ville-du-havre.jpg", 
  },
  {
    title: "Titre événement 6",
    image: "https://www.lehavre-etretat-tourisme.com/uploads/2020/04/le-havre_0000-00_week-end-de-la-glisse_erik-levilly-ville-du-havre.jpg", 
  },
  {
    title: "Titre événement 7",
    image: "https://www.lehavre-etretat-tourisme.com/uploads/2020/04/le-havre_0000-00_week-end-de-la-glisse_erik-levilly-ville-du-havre.jpg", 
  },

];

// Styles en ligne pour l'interface
const styles = {
  container: {
    fontFamily: "'Arial', sans-serif",
    color: "#333",
    backgroundColor: "#F8F8F8",
    padding: "20px",
  },
  header: {
    display: "flex",
    justifyContent: "flex-end",
  },
  backButton: {
    backgroundColor: "#4CAF50",
    color: "#fff",
    padding: "8px 16px",
    border: "none",
    borderRadius: "4px",
    fontWeight: "bold",
    cursor: "pointer",
  },
  pageTitle: {
    textAlign: "center",
    fontSize: "24px",
    fontWeight: "bold",
    margin: "0",
    padding: "10px 0",
    backgroundColor:"#1A1A4E",
    color: "#fff",
  },
  section: {
    marginBottom: "30px",
  },
  sectionTitle: {
    color: "#4CAF50",
    fontSize: "20px",
    fontWeight: "bold",
    textAlign: "left",
    marginBottom: "10px",
    paddingLeft: "10px",
  },
  eventsList: {
    display: "flex",
    flexWrap: "wrap",
    gap: "20px",
    justifyContent: "center",
  },
  eventRow: {
    display: "flex",
    flexWrap: "wrap",
    gap: "10px",
    justifyContent: "space-evenly",
    padding: "5px",
  },
  eventCard: {
    display: "flex",
    backgroundColor: "#fff",
    borderRadius: "4px",
    boxShadow: "0 4px 8px rgba(0, 0, 0, 0.1)",
    overflow: "hidden",
    width: "300px",
  },
  eventImage: {
    width: "80px",
    height: "80px",
    objectFit: "cover",
  },
  eventInfo: {
    padding: "10px",
    textAlign: "left",
  },
  eventTitle: {
    fontSize: "16px",
    fontWeight: "bold",
    margin: "0 0 5px 0",
  },
  eventDetails: {
    fontSize: "12px",
    color: "#666",
    margin: "2px 0",
  },
  divider: {
    margin: "20px 0",
    border: "0",
    borderTop: "1px solid #ddd",
    width: "95%",
    marginLeft: "auto",
    marginRight: "auto",
  },
  showMoreButtonContainer: {
    textAlign: "center",
    marginTop: "20px",
  },
  showMoreButton: {
    backgroundColor: "#4CAF50",
    color: "#fff",
    padding: "8px 16px",
    border: "none",
    borderRadius: "4px",
    fontWeight: "bold",
    cursor: "pointer",
  },
};

export default Events;
