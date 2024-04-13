import express, { Request, Response } from 'express';
import dotenv from 'dotenv';
import morgan from 'morgan';

dotenv.config();

const app = express();
const port = process.env.PORT || 8000;

app.use(morgan('combined'));

app.get('/FraudActivity', (req: Request, res: Response) => {
    const transaction_id = req.query.transaction_id as string;
    if (transaction_id) {
        res.status(200).send(`Hello, ${transaction_id}!`);
    } else {
        res.status(400).send('Missing query parameter: transaction_id');
    }
});

app.use((err: any, req: Request, res: Response, next: Function) => {
    console.error(err.stack);
    res.status(500).send('Oups, Something broke!');
});

app.listen(port, () => console.log(`🚀 Server is running on port ${port}...`));
