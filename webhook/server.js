const express = require("express");
const { exec } = require("child_process");

const app = express();

app.use(express.json());

app.post("/webhook", (req, res) => {
  console.log("GitHub Push Received");

  exec(
    "/Users/mohammedadam/Downloads/engineering-ai-assistant-rag/deploy.sh",
    (err, stdout, stderr) => {
      if (err) {
        console.error(err);
        return;
      }

      console.log(stdout);

      if (stderr) {
        console.error(stderr);
      }
    }
  );

  res.sendStatus(200);
});

app.listen(3000, () => {
  console.log("Webhook server running on port 3000");
});
