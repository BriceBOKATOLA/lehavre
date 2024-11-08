import React from "react";
import { Navigate } from "react-router-dom";

// Remplacez `isAuthenticated` par un système d'authentification réel
const isAuthenticated = () => {
  // Par exemple, vérifiez un token ou l'état d'authentification de l'utilisateur
  return localStorage.getItem("authToken") ? true : false;
};

const ProtectedRoute = ({ children }) => {
  return isAuthenticated() ? children : <Navigate to="/" />;
};

export default ProtectedRoute;
