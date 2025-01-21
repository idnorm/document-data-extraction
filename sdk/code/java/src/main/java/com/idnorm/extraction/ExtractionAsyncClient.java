package com.idnorm.extraction;

import com.google.protobuf.ByteString;
import io.grpc.stub.StreamObserver;
import proto.ddx.v1.ExtractionGrpc;
import proto.ddx.v1.Service;

public class ExtractionAsyncClient {

    private final ExtractionGrpc.ExtractionStub stub;

    protected ExtractionAsyncClient(ExtractionGrpc.ExtractionStub stub) {
        this.stub = stub;
    }

    public static ExtractionClientBuilder<ExtractionAsyncClient> builder() {
        return new ExtractionClientBuilder<>(c -> new ExtractionAsyncClient(ExtractionGrpc.newStub(c)));
    }

    public void scanDocument(ByteString imgData, StreamObserver<Service.ScanDocumentResponse> responseObserver) {
        stub.scanDocument(Service.ScanDocumentRequest.newBuilder()
                .setImageJpeg(imgData)
                .build(), responseObserver);
    }

    public void scanDocument(ByteString imgData, Service.ScanConfig cfg, StreamObserver<Service.ScanDocumentResponse> responseObserver) {
        stub.scanDocument(Service.ScanDocumentRequest.newBuilder()
                .setImageJpeg(imgData)
                .setConfig(cfg)
                .build(), responseObserver);
    }

}
