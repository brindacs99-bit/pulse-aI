import React from "react";

function Dashboard() {

  return (

    <div style={{
      height:"100vh",
      width:"100%",
      background:"#020b1f"
    }}>

      <iframe
        src="http://localhost:8501"
        title="Pulse AI Monitoring"
        width="100%"
        height="100%"
        style={{
          border:"none"
        }}
      />

    </div>

  );

}

export default Dashboard;