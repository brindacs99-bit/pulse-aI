const express = require("express");
const axios = require("axios");
const cors = require("cors");

const app = express();
app.use(cors());

const PORT = 5000;

app.get("/", (req, res) => {
  res.send("Backend is running 🚀");
});

app.get("/cpu", async (req, res) => {
  try {
    const response = await axios.get(
      "http://localhost:9090/api/v1/query",
      {
        params: {
          query:
            "100 - (avg(irate(node_cpu_seconds_total{mode='idle'}[5m])) * 100)"
        }
      }
    );

    let value = response.data.data.result[0]?.value[1] || 0;
    value = Math.max(0, parseFloat(value)).toFixed(2);

    res.json({ cpu: value });
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});
