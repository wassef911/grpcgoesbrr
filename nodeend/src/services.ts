import grpc from "grpc";
import * as protoLoader from "@grpc/proto-loader";

interface IPredictionRequest {
    transaction_id: number;
    amount: number;
    time: number;
    age_of_account: number;
    number_of_transactions: number;
}

interface IPredictionResponse {
    transaction_id: number;
    predicted_label: boolean;
    fraud_probability: number;
}


class BaseGrpcService {
    protected proto_buff: grpc.PackageDefinition;

    constructor(protobuffer_path: string,) {
        this.proto_buff = protoLoader.loadSync(protobuffer_path, {
            longs: String,
            enums: String,
            keepCase: true,
            defaults: true,
            oneofs: true,
        });
    }

    protected getPackagesFrom(proto_buff: grpc.PackageDefinition): grpc.GrpcObject {
        return grpc.loadPackageDefinition(
            proto_buff
        );
    }
}

class FraudService extends BaseGrpcService {
    private fraudPackage: any;
    private client: any;

    constructor(protobuffer_path: string, server_address: string) {
        super(protobuffer_path);
        this.fraudPackage = this.getPackagesFrom(this.proto_buff).fraud_detection as any;
        this.client = new this.fraudPackage.FraudDetectionService(
            server_address,
            grpc.credentials.createInsecure()
        );
    }

    public getFraudActivity(
        predictionRequest: IPredictionRequest
    ): Promise<IPredictionResponse> {
        return new Promise((resolve, reject) => {
            this.client.PredictFraud(
                predictionRequest,
                (error: any, response: IPredictionResponse) => {
                    if (error) {
                        console.error("Error calling PredictFraud:", error);
                        reject(error);
                    } else {
                        resolve(response);
                    }
                }
            );
        });
    }
}

export default FraudService;
