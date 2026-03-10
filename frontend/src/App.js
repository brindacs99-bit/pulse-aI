import React from "react";
import { BrowserRouter, Routes, Route, Navigate } from "react-router-dom";

import LandingPage from "./LandingPage";
import Login from "./pages/Login";
import Dashboard from "./pages/Dashboard";
import Forecast from "./pages/Forecast";

/* Protected Route */
function PrivateRoute({ children }) {

  const isLoggedIn = localStorage.getItem("auth");

  return isLoggedIn ? children : <Navigate to="/login" />;

}

function App() {

  return (

    <BrowserRouter>

      <Routes>

        <Route path="/" element={<LandingPage />} />

        <Route path="/login" element={<Login />} />

        <Route
          path="/dashboard"
          element={
            <PrivateRoute>
              <Dashboard />
            </PrivateRoute>
          }
        />

        <Route
          path="/forecast"
          element={
            <PrivateRoute>
              <Forecast />
            </PrivateRoute>
          }
        />

      </Routes>

    </BrowserRouter>

  );
}

export default App;