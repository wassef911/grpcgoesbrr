import express, { Request, Response } from "express";
import dotenv from "dotenv";
import morgan from "morgan";
import routes from "./routers";

dotenv.config();

const nodeend = express();
const PORT = process.env.PORT || 8000;

nodeend.use(morgan("combined"));
nodeend.use("/api", routes);

nodeend.use((err: any, req: Request, res: Response, next: Function) => {
    console.error(err.stack);
    res.status(500).send("Oups, Something broke!");
});

nodeend.listen(PORT, () => console.log(`🚀 Server is running on port ${PORT}...`));
