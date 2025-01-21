package client

import (
	"context"
	"fmt"
	"github.com/idnorm/id-extraction/sdk/code/go/client/dial_options"
	v1 "github.com/idnorm/id-extraction/sdk/code/go/proto/ddx/v1"
	"google.golang.org/grpc"
	"google.golang.org/grpc/codes"
	"google.golang.org/grpc/metadata"
	"time"
)

type Client interface {
	Scan(ctx context.Context, imgJpegBytes []byte, config *v1.ScanConfig) (*v1.ScanDocumentResponse, error)
}

//
//
//

type Impl struct {
	client v1.ExtractionClient
}

type clientConfig struct {
	Host             string
	LicenseKeyBase64 string
	*dial_options.DialConfig
}

type Option func(*clientConfig)

const (
	defaultHost      = "ddx.idnorm.com:443"
	licenseKeyHeader = "vdil-license-key"
)

func NewClient(opts ...Option) (*Impl, error) {
	cfg := &clientConfig{
		Host: defaultHost,
		DialConfig: &dial_options.DialConfig{
			Target: defaultHost,
		},
	}
	for _, opt := range opts {
		opt(cfg)
	}
	if cfg.Host == defaultHost && cfg.LicenseKeyBase64 == "" {
		return nil, fmt.Errorf("license key is empty")
	}

	dialOpts := dial_options.DialOptions(dial_options.WithConfig(cfg.DialConfig))

	if cfg.LicenseKeyBase64 != "" {
		dialOpts = append(dialOpts, grpc.WithUnaryInterceptor(
			func(ctx context.Context, method string, req, reply any, cc *grpc.ClientConn, invoker grpc.UnaryInvoker, opts ...grpc.CallOption) error {
				ctx = metadata.AppendToOutgoingContext(context.Background(), licenseKeyHeader, cfg.LicenseKeyBase64)
				return invoker(ctx, method, req, reply, cc, opts...)
			},
		), grpc.WithStreamInterceptor(
			func(ctx context.Context, desc *grpc.StreamDesc, cc *grpc.ClientConn, method string, streamer grpc.Streamer, opts ...grpc.CallOption) (grpc.ClientStream, error) {
				ctx = metadata.AppendToOutgoingContext(context.Background(), licenseKeyHeader, cfg.LicenseKeyBase64)
				return streamer(ctx, desc, cc, method, opts...)
			},
		))
	}

	grpcConn, err := grpc.NewClient(cfg.Host, dialOpts...)

	if err != nil {
		return nil, err
	}
	client := v1.NewExtractionClient(grpcConn)
	return &Impl{client: client}, nil
}

func (c *Impl) Scan(ctx context.Context, imgJpegBytes []byte, config *v1.ScanConfig) (*v1.ScanDocumentResponse, error) {
	return c.client.ScanDocument(ctx, &v1.ScanDocumentRequest{
		ImageJpeg: imgJpegBytes,
		Config:    config,
	})
}

// Options

func WithHost(host string) Option {
	return func(cfg *clientConfig) {
		cfg.Host = host
	}
}

func WithLicenseKeyBase64(key string) Option {
	return func(cfg *clientConfig) {
		cfg.LicenseKeyBase64 = key
	}
}

func WithRetries(retries int) Option {
	return func(cfg *clientConfig) {
		cfg.Retries = retries
	}
}

func WithExponentialBackoff(backoff time.Duration) Option {
	return func(cfg *clientConfig) {
		cfg.ExponentialBackoff = backoff
	}
}

func WithWaitForReady(wait bool) Option {
	return func(cfg *clientConfig) {
		cfg.WaitForReady = wait
	}
}

func WithRetryCodes(codes ...codes.Code) Option {
	return func(cfg *clientConfig) {
		cfg.RetryCodes = codes
	}
}
