package proto.ddx.v1;

import static io.grpc.MethodDescriptor.generateFullMethodName;

/**
 */
@javax.annotation.Generated(
    value = "by gRPC proto compiler (version 1.67.1)",
    comments = "Source: proto/ddx/v1/service.proto")
@io.grpc.stub.annotations.GrpcGenerated
public final class ExtractionGrpc {

  private ExtractionGrpc() {}

  public static final java.lang.String SERVICE_NAME = "proto.ddx.v1.Extraction";

  // Static method descriptors that strictly reflect the proto.
  private static volatile io.grpc.MethodDescriptor<proto.ddx.v1.Service.ScanDocumentRequest,
      proto.ddx.v1.Service.ScanDocumentResponse> getScanDocumentMethod;

  @io.grpc.stub.annotations.RpcMethod(
      fullMethodName = SERVICE_NAME + '/' + "ScanDocument",
      requestType = proto.ddx.v1.Service.ScanDocumentRequest.class,
      responseType = proto.ddx.v1.Service.ScanDocumentResponse.class,
      methodType = io.grpc.MethodDescriptor.MethodType.UNARY)
  public static io.grpc.MethodDescriptor<proto.ddx.v1.Service.ScanDocumentRequest,
      proto.ddx.v1.Service.ScanDocumentResponse> getScanDocumentMethod() {
    io.grpc.MethodDescriptor<proto.ddx.v1.Service.ScanDocumentRequest, proto.ddx.v1.Service.ScanDocumentResponse> getScanDocumentMethod;
    if ((getScanDocumentMethod = ExtractionGrpc.getScanDocumentMethod) == null) {
      synchronized (ExtractionGrpc.class) {
        if ((getScanDocumentMethod = ExtractionGrpc.getScanDocumentMethod) == null) {
          ExtractionGrpc.getScanDocumentMethod = getScanDocumentMethod =
              io.grpc.MethodDescriptor.<proto.ddx.v1.Service.ScanDocumentRequest, proto.ddx.v1.Service.ScanDocumentResponse>newBuilder()
              .setType(io.grpc.MethodDescriptor.MethodType.UNARY)
              .setFullMethodName(generateFullMethodName(SERVICE_NAME, "ScanDocument"))
              .setSampledToLocalTracing(true)
              .setRequestMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
                  proto.ddx.v1.Service.ScanDocumentRequest.getDefaultInstance()))
              .setResponseMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
                  proto.ddx.v1.Service.ScanDocumentResponse.getDefaultInstance()))
              .setSchemaDescriptor(new ExtractionMethodDescriptorSupplier("ScanDocument"))
              .build();
        }
      }
    }
    return getScanDocumentMethod;
  }

  private static volatile io.grpc.MethodDescriptor<proto.ddx.v1.Service.ScanTwoSidedDocumentRequest,
      proto.ddx.v1.Service.ScanTwoSidedDocumentResponse> getScanTwoSidedDocumentMethod;

  @io.grpc.stub.annotations.RpcMethod(
      fullMethodName = SERVICE_NAME + '/' + "ScanTwoSidedDocument",
      requestType = proto.ddx.v1.Service.ScanTwoSidedDocumentRequest.class,
      responseType = proto.ddx.v1.Service.ScanTwoSidedDocumentResponse.class,
      methodType = io.grpc.MethodDescriptor.MethodType.UNARY)
  public static io.grpc.MethodDescriptor<proto.ddx.v1.Service.ScanTwoSidedDocumentRequest,
      proto.ddx.v1.Service.ScanTwoSidedDocumentResponse> getScanTwoSidedDocumentMethod() {
    io.grpc.MethodDescriptor<proto.ddx.v1.Service.ScanTwoSidedDocumentRequest, proto.ddx.v1.Service.ScanTwoSidedDocumentResponse> getScanTwoSidedDocumentMethod;
    if ((getScanTwoSidedDocumentMethod = ExtractionGrpc.getScanTwoSidedDocumentMethod) == null) {
      synchronized (ExtractionGrpc.class) {
        if ((getScanTwoSidedDocumentMethod = ExtractionGrpc.getScanTwoSidedDocumentMethod) == null) {
          ExtractionGrpc.getScanTwoSidedDocumentMethod = getScanTwoSidedDocumentMethod =
              io.grpc.MethodDescriptor.<proto.ddx.v1.Service.ScanTwoSidedDocumentRequest, proto.ddx.v1.Service.ScanTwoSidedDocumentResponse>newBuilder()
              .setType(io.grpc.MethodDescriptor.MethodType.UNARY)
              .setFullMethodName(generateFullMethodName(SERVICE_NAME, "ScanTwoSidedDocument"))
              .setSampledToLocalTracing(true)
              .setRequestMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
                  proto.ddx.v1.Service.ScanTwoSidedDocumentRequest.getDefaultInstance()))
              .setResponseMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
                  proto.ddx.v1.Service.ScanTwoSidedDocumentResponse.getDefaultInstance()))
              .setSchemaDescriptor(new ExtractionMethodDescriptorSupplier("ScanTwoSidedDocument"))
              .build();
        }
      }
    }
    return getScanTwoSidedDocumentMethod;
  }

  /**
   * Creates a new async stub that supports all call types for the service
   */
  public static ExtractionStub newStub(io.grpc.Channel channel) {
    io.grpc.stub.AbstractStub.StubFactory<ExtractionStub> factory =
      new io.grpc.stub.AbstractStub.StubFactory<ExtractionStub>() {
        @java.lang.Override
        public ExtractionStub newStub(io.grpc.Channel channel, io.grpc.CallOptions callOptions) {
          return new ExtractionStub(channel, callOptions);
        }
      };
    return ExtractionStub.newStub(factory, channel);
  }

  /**
   * Creates a new blocking-style stub that supports unary and streaming output calls on the service
   */
  public static ExtractionBlockingStub newBlockingStub(
      io.grpc.Channel channel) {
    io.grpc.stub.AbstractStub.StubFactory<ExtractionBlockingStub> factory =
      new io.grpc.stub.AbstractStub.StubFactory<ExtractionBlockingStub>() {
        @java.lang.Override
        public ExtractionBlockingStub newStub(io.grpc.Channel channel, io.grpc.CallOptions callOptions) {
          return new ExtractionBlockingStub(channel, callOptions);
        }
      };
    return ExtractionBlockingStub.newStub(factory, channel);
  }

  /**
   * Creates a new ListenableFuture-style stub that supports unary calls on the service
   */
  public static ExtractionFutureStub newFutureStub(
      io.grpc.Channel channel) {
    io.grpc.stub.AbstractStub.StubFactory<ExtractionFutureStub> factory =
      new io.grpc.stub.AbstractStub.StubFactory<ExtractionFutureStub>() {
        @java.lang.Override
        public ExtractionFutureStub newStub(io.grpc.Channel channel, io.grpc.CallOptions callOptions) {
          return new ExtractionFutureStub(channel, callOptions);
        }
      };
    return ExtractionFutureStub.newStub(factory, channel);
  }

  /**
   */
  public interface AsyncService {

    /**
     * <pre>
     * Detects document on a given image and extracts all relevant fields. For input parameters
     * see ScanDocumentRequest Model documentation (in swagger, click on the "Model" in the request "Body" part)
     * </pre>
     */
    default void scanDocument(proto.ddx.v1.Service.ScanDocumentRequest request,
        io.grpc.stub.StreamObserver<proto.ddx.v1.Service.ScanDocumentResponse> responseObserver) {
      io.grpc.stub.ServerCalls.asyncUnimplementedUnaryCall(getScanDocumentMethod(), responseObserver);
    }

    /**
     * <pre>
     * Expects two images, one for front side of the document and one for back side of the document.
     * Scans both sides and extracts all relevant fields.
     * see ScanTwoSidedDocumentRequest Model documentation (in swagger, click on the "Model" in the request "Body" part)
     * </pre>
     */
    default void scanTwoSidedDocument(proto.ddx.v1.Service.ScanTwoSidedDocumentRequest request,
        io.grpc.stub.StreamObserver<proto.ddx.v1.Service.ScanTwoSidedDocumentResponse> responseObserver) {
      io.grpc.stub.ServerCalls.asyncUnimplementedUnaryCall(getScanTwoSidedDocumentMethod(), responseObserver);
    }
  }

  /**
   * Base class for the server implementation of the service Extraction.
   */
  public static abstract class ExtractionImplBase
      implements io.grpc.BindableService, AsyncService {

    @java.lang.Override public final io.grpc.ServerServiceDefinition bindService() {
      return ExtractionGrpc.bindService(this);
    }
  }

  /**
   * A stub to allow clients to do asynchronous rpc calls to service Extraction.
   */
  public static final class ExtractionStub
      extends io.grpc.stub.AbstractAsyncStub<ExtractionStub> {
    private ExtractionStub(
        io.grpc.Channel channel, io.grpc.CallOptions callOptions) {
      super(channel, callOptions);
    }

    @java.lang.Override
    protected ExtractionStub build(
        io.grpc.Channel channel, io.grpc.CallOptions callOptions) {
      return new ExtractionStub(channel, callOptions);
    }

    /**
     * <pre>
     * Detects document on a given image and extracts all relevant fields. For input parameters
     * see ScanDocumentRequest Model documentation (in swagger, click on the "Model" in the request "Body" part)
     * </pre>
     */
    public void scanDocument(proto.ddx.v1.Service.ScanDocumentRequest request,
        io.grpc.stub.StreamObserver<proto.ddx.v1.Service.ScanDocumentResponse> responseObserver) {
      io.grpc.stub.ClientCalls.asyncUnaryCall(
          getChannel().newCall(getScanDocumentMethod(), getCallOptions()), request, responseObserver);
    }

    /**
     * <pre>
     * Expects two images, one for front side of the document and one for back side of the document.
     * Scans both sides and extracts all relevant fields.
     * see ScanTwoSidedDocumentRequest Model documentation (in swagger, click on the "Model" in the request "Body" part)
     * </pre>
     */
    public void scanTwoSidedDocument(proto.ddx.v1.Service.ScanTwoSidedDocumentRequest request,
        io.grpc.stub.StreamObserver<proto.ddx.v1.Service.ScanTwoSidedDocumentResponse> responseObserver) {
      io.grpc.stub.ClientCalls.asyncUnaryCall(
          getChannel().newCall(getScanTwoSidedDocumentMethod(), getCallOptions()), request, responseObserver);
    }
  }

  /**
   * A stub to allow clients to do synchronous rpc calls to service Extraction.
   */
  public static final class ExtractionBlockingStub
      extends io.grpc.stub.AbstractBlockingStub<ExtractionBlockingStub> {
    private ExtractionBlockingStub(
        io.grpc.Channel channel, io.grpc.CallOptions callOptions) {
      super(channel, callOptions);
    }

    @java.lang.Override
    protected ExtractionBlockingStub build(
        io.grpc.Channel channel, io.grpc.CallOptions callOptions) {
      return new ExtractionBlockingStub(channel, callOptions);
    }

    /**
     * <pre>
     * Detects document on a given image and extracts all relevant fields. For input parameters
     * see ScanDocumentRequest Model documentation (in swagger, click on the "Model" in the request "Body" part)
     * </pre>
     */
    public proto.ddx.v1.Service.ScanDocumentResponse scanDocument(proto.ddx.v1.Service.ScanDocumentRequest request) {
      return io.grpc.stub.ClientCalls.blockingUnaryCall(
          getChannel(), getScanDocumentMethod(), getCallOptions(), request);
    }

    /**
     * <pre>
     * Expects two images, one for front side of the document and one for back side of the document.
     * Scans both sides and extracts all relevant fields.
     * see ScanTwoSidedDocumentRequest Model documentation (in swagger, click on the "Model" in the request "Body" part)
     * </pre>
     */
    public proto.ddx.v1.Service.ScanTwoSidedDocumentResponse scanTwoSidedDocument(proto.ddx.v1.Service.ScanTwoSidedDocumentRequest request) {
      return io.grpc.stub.ClientCalls.blockingUnaryCall(
          getChannel(), getScanTwoSidedDocumentMethod(), getCallOptions(), request);
    }
  }

  /**
   * A stub to allow clients to do ListenableFuture-style rpc calls to service Extraction.
   */
  public static final class ExtractionFutureStub
      extends io.grpc.stub.AbstractFutureStub<ExtractionFutureStub> {
    private ExtractionFutureStub(
        io.grpc.Channel channel, io.grpc.CallOptions callOptions) {
      super(channel, callOptions);
    }

    @java.lang.Override
    protected ExtractionFutureStub build(
        io.grpc.Channel channel, io.grpc.CallOptions callOptions) {
      return new ExtractionFutureStub(channel, callOptions);
    }

    /**
     * <pre>
     * Detects document on a given image and extracts all relevant fields. For input parameters
     * see ScanDocumentRequest Model documentation (in swagger, click on the "Model" in the request "Body" part)
     * </pre>
     */
    public com.google.common.util.concurrent.ListenableFuture<proto.ddx.v1.Service.ScanDocumentResponse> scanDocument(
        proto.ddx.v1.Service.ScanDocumentRequest request) {
      return io.grpc.stub.ClientCalls.futureUnaryCall(
          getChannel().newCall(getScanDocumentMethod(), getCallOptions()), request);
    }

    /**
     * <pre>
     * Expects two images, one for front side of the document and one for back side of the document.
     * Scans both sides and extracts all relevant fields.
     * see ScanTwoSidedDocumentRequest Model documentation (in swagger, click on the "Model" in the request "Body" part)
     * </pre>
     */
    public com.google.common.util.concurrent.ListenableFuture<proto.ddx.v1.Service.ScanTwoSidedDocumentResponse> scanTwoSidedDocument(
        proto.ddx.v1.Service.ScanTwoSidedDocumentRequest request) {
      return io.grpc.stub.ClientCalls.futureUnaryCall(
          getChannel().newCall(getScanTwoSidedDocumentMethod(), getCallOptions()), request);
    }
  }

  private static final int METHODID_SCAN_DOCUMENT = 0;
  private static final int METHODID_SCAN_TWO_SIDED_DOCUMENT = 1;

  private static final class MethodHandlers<Req, Resp> implements
      io.grpc.stub.ServerCalls.UnaryMethod<Req, Resp>,
      io.grpc.stub.ServerCalls.ServerStreamingMethod<Req, Resp>,
      io.grpc.stub.ServerCalls.ClientStreamingMethod<Req, Resp>,
      io.grpc.stub.ServerCalls.BidiStreamingMethod<Req, Resp> {
    private final AsyncService serviceImpl;
    private final int methodId;

    MethodHandlers(AsyncService serviceImpl, int methodId) {
      this.serviceImpl = serviceImpl;
      this.methodId = methodId;
    }

    @java.lang.Override
    @java.lang.SuppressWarnings("unchecked")
    public void invoke(Req request, io.grpc.stub.StreamObserver<Resp> responseObserver) {
      switch (methodId) {
        case METHODID_SCAN_DOCUMENT:
          serviceImpl.scanDocument((proto.ddx.v1.Service.ScanDocumentRequest) request,
              (io.grpc.stub.StreamObserver<proto.ddx.v1.Service.ScanDocumentResponse>) responseObserver);
          break;
        case METHODID_SCAN_TWO_SIDED_DOCUMENT:
          serviceImpl.scanTwoSidedDocument((proto.ddx.v1.Service.ScanTwoSidedDocumentRequest) request,
              (io.grpc.stub.StreamObserver<proto.ddx.v1.Service.ScanTwoSidedDocumentResponse>) responseObserver);
          break;
        default:
          throw new AssertionError();
      }
    }

    @java.lang.Override
    @java.lang.SuppressWarnings("unchecked")
    public io.grpc.stub.StreamObserver<Req> invoke(
        io.grpc.stub.StreamObserver<Resp> responseObserver) {
      switch (methodId) {
        default:
          throw new AssertionError();
      }
    }
  }

  public static final io.grpc.ServerServiceDefinition bindService(AsyncService service) {
    return io.grpc.ServerServiceDefinition.builder(getServiceDescriptor())
        .addMethod(
          getScanDocumentMethod(),
          io.grpc.stub.ServerCalls.asyncUnaryCall(
            new MethodHandlers<
              proto.ddx.v1.Service.ScanDocumentRequest,
              proto.ddx.v1.Service.ScanDocumentResponse>(
                service, METHODID_SCAN_DOCUMENT)))
        .addMethod(
          getScanTwoSidedDocumentMethod(),
          io.grpc.stub.ServerCalls.asyncUnaryCall(
            new MethodHandlers<
              proto.ddx.v1.Service.ScanTwoSidedDocumentRequest,
              proto.ddx.v1.Service.ScanTwoSidedDocumentResponse>(
                service, METHODID_SCAN_TWO_SIDED_DOCUMENT)))
        .build();
  }

  private static abstract class ExtractionBaseDescriptorSupplier
      implements io.grpc.protobuf.ProtoFileDescriptorSupplier, io.grpc.protobuf.ProtoServiceDescriptorSupplier {
    ExtractionBaseDescriptorSupplier() {}

    @java.lang.Override
    public com.google.protobuf.Descriptors.FileDescriptor getFileDescriptor() {
      return proto.ddx.v1.Service.getDescriptor();
    }

    @java.lang.Override
    public com.google.protobuf.Descriptors.ServiceDescriptor getServiceDescriptor() {
      return getFileDescriptor().findServiceByName("Extraction");
    }
  }

  private static final class ExtractionFileDescriptorSupplier
      extends ExtractionBaseDescriptorSupplier {
    ExtractionFileDescriptorSupplier() {}
  }

  private static final class ExtractionMethodDescriptorSupplier
      extends ExtractionBaseDescriptorSupplier
      implements io.grpc.protobuf.ProtoMethodDescriptorSupplier {
    private final java.lang.String methodName;

    ExtractionMethodDescriptorSupplier(java.lang.String methodName) {
      this.methodName = methodName;
    }

    @java.lang.Override
    public com.google.protobuf.Descriptors.MethodDescriptor getMethodDescriptor() {
      return getServiceDescriptor().findMethodByName(methodName);
    }
  }

  private static volatile io.grpc.ServiceDescriptor serviceDescriptor;

  public static io.grpc.ServiceDescriptor getServiceDescriptor() {
    io.grpc.ServiceDescriptor result = serviceDescriptor;
    if (result == null) {
      synchronized (ExtractionGrpc.class) {
        result = serviceDescriptor;
        if (result == null) {
          serviceDescriptor = result = io.grpc.ServiceDescriptor.newBuilder(SERVICE_NAME)
              .setSchemaDescriptor(new ExtractionFileDescriptorSupplier())
              .addMethod(getScanDocumentMethod())
              .addMethod(getScanTwoSidedDocumentMethod())
              .build();
        }
      }
    }
    return result;
  }
}
