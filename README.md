# gRPC goes BRRR!

a **POC** to learn gRPC, and playaround in a imaginary scenario,
Where you want the use a ML model in **python**,
but want to expose somesort other BACKEND to clients, for whatever reason:

- productivity
- performance
- security
- legacy
- stubbornness 🙃

altho obviously you could do this over a stupid rest API.

Today I decided to do it over a stupid gRPC API, to reduce request latency, resource utilization and waste an evening.

#### BEHOLD THE GREATEST OF DIAGRAMS!!! (took 5 minutes 😋)

```js

Some client that
you convinced to use
your backend!
another server or
somesort of UI
┌──────────────┐         ┌──────────────┐                   ┌──────────────┐
│  SomeClient  │         │ Node Backend │                   │Python Backend│
└───────┬──────┘         └──────┬───────┘                   └───────┬──────┘
        │                       │                                   │
        │                       │                                   │
        │ POST: {transaction_id}│                                   │
        │ /api/FraudActivity    │                                   │
        ├──────────────────────►│                                   │
        │+[AUTH/PERMISSION]     │ rpc: package fraud_detection: FraudDetectionService(PredictFraud)
        │                       │                              ┌────┬─────────┐
        │                       ├──────────────────────────────┼──► │         │
        │                       │message PredictionRequest {   │    │Load model
        │                       │    int64 transaction_id      │    │         ┼
        │                       │    double amount             │    │ExtractsFeature
        │                       │    int64 time                │    │         ┼
        │                       │    int32 age_of_account      │    │Do Prediction
        │                       │    int32 number_of_transactions   │         │
        │                       │}                             │    │         │
        │                       │                              │    │         │
        │                       │◄─────────────────────────────┼────┤         │
        │                       │ message PredictionResponse { └────┼─────────┘
        │                       │     int64 transaction_id          │
        │                       │     bool predicted_label          │
        │                       │     double fraud_probability      │
        │                       │ }                                 │
        │◄──────────────────────┤                                   │
        │                       │                                   │
        │{                      │                                   │
        │    "transaction_id": "Y12a34x56",                         │
        │    "predicted_label": true,                               │
        │    "fraud_probability": 99.99,                            │
        │}                      │                                   │
        │                       │                                   │
        │                       │                                   │
```
