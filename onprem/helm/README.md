# Helm chart

Our helm chart is available on our helm registry

`oci://us-central1-docker.pkg.dev/idnorm/charts`

To use it in your helm simply add it as a dependecy to your 
`Chart.yaml` 

```yaml
apiVersion: v2
name: myChart
description: Example Helm chart for Kubernetes
version: 1.0.0
dependencies:
    - name: idex
      version: <specify version>
      repository: oci://us-central1-docker.pkg.dev/idnorm/charts
```

or deploy it directy using 

```bash
helm install <release-name> oci://us-central1-docker.pkg.dev/idnorm/charts/idex --values <path to values.yaml>
```

To find out more on helm charts values.yaml and configuration options please refer to the source and documentation available [here](charts/idex).