import React from "react";
import { useNavigate } from "react-router-dom";

const NotFound = () => {
  const navigate = useNavigate();

  return (
    <div style={styles.container}>
      <h1 style={styles.title}>404 - Page non trouvée</h1>
      <p style={styles.message}>Désolé, la page que vous cherchez n'existe pas.</p>
      <button style={styles.button} onClick={() => navigate("/")}>
        Retour à l'accueil
      </button>
    </div>
  );
};

const styles = {
  container: {
    display: "flex",
    flexDirection: "column",
    alignItems: "center",
    justifyContent: "center",
    height: "100vh",
    textAlign: "center",
    color: "#333",
  },
  title: {
    fontSize: "48px",
    fontWeight: "bold",
  },
  message: {
    fontSize: "18px",
    marginBottom: "20px",
  },
  button: {
    padding: "10px 20px",
    backgroundColor: "#4CAF50",
    color: "#fff",
    border: "none",
    borderRadius: "4px",
    cursor: "pointer",
    fontSize: "16px",
  },
};

export default NotFound;
