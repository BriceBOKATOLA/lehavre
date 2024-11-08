import React from 'react'

export default function database() {
  const URL = 'http://localhost:8000/' 
    // cette page appelle l'api pour récupére les données 
    // a voir : crée des fonctions pour les différent appel 
    
    const get_all_evenement = () => {
      fetch(URL + "evenements/", {
        method: 'GET',
        headers: {
          'Content-Type': 'application/json',
        },
      })
        .then(response => response.json())
        .then(data => {
          console.log("Données récupérées :", data);
        })
        .catch((error) => {
          console.error("Erreur :", error);
        });
    }
    
    get_all_evenement();

  // return (
  //   <div>
      
  //   </div>
  // )
}
