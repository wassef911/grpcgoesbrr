import express, { Request, Response } from "express";
import dotenv from "dotenv";
import morgan from "morgan";
import routes from "./routers";

dotenv.config();

const app = express();
const PORT = process.env.PORT || 8000;

app.use(morgan("combined"));
app.use("/api", routes);

app.use((err: any, req: Request, res: Response, next: Function) => {
    console.error(err.stack);
    res.status(500).send("Oups, Something broke!");
});

app.listen(PORT, () => console.log(`🚀 Server is running on port ${PORT}...`));
