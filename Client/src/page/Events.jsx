import { useNavigate } from "react-router-dom";


const Events = () => {
  return (
    <div style={styles.container}>
      {/* Bouton de retour */}
      <div style={styles.header}>
        <button style={styles.backButton}>← Revenir au Calendrier</button>
      </div>
      
      {/* Titre de la page */}
      <h1 style={styles.pageTitle}>ÉVÉNEMENTS DE LA SEMAINE</h1>
      
      {/* Sections des événements */}
      <EventSection title="EMPLOI & FORMATION" events={dummyEvents} />
    </div>
  );
};

// Section des événements (Emploi & Formation)
const EventSection = ({ title, events }) => {
  return (
    <div style={styles.section}>
      <h2 style={styles.sectionTitle}>{title}</h2>
      <div style={styles.eventRow}>
        {events.map((event, index) => (
          <EventCard key={index} event={event} />
        ))}
      </div>
      <hr style={styles.divider} />
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
        <p style={styles.eventDetails}>Horaires : Lun 12 Sept</p>
        <p style={styles.eventDetails}>De ...h... à ...h...</p>
      </div>
    </div>
  );
};

// Données d'exemple
const dummyEvents = [
  {
    title: "Titre événement",
    image: "", 
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
    margin: "20px 0",
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
  eventRow: {
    display: "flex",
    flexWrap: "wrap",
    gap: "10px",
    justifyContent: "space-evenly",
  },
  eventCard: {
    display: "flex",
    backgroundColor: "#fff",
    borderRadius: "4px",
    boxShadow: "0 4px 8px rgba(0, 0, 0, 0.1)",
    overflow: "hidden",
    width: "180px",
    cursor: "pointer",
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
};

export default Events;
