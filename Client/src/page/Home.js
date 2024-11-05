import React from "react";
import Filter from "../composant/Filter";

const Home = () => {
  return (
    <div style={styles.container}>
      <h1>Bienvenue sur la page d'accueil</h1>
      <p>Cette page présente un aperçu de l'application.</p>
    </div>
  );
};

const styles = {
  container: {
    padding: "20px",
    textAlign: "center",
  },
};

export default Home;

