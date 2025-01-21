# id-extract-service

![Version: 0.1.0](https://img.shields.io/badge/Version-0.1.0-informational?style=flat-square)

A Helm chart for Kubernetes

## Requirements

| Repository | Name | Version |
|------------|------|---------|
| oci://registry-1.docker.io/bitnamicharts | common | 2.x.x |
| oci://us-central1-docker.pkg.dev/idnorm/charts | serving-chart | 0.1.13 |

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| env | list | `[]` | Extra environment variables for the container |
| hpa.annotations | object | `{}` | Optional custom annotations for HPA |
| hpa.enabled | bool | `false` | set to true to enable HPA |
| hpa.labels | object | `{}` | Optional custom labels for HPA |
| hpa.maxReplicas | int | `10` | HPA max replicas |
| hpa.minReplicas | int | `1` | HPA min replicas |
| hpa.targetCPUUtilizationPercentage | int | `80` | Target CPU utilization percentage |
| hpa.targetMemoryUtilizationPercentage | int | `80` | Target memory utilization percentage |
| image.pullPolicy | string | `"IfNotPresent"` | Container image pull policy |
| image.repository | string | `"us-central1-docker.pkg.dev/idnorm/idnorm-pub/idex"` | Container image repository |
| image.tag | string | `"v1.6.30"` | Container image tag |
| ingress.annotations | object | `{"cert-manager.io/cluster-issuer":"letsencrypt-prod","external-dns.custom.kubernetes.io/zone":"public","nginx.ingress.kubernetes.io/force-ssl-redirect":"true"}` | Additional annotations for the Ingress resource |
| ingress.className | string | `"nginx"` | IngressClass that will be be used |
| ingress.enabled | bool | `false` | Enable ingress controller resource |
| ingress.host | string | `"idex.example.com"` | Hostname to be used for the ingress |
| ingress.tls | bool | `false` | Enable TLS configuration for the hostname |
| kpa | object | `{"autoscaling":{"initialScale":1,"maxScale":5,"metricType":"concurrency","minScale":0,"scaleDownDelay":"1m","scaleToZeroGracePeriod":"30s","stableWindow":"30s","target":5,"targetUtilizationPercentage":80},"enabled":true,"http":false}` | KNative pod autoscaling |
| kpa.autoscaling.initialScale | int | `1` | Initial number of replicas |
| kpa.autoscaling.maxScale | int | `5` | Maximum number of replicas |
| kpa.autoscaling.metricType | string | `"concurrency"` | Metric type for autoscaling (concurrency or rps) |
| kpa.autoscaling.minScale | int | `0` | Minimum number of replicas, keep 0 to scale to zero when there is no traffic |
| kpa.autoscaling.scaleDownDelay | string | `"1m"` | Delay before scaling down |
| kpa.autoscaling.scaleToZeroGracePeriod | string | `"30s"` | Grace period before scaling to zero |
| kpa.autoscaling.stableWindow | string | `"30s"` | Window for averaging metrics |
| kpa.autoscaling.target | int | `5` | Target number of concurrent requests |
| kpa.autoscaling.targetUtilizationPercentage | int | `80` | Target utilization percentage |
| kpa.enabled | bool | `true` | Enable knative pod autoscaling |
| kpa.http | bool | `false` | Enable HTTP, exposes gRPC only otherwise |
| labels | object | `{}` | Additional labels for the deployment |
| livenessProbe | object | `{}` | Liveness probe configuration. If empty uses default grpc health probe |
| podLabels | object | `{}` | Additional labels for the pods |
| readinessProbe | object | `{}` | Readiness probe configuration. If empty uses default grpc health probe |
| replicaCount | int | `1` | Number of replicas for the deployment |
| resources.limits.cpu | string | `"200m"` | Maximum CPU allocation |
| resources.limits.memory | string | `"256Mi"` | Maximum memory allocation |
| resources.requests.cpu | string | `"100m"` | Requested CPU allocation |
| resources.requests.memory | string | `"128Mi"` | Requested memory allocation |
| service.annotations | object | `{}` | Additional annotations for the service |
| service.clusterIP | string | `""` | ClusterIP if service type is ClusterIP |
| service.labels | object | `{}` | Additional labels for the service |
| service.loadBalancerIP | string | `""` | LoadBalancer IP if service type is LoadBalancer |
| service.loadBalancerSourceRanges | list | `[]` | Load Balancer sources |
| service.nodePorts | object | `{"grpc":"","http":""}` | Node ports to expose |
| service.ports | object | `{"grpc":8005,"http":8000}` | Service ports |
| service.type | string | `"ClusterIP"` | Kubernetes Service type |
| serving-chart | object | `{"deployments":[{"hpa":{"enabled":false},"knative":{"autoscaling":{"scaleDownDelay":"10m","scaleToZeroGracePeriod":"10m"},"enabled":true},"models":["f4e44a731f7df858","6f697701fc10ce13","fc0dfb12fad78f07","750dac66af62e6b2","2ac3470c50c2bd40","26a3a230499ebb48","077c98276e7ae1a0","ba5c6de27f689d2d","3c27c64bd11d5643"],"name":"extraction","resources":{"limits":{"cpu":"2000m","memory":"2000Mi"},"requests":{"cpu":"100m","memory":"100Mi"}}}],"global":{"image":{"name":"us-central1-docker.pkg.dev/idnorm/idnorm-pub/serving","tag":"v0.1.1-skylake"},"modelStorage":{"gc":{"bucket":"idnorm-models-enc"}}}}` | Values for serving-chart dependency |
| serving-chart.deployments[0].hpa.enabled | bool | `false` | set to true to enable HPA, by default off and is using knative |
| serving-chart.deployments[0].models | list | `["f4e44a731f7df858","6f697701fc10ce13","fc0dfb12fad78f07","750dac66af62e6b2","2ac3470c50c2bd40","26a3a230499ebb48","077c98276e7ae1a0","ba5c6de27f689d2d","3c27c64bd11d5643"]` | List of models |
| serving-chart.deployments[0].resources | object | `{"limits":{"cpu":"2000m","memory":"2000Mi"},"requests":{"cpu":"100m","memory":"100Mi"}}` | Resource settings for deployment, configure with regards to your environment needs |
| serving-chart.deployments[0].resources.limits | object | `{"cpu":"2000m","memory":"2000Mi"}` | Resource limits for deployment |
| serving-chart.deployments[0].resources.limits.cpu | string | `"2000m"` | Maximum CPU allocation |
| serving-chart.deployments[0].resources.limits.memory | string | `"2000Mi"` | Maximum memory allocation |
| serving-chart.deployments[0].resources.requests | object | `{"cpu":"100m","memory":"100Mi"}` | Resource requests for deployment |
| serving-chart.deployments[0].resources.requests.cpu | string | `"100m"` | Requested CPU allocation |
| serving-chart.deployments[0].resources.requests.memory | string | `"100Mi"` | Requested memory allocation |
| serving-chart.global.image.tag | string | `"v0.1.1-skylake"` | Tag to specify the image used. Depending on expected CPU architecture one should update the suffix (haswell, skylake, skylake-avx512, icelake) |
| serving-chart.global.modelStorage.gc.bucket | string | `"idnorm-models-enc"` | Bucket with models |

----------------------------------------------
Autogenerated from chart metadata using [helm-docs v1.14.2](https://github.com/norwoodj/helm-docs/releases/v1.14.2)
