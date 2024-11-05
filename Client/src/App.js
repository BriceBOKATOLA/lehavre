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
        
        <Routes>
          {/* Routes publiques */}
          <Route path="/" element={<Home />} />
          <Route path="/calendar" element={<Calendar />} />
          <Route path="/events" element={<Events />} />
          <Route path="/card" element={<EventCard />} />

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
