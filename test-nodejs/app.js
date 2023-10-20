const express = require("express");

const app = express();

app.get("/", (req, res) => {
  const ipAddress = req.headers["x-forwarded-for"];

  if (!ipAddress) {
    ipAddress = req.connection.remoteAddress;
  }

  res.send(`Din IP-adress är: ${ipAddress}`);
});

app.listen(3000, () => {
  console.log("Servern är nu igång på port 3000");
});