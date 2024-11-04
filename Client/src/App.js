import React from "react";
import { BrowserRouter as Router, Routes, Route, Link } from "react-router-dom";
import Home from "./page/Home";
import Events from "./page/Events";
import Calendar from "./page/Calendar";
import NotFound from "./page/NotFound";
import ProtectedRoute from "./composant/ProtectedRoute";
import EventCard from "./page/EventCard";
import Header from "./composant/Header";

const App = () => {
  return (
    <Router>
      <div>

        <Header />
        
        <nav style={styles.navbar}>
          <Link to="/" style={styles.link}>Accueil</Link>
          <Link to="/calendar" style={styles.link}>Calendrier</Link>
          <Link to="/events" style={styles.link}>Evénement</Link>
        </nav>

        <Routes>
          {/* Routes publiques */}
          <Route path="/" element={<Home />} />
          <Route path="/calendar" element={<Calendar />} />
          <Route path="/events" element={<Events />} />

          {/* Route protégée */}
          <Route
            path="/events"
            element={
              <ProtectedRoute>
                <EventCard />
              </ProtectedRoute>
            }
          />

          {/* Route pour page non trouvée */}
          <Route path="*" element={<NotFound />} />
        </Routes>
      </div>
    </Router>
  );
};

const styles = {
  navbar: {
    display: "flex",
    justifyContent: "space-around",
    padding: "1rem",
    backgroundColor: "#333",
  },
  link: {
    color: "#fff",
    textDecoration: "none",
    fontSize: "18px",
  },
};

export default App;
