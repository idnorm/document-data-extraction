package dial_options

import (
	"crypto/tls"
	grpc_retry "github.com/grpc-ecosystem/go-grpc-middleware/v2/interceptors/retry"
	"google.golang.org/grpc"
	"google.golang.org/grpc/codes"
	"google.golang.org/grpc/credentials"
	"google.golang.org/grpc/credentials/insecure"
	"strings"
	"time"
)

// This is configurable only as a json string atm, for more information see
// https://github.com/grpc/grpc/blob/master/doc/service_config.md
var lbConfigJson = `
{
  "loadBalancingConfig": [ { "round_robin": {} } ]
}
`

type DialConfig struct {
	Target string

	WaitForReady       bool
	ExponentialBackoff time.Duration
	Retries            int
	RetryCodes         []codes.Code
}

func WithRetries(retries int) DialOption {
	return func(cfg *DialConfig) {
		cfg.Retries = retries
	}
}

func WithRetryCodes(codes ...codes.Code) DialOption {
	return func(cfg *DialConfig) {
		cfg.RetryCodes = codes
	}
}

func WithExponentialBackoff(backoff time.Duration) DialOption {
	return func(cfg *DialConfig) {
		cfg.ExponentialBackoff = backoff
	}
}

func WithWaitForReady(wait bool) DialOption {
	return func(cfg *DialConfig) {
		cfg.WaitForReady = wait
	}
}

func WithTarget(target string) DialOption {
	return func(cfg *DialConfig) {
		cfg.Target = target
	}
}

func WithConfig(cfg *DialConfig) DialOption {
	return func(cfg2 *DialConfig) {
		*cfg2 = *cfg
	}
}

func defaultConfig() *DialConfig {
	return &DialConfig{
		WaitForReady:       true,
		ExponentialBackoff: 100 * time.Millisecond,
		Retries:            3,
		RetryCodes:         []codes.Code{codes.Aborted, codes.Unavailable, codes.ResourceExhausted},
	}
}

type DialOption func(cfg *DialConfig)

func TargetDialOptions(target string) []grpc.DialOption {
	opts := make([]grpc.DialOption, 0, 16)
	transportCreds := insecure.NewCredentials()
	if strings.HasSuffix(target, "443") {
		transportCreds = credentials.NewTLS(&tls.Config{})
	}
	opts = append(opts, grpc.WithTransportCredentials(transportCreds))
	if strings.HasPrefix(target, "dns://") {
		opts = append(opts, grpc.WithDefaultServiceConfig(lbConfigJson))
	}
	return opts
}

// DialOptions generates a slice of grpc.DialOption based on specified Options
func DialOptions(opts ...DialOption) []grpc.DialOption {
	cfg := defaultConfig()
	for _, opt := range opts {
		opt(cfg)
	}

	var dialOpts []grpc.DialOption
	if cfg.Target != "" {
		dialOpts = TargetDialOptions(cfg.Target)
	} else {
		dialOpts = make([]grpc.DialOption, 0, 16)
	}

	if len(cfg.RetryCodes) > 0 {
		dialOpts = append(dialOpts,
			grpc.WithUnaryInterceptor(
				grpc_retry.UnaryClientInterceptor(
					grpc_retry.WithCodes(cfg.RetryCodes...),
					grpc_retry.WithMax(uint(cfg.Retries)),
					grpc_retry.WithBackoff(grpc_retry.BackoffExponential(cfg.ExponentialBackoff)),
				),
			),
		)
		dialOpts = append(dialOpts,
			grpc.WithStreamInterceptor(grpc_retry.StreamClientInterceptor(
				grpc_retry.WithCodes(cfg.RetryCodes...),
				grpc_retry.WithMax(uint(cfg.Retries)),
				grpc_retry.WithBackoff(grpc_retry.BackoffExponential(cfg.ExponentialBackoff)),
			)),
		)
	}
	dialOpts = append(dialOpts, grpc.WithDefaultCallOptions(grpc.WaitForReady(cfg.WaitForReady)))
	return dialOpts
}
