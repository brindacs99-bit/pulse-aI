import React, { useEffect, useState } from "react";
import axios from "axios";

function App() {
  const [cpu, setCpu] = useState("Loading...");

  useEffect(() => {
    axios.get("http://localhost:5000/cpu")
      .then((response) => {
        setCpu(response.data.cpu);

      })
      .catch((error) => {
        console.error(error);
        setCpu("Error fetching CPU");
      });
  }, []);

  return (
    <div style={{ textAlign: "center", marginTop: "100px" }}>
      <h1>Pulse AI - Professional Server Monitoring</h1>
      <h2>Live CPU Usage</h2>
      <h1>{cpu}%</h1>
    </div>
  );
}

export default App;
