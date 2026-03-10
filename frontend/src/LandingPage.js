import React from "react";
import { Link, useNavigate } from "react-router-dom";
import "./LandingPage.css";

function LandingPage() {

  const navigate = useNavigate();

  return (
    <div>

      {/* NAVBAR */}
      <nav className="navbar">

        <div className="logo-section">
          <img src="/logo.png" alt="Pulse AI Logo" className="logo" />
          <h2>Pulse.ai</h2>
        </div>

        <div className="nav-links">
          <Link to="/">Features</Link>
          <Link to="/dashboard">Monitoring</Link>
          <Link to="/forecast">Forecasting</Link>
          <Link to="/login">Login</Link>

          <button
            className="demo-btn"
            onClick={() => navigate("/login")}
          >
            Start Monitoring
          </button>
        </div>

      </nav>


      {/* HERO SECTION */}
      <div className="hero">

        <div className="hero-left">

          <h1>
            AI Powered Server Monitoring & Forecasting
          </h1>

          <p>
            Pulse.ai provides real-time infrastructure monitoring using
            Prometheus and Grafana while predicting future server load
            using machine learning models.
          </p>

          <div className="features">
            <span>Real Time Monitoring</span>
            <span>AI Forecasting</span>
            <span>Alert System</span>
            <span>Infrastructure Insights</span>
          </div>

        </div>


        {/* SIGNUP CARD */}
        <div className="hero-right">

          <div className="signup-card">

            <h2>Start Monitoring Your Servers</h2>

            <input type="email" placeholder="Email" />

            <input type="password" placeholder="Password" />

            <button
              onClick={() => navigate("/login")}
            >
              GET STARTED
            </button>

          </div>

        </div>

      </div>

    </div>
  );
}

export default LandingPage;