import { Router, Request, Response } from "express";
import FraudService from "./services";

const CORE_PROTO_PATH = process.env.CORE_PROTO_PATH || "./core.proto";
const GRPC_SERVER_ADDRESS =
  process.env.GRPC_SERVER_ADDRESS || "pyend:50051";

const router = Router();
const fraudService = new FraudService(CORE_PROTO_PATH, GRPC_SERVER_ADDRESS);

router.get("/FraudActivity", async (req: Request, res: Response) => {
  const transaction_id = req.query.transaction_id as string;
  if (transaction_id) {
    const predictionRequest = {
      transaction_id: parseInt(transaction_id),
      amount: 100.0,
      time: 1000,
      age_of_account: 100,
      number_of_transactions: 100,
    };
    const result = await fraudService.getFraudActivity(predictionRequest);
    res.status(200).send(result);
  } else {
    res.status(400).send("Missing query parameter: transaction_id");
  }
});

router.get("/health", (req, res) => res.status(200).send("OK"));

export default router;
