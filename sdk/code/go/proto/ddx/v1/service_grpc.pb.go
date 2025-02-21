// Code generated by protoc-gen-go-grpc. DO NOT EDIT.
// versions:
// - protoc-gen-go-grpc v1.5.1
// - protoc             (unknown)
// source: proto/ddx/v1/service.proto

package v1

import (
	context "context"
	grpc "google.golang.org/grpc"
	codes "google.golang.org/grpc/codes"
	status "google.golang.org/grpc/status"
)

// This is a compile-time assertion to ensure that this generated file
// is compatible with the grpc package it is being compiled against.
// Requires gRPC-Go v1.64.0 or later.
const _ = grpc.SupportPackageIsVersion9

const (
	Extraction_ScanDocument_FullMethodName         = "/proto.ddx.v1.Extraction/ScanDocument"
	Extraction_ScanTwoSidedDocument_FullMethodName = "/proto.ddx.v1.Extraction/ScanTwoSidedDocument"
)

// ExtractionClient is the client API for Extraction service.
//
// For semantics around ctx use and closing/ending streaming RPCs, please refer to https://pkg.go.dev/google.golang.org/grpc/?tab=doc#ClientConn.NewStream.
type ExtractionClient interface {
	// Detects document on a given image and extracts all relevant fields. For input parameters
	// see ScanDocumentRequest Model documentation (in swagger, click on the "Model" in the request "Body" part)
	ScanDocument(ctx context.Context, in *ScanDocumentRequest, opts ...grpc.CallOption) (*ScanDocumentResponse, error)
	// Expects two images, one for front side of the document and one for back side of the document.
	// Scans both sides and extracts all relevant fields.
	// see ScanTwoSidedDocumentRequest Model documentation (in swagger, click on the "Model" in the request "Body" part)
	ScanTwoSidedDocument(ctx context.Context, in *ScanTwoSidedDocumentRequest, opts ...grpc.CallOption) (*ScanTwoSidedDocumentResponse, error)
}

type extractionClient struct {
	cc grpc.ClientConnInterface
}

func NewExtractionClient(cc grpc.ClientConnInterface) ExtractionClient {
	return &extractionClient{cc}
}

func (c *extractionClient) ScanDocument(ctx context.Context, in *ScanDocumentRequest, opts ...grpc.CallOption) (*ScanDocumentResponse, error) {
	cOpts := append([]grpc.CallOption{grpc.StaticMethod()}, opts...)
	out := new(ScanDocumentResponse)
	err := c.cc.Invoke(ctx, Extraction_ScanDocument_FullMethodName, in, out, cOpts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *extractionClient) ScanTwoSidedDocument(ctx context.Context, in *ScanTwoSidedDocumentRequest, opts ...grpc.CallOption) (*ScanTwoSidedDocumentResponse, error) {
	cOpts := append([]grpc.CallOption{grpc.StaticMethod()}, opts...)
	out := new(ScanTwoSidedDocumentResponse)
	err := c.cc.Invoke(ctx, Extraction_ScanTwoSidedDocument_FullMethodName, in, out, cOpts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

// ExtractionServer is the server API for Extraction service.
// All implementations must embed UnimplementedExtractionServer
// for forward compatibility.
type ExtractionServer interface {
	// Detects document on a given image and extracts all relevant fields. For input parameters
	// see ScanDocumentRequest Model documentation (in swagger, click on the "Model" in the request "Body" part)
	ScanDocument(context.Context, *ScanDocumentRequest) (*ScanDocumentResponse, error)
	// Expects two images, one for front side of the document and one for back side of the document.
	// Scans both sides and extracts all relevant fields.
	// see ScanTwoSidedDocumentRequest Model documentation (in swagger, click on the "Model" in the request "Body" part)
	ScanTwoSidedDocument(context.Context, *ScanTwoSidedDocumentRequest) (*ScanTwoSidedDocumentResponse, error)
	mustEmbedUnimplementedExtractionServer()
}

// UnimplementedExtractionServer must be embedded to have
// forward compatible implementations.
//
// NOTE: this should be embedded by value instead of pointer to avoid a nil
// pointer dereference when methods are called.
type UnimplementedExtractionServer struct{}

func (UnimplementedExtractionServer) ScanDocument(context.Context, *ScanDocumentRequest) (*ScanDocumentResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method ScanDocument not implemented")
}
func (UnimplementedExtractionServer) ScanTwoSidedDocument(context.Context, *ScanTwoSidedDocumentRequest) (*ScanTwoSidedDocumentResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method ScanTwoSidedDocument not implemented")
}
func (UnimplementedExtractionServer) mustEmbedUnimplementedExtractionServer() {}
func (UnimplementedExtractionServer) testEmbeddedByValue()                    {}

// UnsafeExtractionServer may be embedded to opt out of forward compatibility for this service.
// Use of this interface is not recommended, as added methods to ExtractionServer will
// result in compilation errors.
type UnsafeExtractionServer interface {
	mustEmbedUnimplementedExtractionServer()
}

func RegisterExtractionServer(s grpc.ServiceRegistrar, srv ExtractionServer) {
	// If the following call pancis, it indicates UnimplementedExtractionServer was
	// embedded by pointer and is nil.  This will cause panics if an
	// unimplemented method is ever invoked, so we test this at initialization
	// time to prevent it from happening at runtime later due to I/O.
	if t, ok := srv.(interface{ testEmbeddedByValue() }); ok {
		t.testEmbeddedByValue()
	}
	s.RegisterService(&Extraction_ServiceDesc, srv)
}

func _Extraction_ScanDocument_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(ScanDocumentRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(ExtractionServer).ScanDocument(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: Extraction_ScanDocument_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(ExtractionServer).ScanDocument(ctx, req.(*ScanDocumentRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _Extraction_ScanTwoSidedDocument_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(ScanTwoSidedDocumentRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(ExtractionServer).ScanTwoSidedDocument(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: Extraction_ScanTwoSidedDocument_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(ExtractionServer).ScanTwoSidedDocument(ctx, req.(*ScanTwoSidedDocumentRequest))
	}
	return interceptor(ctx, in, info, handler)
}

// Extraction_ServiceDesc is the grpc.ServiceDesc for Extraction service.
// It's only intended for direct use with grpc.RegisterService,
// and not to be introspected or modified (even as a copy)
var Extraction_ServiceDesc = grpc.ServiceDesc{
	ServiceName: "proto.ddx.v1.Extraction",
	HandlerType: (*ExtractionServer)(nil),
	Methods: []grpc.MethodDesc{
		{
			MethodName: "ScanDocument",
			Handler:    _Extraction_ScanDocument_Handler,
		},
		{
			MethodName: "ScanTwoSidedDocument",
			Handler:    _Extraction_ScanTwoSidedDocument_Handler,
		},
	},
	Streams:  []grpc.StreamDesc{},
	Metadata: "proto/ddx/v1/service.proto",
}
